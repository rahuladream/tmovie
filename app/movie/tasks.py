from celery import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task
def test_celery_worker(a, b):
    return (a + b)


def start_service():
    test = test_celery_worker.delay(1, 4)
    print(test)
