from celery import Celery
from celery.schedules import crontab
import pkgutil
import src.app

celery_app = Celery(
    "geo_off",
    broker="amqp://guest:guest@localhost:5672//",
    backend="rpc://"
)

def discover_task_modules():
    """Discover all task modules under src.app.*"""
    modules = []
    for _, module_name, is_pkg in pkgutil.iter_modules(src.app.__path__):
        full_module_path = f"src.app.{module_name}"
        modules.append(full_module_path)
    return modules


celery_app.autodiscover_tasks(packages=discover_task_modules())


celery_app.conf.beat_schedule = {
    "run-health-check-every-minute": {
        "task": "src.worker.celery_config.health_check",
        "schedule": crontab(minute="*"), # Every minute
        "args": ()
    },
    "run-voucher-parse_outlook-every-minute": {
        "task": "src.app.voucher.tasks.parse_outlook_emails",
        "schedule": crontab(minute="*"), # Every minute
        "args": ()
    },
    "run-user-task-test-every-5-minutes": {
        "task": "src.app.users.tasks.user_task_test",
        "schedule": crontab(minute="*/5"), # Every 5 minutes
        "args": ()
    },
    "run-voucher-task-test-every-10-minutes": {
        "task": "src.app.voucher.tasks.voucher_task_test",
        "schedule": crontab(minute="*/10"), # Every 10 minutes
        "args": ()
    },
    
    # "run-another-task-every-hour": {
    #     "task": "src.app.some_other_module.some_task",
    #     "schedule": crontab(minute=0, hour="*"), # Every hour
    #     "args": ()
    # },
    # "run-daily-task-at-midnight": {
    #     "task": "src.app.another_module.daily_task",
    #     "schedule": crontab(minute=0, hour=0), # Every day at midnight
    #     "args": ()
    # }
}

# Example task
@celery_app.task(name="src.worker.celery_config.health_check")
def health_check():
    return "Celery is alive!"
