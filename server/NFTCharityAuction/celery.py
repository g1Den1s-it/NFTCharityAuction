import os
from NFTCharityAuction import settings
from celery import Celery
from celery.signals import worker_ready

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NFTCharityAuction.settings")

app = Celery("NFTCharityAuction", broker=settings.CELERY_BROKER_URL)
app.config_from_object("django.conf:settings", namespace="CELETY")
app.autodiscover_tasks()


@worker_ready.connect
def at_start(sender, **kwargs):
    with sender.app.connection() as conn:
        sender.app.send_task('api.tasks.get_event_task')
