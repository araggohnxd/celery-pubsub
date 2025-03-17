from celery import Celery


app = Celery(
    "celery-pubsub",
    broker="gcpubsub://projects/celery-pubsub",
    backend="gs://celery-result-backend/tasks?gcs_project=celery-pubsub",
)


@app.task
def hello():
    return "hello"
