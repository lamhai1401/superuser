from celery import Celery
import os

# Create the celery app and get the logger
# celery_app = Celery('tasks', broker="amqp://guest@localhost:5672//")
# celery_app.autodiscover_tasks()

celery_app = None

if not bool(os.getenv('DOCKER')):  # if running example without docker
    celery_app = Celery(
        "worker",
        backend="redis://:password123@localhost:6379/0",
        broker="amqp://guest@localhost:5672//",
        include=["src.worker"],
    )
    celery_app.conf.task_routes = {
        "src.worker.tasks.test_celery": "test-queue"}
else:  # running example with docker
    celery_app = Celery(
        "worker",
        backend="redis://:password123@redis:6379/0",
        broker="amqp://guest@localhost:5672//",
        include=["src.worker"],
    )
    celery_app.conf.task_routes = {
        "src.worker.tasks.test_celery": "test-queue"}

celery_app.conf.update(task_track_started=True)
celery_app.autodiscover_tasks()
