from src.worker.celery_config import celery_app


@celery_app.task()
def user_task_test():
    """A simple task to add two numbers."""
    return "User Task executed successfully!"


@celery_app.task(name="src.app.users.tasks.send_email")
def send_email(user_id: int):
    print(f"Sending email to user: {user_id}")