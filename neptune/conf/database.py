import os

import pymysql
from redis import ConnectionPool

from .base import BASE_DIR

pymysql.install_as_MySQLdb()

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# database configurations(include mysql(as default), sqlites, oracle, postgresql)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DB_NAME', 'smp'),
        'USER': os.environ.get('MYSQL_DB_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_DB_PSW', 'smp_system_12345'),
        'HOST': os.environ.get('MYSQL_DB_HOST', '10.153.115.5'),
        'PORT': os.environ.get('MYSQL_DB_PORT', ''),
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        },
        'CONN_MAX_AGE': None
    },
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'CONN_MAX_AGE': None
    },
    'oracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': os.environ.get('ORACLE_DB_NAME'),
        'USER': os.environ.get('ORACLE_DB_USER'),
        'PASSWORD': os.environ.get('ORACLE_DB_PSW'),
        'CONN_MAX_AGE': None
    },
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('MYSQL_DB_NAME', 'smp'),
        'USER': os.environ.get('MYSQL_DB_NAME', 'smp'),
        'PASSWORD': os.environ.get('MYSQL_DB_NAME', 'smp'),
        'HOST': os.environ.get('MYSQL_DB_NAME', 'smp'),
        'PORT': os.environ.get('MYSQL_DB_NAME', 'smp'),
        'CONN_MAX_AGE': None
    }
}

# lifetime of a database connection

# config database route rule
DATABASE_ROUTERS = ['apps.db_router.router.DBRouter']

# Redis Configuration
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_DB = int(os.getenv('REDIS_DB', '0'))

# init redis connect pool
REDIS_POOL = ConnectionPool(host=REDIS_HOST, port=REDIS_PORT,
                            password=REDIS_PASSWORD, decode_responses=True,
                            db=REDIS_DB)
