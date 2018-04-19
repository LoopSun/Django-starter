import os

# 扫描django app下的task
# import djcelery
# djcelery.setup_loader()
from .debug import DEBUG

# 不同任务队列配置
from kombu import Exchange, Queue

if DEBUG:
    CELERYD_CONCURRENCY = 4
    CELERY_DEFAULT_QUEUE = 'neptune_dev'
    CELERY_DEFAULT_ROUTING_KEY = 'neptune_dev'
    CELERY_QUEUES = (
        Queue('neptune_dev', Exchange('neptune_dev'), routing_key='neptune_dev'),
    )
else:
    CELERYD_CONCURRENCY = 20
    CELERY_DEFAULT_QUEUE = 'neptune'
    CELERY_DEFAULT_ROUTING_KEY = 'neptune'
    CELERY_QUEUES = (
        Queue('neptune', Exchange('neptune'), routing_key='neptune'),
    )

# CELERY_ROUTES = {
#     'apps.tsn.tasks.update_date': {'queue': 'process_worker'},
#     'apps.file_upload.tasks.import_hq_tsn_data': {'queue': 'file_depend'},
#     'apps.file_upload.tasks.import_xls_file_task': {'queue': 'file_depend'},
#     'apps.services.tasks.nmap_scan': {'queue': 'thread_worker'},
#     'apps.services.tasks.web_check': {'queue': 'process_worker'},
# }

# 默认配置RabbitMQ为Celery的brokers
BROKER_URL = os.getenv("CELERY_BROKER_URL")
# redis的broker备用
# BROKER_URL = 'redis://localhost:6379'


# 使用和Django一样的时区
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_TRACK_STARTED = True
# 执行结果储存位置
# CELERY_RESULT_BACKEND = 'amqp://admin:admin@localhost:5672//'

# 序列化格式
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'msgpack'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

CELERYBEAT_SCHEDULE = {}

CELERY_CREATE_MISSING_QUEUES = True
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_ACKS_LATE = True
CELERYD_FORCE_EXECV = True  # 非常重要,有些情况下可以防止死锁
CELERYD_MAX_TASKS_PER_CHILD = 100  # 每个worker最多执行100个任务就会被销毁，可防止内存泄露
# BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 41600} # Redis才有效
# CELERYD_TASK_TIME_LIMIT = 600 #24 hours
# CELERYD_TASK_SOFT_TIME_LIMIT = 600
# 任务发出后，经过一段时间还未收到acknowledge , 就将任务重新交给其他worker执行

# QoS
CELERY_ANNOTATIONS = {
}
