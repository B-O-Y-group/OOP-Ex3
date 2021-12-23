from abc import ABC
from Node import *
from GraphInterface import *


class DiGraph(GraphInterface, ABC):
    def __init__(self):
        self.MC = 0
        self.nodes = {}
        self.edges_out = {}
        self.edges_in = {}

    def v_size(self) -> int:
        return self.nodes.__len__()

    def e_size(self) -> int:
        return self.edges_out.__len__()

    def get_all_v(self) -> dict:
        dict_nodes = {i: self.nodes.keys() for i in range(0, len(self.nodes))}
        return dict(dict_nodes)

    def all_in_edges_of_node(self, id1: int) -> dict:
        # node_in = {self.nodes.get(id1): {self.nodes.get(id2):self.edges(id1,id2)}}
        return None

    def all_out_edges_of_node(self, id1: int) -> dict:

        return self.edges_out

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes:  # by key
            if id1 not in self.edges_out:
                self.edges_out[id1] = {}  # create new
            if id2 not in self.edges_in:
                self.edges_in[id2] = {}
            self.edges_out[id1][id2] = weight
            self.edges_in[id2][id1] = weight
            self.MC += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        self.nodes[node_id] = Node(node_id, pos)

        # Node(node_id, pos)
        # list.count(node_id)
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.nodes.keys() in self.nodes:
            self.MC += 1
            return self.nodes.pop()
        else:
            print("This node does not exist")

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.edges_out.keys() in self.edges_out:
            self.MC += 1
            return self.edges_out.pop()
        else:
            print("This edge does not exist")

    def __str__(self):
        return f"nodes: {self.nodes}\nedges: {self.edges_out}"


if __name__ == '__main__':
    g = DiGraph()
    pos = (1, 2, 3)

    g.add_node(1, pos)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(1, 2, 0)
    g.add_edge(1, 3, 0)
    list = g.all_out_edges_of_node(1)
    print(list)

    # print(g)
