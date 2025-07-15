from src.worker.celery_config import celery_app


@celery_app.task()
def voucher_task_test():
    """A simple task to add two numbers."""
    return "Voucher Task executed successfully!"