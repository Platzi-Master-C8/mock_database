from mock_database.datasource import engine
from mock_database.mock import Positions
from mock_database.model import Base

Base.metadata.create_all(engine)

print([Positions() for x in range(0, 10)])
