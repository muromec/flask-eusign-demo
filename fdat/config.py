SOCIAL_AUTH_USER_MODEL = 'fdat.models.User'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'fdat.dstu.EusignFull',
    'fdat.dstu.EusignOauth2',
)

SOCIAL_AUTH_USER_FIELDS = ['username', 'email', 'fullname', 'tax_id']

# auth url is set to http://127.0.0.1:5000/complete/eusign/
SOCIAL_AUTH_EUSIGN_APP_ID = '41ec8bc70e3745d4a0c75fd1b752c44e'

SOCIAL_AUTH_EUSIGN_OAUTH2_KEY = 'dfe23c41bde14a429bea969e6e98c1eb'
