import numpy as np
import datetime
from faker import Faker

from mock_database.datasource import session

fake = Faker()


class ModelGenerator:

    def __init__(self, entity, id, fields, length):
        self._id = id
        self.entity = entity
        self.fields = fields
        self.length = length
        self.samples = None
        self._data = []

    def __call__(self, *args, **kwargs):
        def create():
            entity = self.entity(**{name.name: field() for (name, field) in self.fields.items()})
            session.add(entity)
            return entity

        if self.samples is None:
            self._data = [create() for x in range(0, self.length)]
            self.samples = enum(self._data)
            session.commit()

        return self.samples()

    def id(self, as_sequence: bool = False):
        self()
        if as_sequence:
            data_provider = sequence(self._data)
        else:
            data_provider = self.samples

        return lambda: data_provider().__getattribute__(self._id.name)

    def update(self):
        def update_record(row):
            for (field_name, field) in self.fields.items():
                field_value = row.__getattribute__(field_name.name)
                if field_value is None:
                    row.__setattr__(field_name.name, field())
            return row

        if self.samples is None:
            self._data = [update_record(row) for row in session.query(self.entity).all()]
            self.samples = enum(self._data)
            session.commit()

        return self.samples()

    def update_id(self, as_sequence: bool = False):
        self.update()
        if as_sequence:
            data_provider = sequence(self._data)
        else:
            data_provider = self.samples

        return lambda: data_provider().__getattribute__(self._id.name)


class Sequence:

    def __init__(self, values):
        self.values = values
        self.counter = 0

    def __call__(self, *args, **kwargs):
        result = self.values[self.counter]
        self.counter = self.counter + 1
        if self.counter == len(self.values):
            self.counter = 0
        return result


def sequence(values: list):
    return Sequence(values)


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


def text(length):
    """
    Produce random text
    :return:
    """
    return lambda: str(fake.text())[:length]


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


def model(entity, id, fields, samples):
    """
    Produce entities and store them in the database
    :param entity:
    :param fields:
    :param samples:
    :return:
    """
    return ModelGenerator(entity, id, fields, samples)


def company_name(length):
    """
    Produce random company names
    :return:
    """
    taken = set()

    def take_name():
        new_value = fake.company()[:length]
        if new_value in taken:
            return take_name()
        taken.add(new_value)
        return new_value

    return lambda: take_name()


def name(length):
    """
    Produce random person name
    :return:
    """
    return lambda: fake.name()[:length]


def random_int(min, max):
    """
    Produce random number in range
    :param min:
    :param max:
    :return:
    """
    return lambda: min + np.random.randint(max - min)


def random_float(min, max):
    """
    Produce random number in range
    :param min:
    :param max:
    :return:
    """
    return lambda: min + np.random.rand() * max


def boolean():
    """
    Produce a random boolean value
    :return:
    """
    return lambda: (np.random.randint(100) % 2) == 0


def datetime_between(start, end):
    """
    produce a random date time between two dates
    :param start:
    :param end:
    :return:
    """
    return lambda: fake.date_time_between_dates(datetime_start=start, datetime_end=end)
