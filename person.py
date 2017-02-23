class Person:
    count = 0

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections
        self.id = Person.count
        Person.count += 1

    def getName(self):
        return self.name

    def getConnections(self):
        return self.connections
