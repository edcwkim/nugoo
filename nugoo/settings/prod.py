from . import *  # noqa

# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i6^5svhg#&&5ha2sj9hv18n3*2*bw1g$mc+#+m$h1rvczg3lz&'  # TODO: change in production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = '*'

WSGI_APPLICATION = 'nugoo.wsgi.application'
