from celery.utils.log import get_task_logger
from celery import shared_task
from celery import current_task
from time import sleep
from src.worker.celery import celery_app

logger = get_task_logger(__name__)


@celery_app.task(acks_late=True)
def add(x, y):
    res = x + y
    logger.info("Adding %s + %s, res: %s" % (x, y, res))
    return res


@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    for i in range(1, 11):
        sleep(1)
        current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': i * 10})
    return f"test task return {word}"
