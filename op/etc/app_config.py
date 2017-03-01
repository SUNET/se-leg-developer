import os

DEBUG = True
SERVER_NAME = 'demo.seleg_dev'
APPLICATION_ROOT = '/op'
PREFERRED_URL_SCHEME = 'https'

basepath = os.path.dirname(os.path.realpath(__file__))

PROVIDER_SIGNING_KEY = {
    'PATH': os.path.join(basepath, 'private.pem'),
    'KID': 'test_kid'
}

PROVIDER_SUBJECT_IDENTIFIER_HASH_SALT = 'test_salt'
TEST_NONCE = ['test']
PACKAGES = [
        'se_leg_op.plugins.se_leg_vetting_process',
        'se_leg_op.plugins.nstic_vetting_process'
]

DB_URI = 'mongodb://se_leg_op:se_leg_op_pw@mongodb'
REDIS_URI = 'redis://redis'
