import os
from .base import BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = os.getenv('STATIC_URL', '/static/')

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = os.getenv('STATIC_URL', '/media/')


