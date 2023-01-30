from time import sleep
from celery import shared_task
# from storefront.celery import celery

# Below method, since importing file from the storefront app, will pose problem in scaling of apps, therefore we need to apply the shared_task once, since it is independent of the storefront app

# @celery.task

# applying the celery decorator
@shared_task
def notify_customers(message):
    print('Sending 10k emails...')
    print(message)
    sleep(10)
    print('Emails were successfully sent!')