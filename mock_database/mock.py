from mock_database.generators import enum, value, model, phrase
from mock_database.model import Example

position_title = phrase(
    enum(['Senior', "Junior"]),
    enum(['Backend', "Frontend", "Go", "Rust", "React", "FullStack", "Machine Learning", "Data Scientist"]),
    value("Developer")
)

# Positions = model(Position, {
#     Position.position_title: position_title,
# }).enum(20)

Examples = model(Example, {
    Example.title: position_title
}, 20)


def mock_data():
    Examples()
