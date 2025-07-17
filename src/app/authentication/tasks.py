from src.worker.celery_config import celery_app

@celery_app.task()
def authentication_task_test(email: str=None, token:str=None):
    """A simple task to test authentication functionality."""
    print(f"Testing authentication for user: {email}")
    return "Authentication Task executed successfully!"

@celery_app.task(name="send_welcome_email")
def send_welcome_email(user_id: int):
    print(f"Sending welcome email to user: {user_id}")
    # Here you would implement the logic to send an email to the user
    return f"Welcome email sent to user: {user_id}"

@celery_app.task(name="send_password_reset_email")
def send_password_reset_email(email: str, user_id: int, reset_token_url: str):
    print(f"Sending password reset email to user: {user_id}")
    return f"Password reset email sent to user: {user_id}"

