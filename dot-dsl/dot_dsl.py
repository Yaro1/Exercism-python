NODE, EDGE, ATTR = range(3)


def check_valid(item):
    if len(item) < 3:
        raise TypeError("Undefined element.")
    if item[0] == NODE:
        if len(item) == 3 and isinstance(item[1], str) and isinstance(item[2], dict):
            return True
        else:
            raise ValueError("Wrong data for node.")
    elif item[0] == EDGE:
        if len(item) == 4 and isinstance(item[1], str) and isinstance(item[2], str) and isinstance(item[3], dict):
            return True
        else:
            raise ValueError("Wrong data for edge.")
    elif item[0] == ATTR:
        if len(item) == 3 and isinstance(item[1], str) and isinstance(item[2], str):
            return True
        else:
            raise ValueError("Wrong data for attr.")
    return False


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if data:
            if not isinstance(data, list):
                raise TypeError("Data should be list.")
            for item in data:
                if not check_valid(item):
                    raise ValueError("Wrong element. You can use only NODE, EDGE, ATTR.")
                if item[0] == NODE:
                    self.nodes.append(Node(item[1], item[2]))
                elif item[0] == EDGE:
                    self.edges.append(Edge(item[1], item[2], item[3]))
                elif item[0] == ATTR:
                    self.attrs[item[1]] = item[2]

