from mock_database.generators import enum, value, phrase_from_enum, model
from mock_database.model import Position

position_title = phrase_from_enum(
    enum(['Senior', "Junior"]),
    enum(['Backend', "Frontend", "Go", "Rust", "React", "FullStack", "Machine Learning", "Data Scientist"]),
    value("Developer")
)

Positions = model(Position, {
    Position.position_title.name: position_title,
}).enum(20)
