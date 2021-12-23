from abc import ABC
from Node import *
from GraphInterface import *


class DiGraph(GraphInterface, ABC):
    def __init__(self):
        self.MC = 0
        self.nodes = {}
        self.edges = {}

    def v_size(self) -> int:
        return self.nodes.__len__()

    def e_size(self) -> int:
        return self.edges.__len__()

    def get_all_v(self) -> dict:
        dict_nodes = {i: self.nodes.keys() for i in range(0, len(self.nodes))}
        return dict(dict_nodes)

    def all_in_edges_of_node(self, id1: int) -> dict:
        node_in = {self.nodes.get(id1): {self.nodes.get(id2):self.edges(id1,id2)}}
        return node_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes:  # by key
            if id1 not in self.edges:
                self.edges[id1] = {}  # create new
            self.edges[id1][id2] = weight
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
        if self.edges.keys() in self.edges:
            self.MC += 1
            return self.edges.pop()
        else:
            print("This edge does not exist")

    def __str__(self):
        return f"nodes: {self.nodes}\nedges: {self.edges}"


if __name__ == '__main__':
    g = DiGraph()
    pos = (1, 2, 3)

    g.add_node(1, pos)

    print(g)