from src.worker.celery_config import celery_app

if __name__ == "__main__":
    celery_app.start(argv=["beat", "--loglevel=info"])
