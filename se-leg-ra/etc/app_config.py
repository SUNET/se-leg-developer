DEBUG = True
SECRET_KEY = 'notasecret'
DB_URI = 'mongodb://se_leg_ra:se_leg_ra_pw@mongodb'
LOGIN_ALTERNATIVES = [
        {'name': 'pysaml2 IdP', 'url': 'https://rasp.se-leg.docker/Shibboleth.sso/Login/idp', 'description': 'Test IdP'},
        {'name': 'pysaml2 IdP 2', 'url': 'https://rasp.se-leg.docker/Shibboleth.sso/Login/idp', 'description': 'Test IdP 2'},
]
LOGOUT_URL = 'https://rasp.se-leg.docker/Shibboleth.sso/Logout'
RA_APP_ID = 'RA-APP-1'
RA_APP_SECRET = 'secret'
VETTING_ENDPOINT = 'https://demo.seleg_dev/op/vetting-result'
AL2_IDP_EXCEPTIONS = [
    'https://idp.se-leg.docker/idp.xml'
]
