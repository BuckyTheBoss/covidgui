from django.contrib.messages import constants as messages
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'RANDOMLY_GENERATE_APP_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Put the address/domain-name where the server will run in the list below
ALLOWED_HOSTS = ['127.0.0.1', ]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
IMPORT_EXPORT_USE_TRANSACTIONS = True
LOGIN_REDIRECT_URL = 'new_form'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = '/'
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
# How long after idling a user is logged out, in seconds
SESSION_COOKIE_AGE = 900
SESSION_SAVE_EVERY_REQUEST = True
SIGNUP_KEY = 'SOME-STRING'
