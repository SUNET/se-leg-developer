DEBUG = True
SECRET_KEY = 'notasecret'
DB_URI = 'mongodb://se_leg_ra:se_leg_ra_pw@mongodb'
LOGIN_ALTERNATIVES = [
        {'name': 'pysaml2 IdP', 'url': 'https://rasp.se-leg.docker/Shibboleth.sso/Login/idp', 'description': 'Test IdP'},
        {'name': 'Sweden Connect', 'url': 'https://rasp.se-leg.docker/Shibboleth.sso/Login/swedenconnect', 'description': 'Svensk e-legitimation'},
]
LOGOUT_URL = 'https://rasp.se-leg.docker/Shibboleth.sso/Logout'
RA_APP_ID = 'RA-APP-1'
RA_APP_SECRET = 'secret'
VETTING_ENDPOINT = 'https://demo.seleg_dev/op/vetting-result'
AL2_IDP_EXCEPTIONS = [
    'https://idp.se-leg.docker/idp.xml'
]
AL2_ASSURANCES = [
    'http://id.elegnamnden.se/loa/1.0/loa3'
]
