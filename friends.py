from ast import Num
from os import name


class Friends:
    connections = []
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        return set(name
                   for c in self.connections
                   for name in c)

    def connected(self, name):
        connections = list(filter(lambda x: name in x, self.connections))
        names = []
        for c in connections:
            for n in list(c):
                if n != name: names.append(n)
        return set(names)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
