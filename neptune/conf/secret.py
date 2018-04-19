import os
from .debug import DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '%k_^&k0l037n6^_o^#*b4pmn)i(ms!$-id$5%f3g5o54#-*+ge')

if DEBUG:
    ALLOWED_HOSTS = [
        '*'
    ]
else:
    CSRF_COOKIE_SECURE = True

    SESSION_COOKIE_SECURE = True

    ALLOWED_HOSTS = [
        '127.0.0.1'
    ]