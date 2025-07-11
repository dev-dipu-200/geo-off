from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.configuration.env_settings import setting


engine = create_engine(setting.MongoDB_URL, connect_args={"serverSelectionTimeoutMS": 5000})  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_mongo_db():
    """Get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



