from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "sqlite:///job_placement.db"

engine = create_engine(
    DATABASE_URI,
    connect_args={"check_same_thread": False}
)

Session = sessionmaker(engine)

session = Session()
