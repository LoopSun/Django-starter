import datetime

import jwt
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa


AES_KEY = b"-jWcDxqBr2VQyymoRTXnGncprp-5Amzm1-owm5jZmqc="


### 对称加密
def encrypt_data_by_syn(message, key=AES_KEY):
    f = Fernet(key)
    token = f.encrypt(message)
    return token


def decrypt_data_by_syn(message, key=AES_KEY):
    f = Fernet(key)
    token = f.decrypt(message)
    return token