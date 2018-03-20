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

# flask-registry config
PACKAGES = [
        'se_leg_op.plugins.se_leg_vetting_process',
        'se_leg_op.plugins.nstic_vetting_process'
]
EXTENSIONS = ['se_leg_op.plugins.nstic_vetting_process.license_service']
USER_CFG = True

DB_URI = 'mongodb://se_leg_op:se_leg_op_pw@mongodb'
REDIS_URI = 'redis://redis'

# Yubico service config
MOBILE_VERIFY_WSDL = 'https://s01.cloud-xip.miteksystems.com/Plugins/ProductServices.PhotoVerify/services/v1.0/PhotoVerifyService.svc?singleWsdl'
MOBILE_VERIFY_USERNAME = 'username'
MOBILE_VERIFY_PASSWORD = 'secret'
MOBILE_VERIFY_TENANT_REF = 'tenant_ref'

# se-leg service config
SELEG_VETTING_APPS = {
    'RA-APP-1': {
        'secret': 'secret'
    }
}
