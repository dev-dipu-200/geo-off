from src.worker.celery_config import celery_app

@celery_app.task()
def authentication_task_test():
    """A simple task to test authentication functionality."""
    return "Authentication Task executed successfully!"

@celery_app.task(name="send_welcome_email")
def send_welcome_email(user_id: int):
    print(f"Sending welcome email to user: {user_id}")
    # Here you would implement the logic to send an email to the user
    return f"Welcome email sent to user: {user_id}"

@celery_app.task(name="send_password_reset_email")
def send_password_reset_email(user_id: int):
    print(f"Sending password reset email to user: {user_id}")
    # Here you would implement the logic to send a password reset email to the user
    return f"Password reset email sent to user: {user_id}"

