"""A application for tracking social network"""


class Person:
    """A class for tracking people and their connection
    Attributes:
        name (str): name of the person
        connections (set of connection): a set of people that a person knows
    """

    def __init__(self, name):
        self.name = name
        self.connections = set()
