import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')
# instance of celery
celery = Celery('storefront')
# celery can find config variables from here
celery.config_from_object('django.conf:settings', namespace='CELERY')
# function to autodiscover the pre-allocated tasks
celery.autodiscover_tasks()
