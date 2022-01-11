from mock_database.datasource import engine
from mock_database.model import Base

Base.metadata.create_all(engine)
