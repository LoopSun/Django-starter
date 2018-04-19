#-*-coding:utf-8-*-
__author__ = 'loopsun'

import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key

JWT_PRIVATE_KEY = os.path.join(BASE_DIR, 'neptune', 'conf', 'keys', 'api_signature', 'key.pem')
JWT_PUBLIC_KEY = os.path.join(BASE_DIR, 'neptune', 'conf', 'keys', 'api_signature', 'public.pem')

DATA_PRIVATE_KEY = os.path.join(BASE_DIR, 'neptune', 'conf', 'keys', 'api_data', 'key.pem')
DATA_PUBLIC_KEY = os.path.join(BASE_DIR, 'neptune', 'conf', 'keys', 'api_data', 'public.pem')

def load_key(key_path, key_type):
    key_obj = None
    with open(key_path, 'rb') as key_file:
        if key_type == "private":
            key_obj = load_pem_private_key(key_file.read(), password=None, backend=default_backend())
        elif key_type == "public":
            key_obj = load_pem_public_key(key_file.read(), backend=default_backend())
    return key_obj

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': "ef6(z5-u!w@*y1(ot^3tqw20%_*8311iw_so#w_e_k=6-l&qkj",
    'JWT_GET_USER_SECRET_KEY': None,
    # 'JWT_PUBLIC_KEY': load_key(JWT_PUBLIC_KEY, "public"),
    # 'JWT_PRIVATE_KEY': load_key(JWT_PRIVATE_KEY, "private"),
    'JWT_ALGORITHM': 'RS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=842000),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,

}


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # HEADER: """ Authorization: JWT <your_token> """
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
    ),
    'PAGE_SIZE': 10,
}