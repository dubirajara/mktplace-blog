from django.core.management import utils


CONFIG_ENV = f"""
SECRET_KEY={utils.get_random_secret_key()}
DEBUG=True
ALLOWED_HOSTS=*

DEFAULT_FROM_EMAIL=admin@exemple.com
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=localhost
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=25
EMAIL_USE_TLS=False

META_DESCRIPTION=test blog.
META_TITLE=test blog.
"""

# Writing our configuration file to '.env'
with open('mktplace/.env', 'w') as configfile:
    configfile.write(CONFIG_ENV)
    print('Created the .env file successfully.')
