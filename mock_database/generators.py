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
    """
    Choose randomly a value from a list
    :param values: listo of values
    :return: a generator
    """
    return lambda: np.random.choice(values)


def phrase(*values):
    """
    create a phrase use generator values
    :param values: possible values
    :return: a string combining the different values
    """
    return lambda: " ".join([v() for v in values])


def value(v):
    """
    Return a constant value
    :param v:
    :return:
    """
    return lambda: v


def text():
    """
    Produce random text
    :return:
    """
    return lambda: fake.text()


def url():
    """
    produce a random url
    :return:
    """
    return phrase(
        enum(["http://", "https://"]),
        enum(["platzi", "amazon", "google", "globant"]),
        value("."),
        enum(["com", "net", "org"])
    )


def model(entity, fields, samples):
    """
    Produce entities and store them in the database
    :param entity:
    :param fields:
    :param samples:
    :return:
    """
    return ModelGenerator(entity, fields, samples)
