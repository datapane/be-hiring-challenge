from config import celery_app


@celery_app.task()
def save_dataset():
    ...


@celery_app.task()
def create_excel():
    ...


@celery_app.task()
def create_plot():
    ...
