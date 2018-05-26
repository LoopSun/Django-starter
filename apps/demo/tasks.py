import django
django.setup()

from celery import task

@task
def drink():
    print("Should Drink")


@task
def breakfast():
    print("Breakfast Time")
