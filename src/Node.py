

class Node:
    def __init__(self, id: int, pos: tuple):
        self.id = id
        self.pos = pos

    def __repr__(self):
        return f"id: {self.id}, pos: {self.pos}"


if __name__ == '__main__':
    pos = (1, 2, 3)
    node = Node(1, pos)

    print(node)


