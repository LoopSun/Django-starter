import os

import pymysql
from redis import ConnectionPool

from .base import BASE_DIR

pymysql.install_as_MySQLdb()

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# 数据库配置(默认Mariadb, 包括sqlite3, Oracle, postgresql)
DATABASES = {
    ## 默认Mariadb数据库,
    'default': {
        # 设置Mariadb数据库客户端, python3使用pymysql
        'ENGINE': 'django.db.backends.mysql',
        # 数据库名
        'NAME': os.environ.get('MYSQL_DB_NAME', 'demo'),
        # 数据库用户, 不推荐使用root用户，只拥有访问目标数据库用户， 默认root
        'USER': os.environ.get('MYSQL_DB_USER', 'demo'),
        # 数据库密码， 默认无
        'PASSWORD': os.environ.get('MYSQL_DB_PSW', 'Zhou_111111'),
        # 数据库主机, 默认localhost
        'HOST': os.environ.get('MYSQL_DB_HOST', '127.0.0.1'),
        # 数据库端口, 默认3306
        'PORT': os.environ.get('MYSQL_DB_PORT', '3306'),
        # 设置数据库遇到非法||错误值处理模式
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        # 测试数据库配置
        'TEST': {
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8_general_ci',
        },
        # 数据库长连接
        'CONN_MAX_AGE': None
        ## 推荐字符集: utf8mb4 -- UTF-8 Unicode
        ## 排序规则: 无特殊要求utf8mb4_general_ci即可
    },
    ## 测试||学习||轻量应用推荐
    # 'sqlite3': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     'CONN_MAX_AGE': None
    # },
    ## 适合中大型企业的数据持久化存储方案, 需要运行系统额外的instant-client支持
    ## http://www.oracle.com/technetwork/database/database-technologies/instant-client/overview/index.html
    # 'oracle': {
    #     'ENGINE': 'django.db.backends.oracle',
    #     'NAME': os.environ.get('ORACLE_DB_NAME'),
    #     'USER': os.environ.get('ORACLE_DB_USER'),
    #     'PASSWORD': os.environ.get('ORACLE_DB_PSW'),
    #     'CONN_MAX_AGE': None
    # },
    ## Mariadb的替代品
    # 'postgresql': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': os.environ.get('MYSQL_DB_NAME', 'smp'),
    #     'USER': os.environ.get('MYSQL_DB_NAME', 'smp'),
    #     'PASSWORD': os.environ.get('MYSQL_DB_NAME', 'smp'),
    #     'HOST': os.environ.get('MYSQL_DB_NAME', 'smp'),
    #     'PORT': os.environ.get('MYSQL_DB_NAME', 'smp'),
    #     'CONN_MAX_AGE': None
    # }
}

# 配置数据库路由策略
DATABASE_ROUTERS = ['apps.db_router.router.DBRouter']

# Redis 配置
REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_DB = int(os.getenv('REDIS_DB', '0'))

# 使用全局Redis连接池, 减少连接开销
REDIS_POOL = ConnectionPool(host=REDIS_HOST, port=REDIS_PORT,
                            password=REDIS_PASSWORD, decode_responses=True,
                            db=REDIS_DB)
