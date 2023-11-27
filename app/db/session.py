from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import Settings

import os
from dotenv import load_dotenv

load_dotenv()

connection_string = f"{os.environ.get('DB_ENGINE')}://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"
if os.environ.get('DATABASE_URL'):
    connection_string = os.environ.get('DATABASE_URL')
    
engine = create_engine(connection_string, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)