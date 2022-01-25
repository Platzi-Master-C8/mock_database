from mock_database.datasource import engine, session
from mock_database.mock import update_data
from mock_database.model import Base

Base.metadata.create_all(engine)
update_data()
session.commit()
