import os

TESTING = True
SERVER_NAME = 'demo.seleg_dev'
APPLICATION_ROOT = '/op'
PREFERRED_URL_SCHEME = 'https'

basepath = os.path.dirname(os.path.realpath(__file__))

PROVIDER_SIGNING_KEY = {
    'PATH': os.path.join(basepath, 'private.pem'),
    'KID': 'test_kid'
}

PROVIDER_SUBJECT_IDENTIFIER_HASH_SALT = 'test_salt'

DB_URI = 'mongodb://se_leg_op:se_leg_op_pw@mongodb'
REDIS_URI = 'redis://redis'
