# -*- coding: utf-8 -*-

import sys
import os
import etcd
import yaml
import json
import argparse


__author__ = 'lundberg'

VERBOSE = False


def load_yaml(file_path):
    """
    :param file_path: Full path to a file with configuration in yaml
    :type file_path: str | unicode

    :return: dict representation of the yaml
    :rtype: dict
    """
    try:
        with open(file_path) as f:
            if VERBOSE:
                print('Loading configuration from {!s}'.format(file_path))
            return yaml.load(f)
    except IOError as e:
        sys.stderr.writelines(str(e)+'\n')
        sys.exit(1)


def init_etcd_client(host=None, port=None):
    if not host:
        host = os.environ.get('ETCD_HOST', '127.0.0.1')
    if not port:
        port = int(os.environ.get('ETCD_PORT', '2379'))
    if VERBOSE:
        print('Initializing etcd client {!s}:{!s}'.format(host, port))
    return etcd.Client(host, port)


def write_configuration(client, config, base_namespace_depth, base_ns='', depth=0):
    """
    :param client: etcd client
    :type client: etcd.Client
    :param config: Dictonary with config
    :type config: dict
    :param base_namespace_depth: How deep down the interesting key-value pairs start
    :type base_namespace_depth: int
    :param base_ns: Cumulative base namespace
    :type base_ns: str | unicode
    :param depth: Current depth in the dictionary
    :type depth: int

    Ex

    The following yaml has been loaded from file
    eduid:
        webapp:
            common:
                SAML_CONFIG:
                    xmlsec_binary: /usr/bin/xmlsec1
            oidc_proofing:
                MONGO_URI: mongodb://user:pw@mongodb.docker
                LOG_TYPE:
                   - rotating
                   - gelf

    and results in the a dict like below:

    {
        'eduid': {
            'webapp': {
                'common': {
                    'SAML_CONFIG': {
                        'xmlsec_binary': '/usr/bin/xmlsec1'
                    }
                },
                'oidc_proofing': {
                    'LOG_TYPE': ['rotating', 'gelf'],
                    'MONGO_URI': 'mongodb://user:pw@mongodb.docker'
                }
            }
        }
    }

    With base_namespace_depth set to 3 we know that the key-value pairs below common and oidc_proofing
    are the ones we want write to etcd.

    This will result in the following key-value pairs being written to etcd:
    /eduid/webapp/oidc_proofing/log_type -> '["rotating", "gelf"]'
    /eduid/webapp/oidc_proofing/mongo_uri -> 'mongodb://user:pw@mongodb.docker'
    /eduid/webapp/common/saml_config -> '{"xmlsec_binary": "/usr/bin/xmlsec1"}'
    """

    depth += 1
    for level in config.keys():
        if depth < base_namespace_depth:
            base_ns = '{!s}/{!s}'.format(base_ns, level)
            write_configuration(client, config[level], base_namespace_depth, base_ns, depth)
        else:
            ns = '{!s}/{!s}'.format(base_ns, level)
            for key, value in config[level].items():
                fq_key = '{!s}/{!s}'.format(ns, key).lower()
                json_value = json.dumps(value)

                try:
                    client.write(fq_key, json_value)
                except etcd.EtcdConnectionFailed as e:
                    sys.stderr.writelines(str(e)+'\n')
                    sys.exit(1)

                if VERBOSE:
                    print('{!s} -> {!s}'.format(fq_key, json_value))


def main():
    # User friendly usage output
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--configuration', help='Path to the yaml configuration file.', default='conf.yaml')
    parser.add_argument('-b', '--base-ns-depth', nargs='?', help='Base namespace depth', default=3, type=int)
    parser.add_argument('--host', nargs='?', help='etcd hostname')
    parser.add_argument('--port', nargs='?', help='etcd port')
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    args = parser.parse_args()

    if not args.configuration:
        print('Please provide a configuration file with -c.')
        sys.exit(1)

    if args.verbose:
        global VERBOSE
        VERBOSE = True

    config_dict = load_yaml(args.configuration)
    etcd_client = init_etcd_client(args.host, args.port)
    write_configuration(etcd_client, config_dict, args.base_ns_depth)


if __name__ == '__main__':
    main()

