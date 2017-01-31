# -*- coding: utf-8 -*-

DEBUG = True
SERVER_NAME = 'demo.seleg_dev'
APPLICATION_ROOT = '/nstic-rp'
PREFERRED_URL_SCHEME = 'https'
VETTING_METHOD = 'nstic'

# ================#
#  mongodb config #
# ================#

MONGO_URI = 'mongodb://se_leg_rp:se_leg_rp_pw@mongodb'

# ================#
# OIDC            #
# ================#
CLIENT_REGISTRATION_INFO = {
    'client_id': 'client2',
    'client_secret': 'abcdef'
}

PROVIDER_CONFIGURATION_INFO = {
    'issuer': 'https://demo.seleg_dev/op',
}
USERINFO_ENDPOINT_METHOD = 'POST'

# ================#
# Logging         #
# ================#

LOG_LEVEL = 'DEBUG'
