import numpy as np
from faker import Faker

from mock_database.datasource import session

fake = Faker()


class ModelGenerator:

    def __init__(self, entity, fields):
        self.entity = entity
        self.fields = fields

    def __call__(self, *args, **kwargs):
        entity = self.entity(**{name: field() for (name, field) in self.fields.items()})
        return session.add(entity)

    def enum(self, length):
        result = enum([self() for x in range(0, length)])
        session.commit()
        return result


def enum(values: list):
    return lambda: np.random.choice(values)


def phrase_from_enum(*values):
    return lambda: " ".join([v() for v in values])


def value(v):
    return lambda: v


def text():
    return lambda: fake.text()


def url():
    return phrase_from_enum(
        enum(["http://", "https://"]),
        enum(["platzi", "amazon", "google", "globant"]),
        value("."),
        enum(["com", "net", "org"])
    )


def model(entity, fields):
    return ModelGenerator(entity, fields)
