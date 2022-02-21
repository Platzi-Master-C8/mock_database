from mock_database.datasource import engine, session
from mock_database.mock import mock_data
from mock_database.model import Base

Base.metadata.create_all(engine)
mock_data()
session.commit()
