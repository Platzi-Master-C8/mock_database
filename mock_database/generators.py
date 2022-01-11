import numpy as np
from faker import Faker

from mock_database.datasource import session

fake = Faker()


class ModelGenerator:

    def __init__(self, entity, fields, length):
        self.entity = entity
        self.fields = fields
        self.length = length
        self.samples = None

    def __call__(self, *args, **kwargs):
        def create():
            entity = self.entity(**{name.name: field() for (name, field) in self.fields.items()})
            session.add(entity)
            return entity

        if self.samples is None:
            self.samples = enum([create() for x in range(0, self.length)])
            session.commit()

        return self.samples()


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


def model(entity, fields, samples):
    return ModelGenerator(entity, fields, samples)
