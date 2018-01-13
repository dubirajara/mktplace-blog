#!/usr/bin/env python

"""
Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

CONFIG_STRING = """
SECRET_KEY={}
DEBUG=True
ALLOWED_HOSTS=*

#EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
#EMAIL_HOST=localhost
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
#EMAIL_PORT=25
#EMAIL_USE_TLS=False

META_DESCRIPTION=test blog.
META_TITLE=test blog.
""".strip().format(get_random_string(50, chars))

# Writing our configuration file to '.env'
with open('mktplace/.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
    print('Created the .env file successfully.')
