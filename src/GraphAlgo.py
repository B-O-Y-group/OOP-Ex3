import copy
from abc import ABC

from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import json
from DiGraph import *
from Node import *
from PriorityQueue import *


class GraphAlgo(GraphAlgoInterface, ABC):

    def __init__(self, graph: GraphInterface):
        self.graph = graph

    # def TSP(self, node_lst: List[int]) -> (List[int], float):
    #     super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def get_graph(self) -> GraphInterface:
        # super().get_graph()
        return self.graph

    # add_edge(self, id1: int, id2: int, weight: float)
    ##    add_node(self, node_id: int, pos: tuple = None)

    def load_from_json(self, file_name: str) -> bool:
        try:
            dic = {}
            g = DiGraph()
            with open(file_name, "r") as f:
                dic = json.load(fp=f)
            for n in dic["Nodes"].values():
                ##p = n["pos"].values()
                ## pos = tuple(map(float, pos.split(",")))
                g.add_node(node_id=n["id"], pos=(n["pos"]))

            for e in dic["Edges"].values():
                g.add_edge(id1=["src"], id2=["dest"], weight=["w"])

                self.graph = g
            return True
        except Exception:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as f:
                ## indenter is number rof space
                ## default= lambda  o :o.__dict__ taking the self and change him to dictionaries
                json.dump(self, filePointer=f, indent=4, default=lambda o: o.__dict__)
            return True
        except Exception:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path_list = []
        # the same vertex
        if id1 == id2:
            path_list.append(id1)
            return 0, path_list

        graph_algo = copy.deepcopy(self.get_graph())

        node_list = graph_algo.get_all_v()  # dic of node

        curr: Node = graph_algo.get_all_v().get(id1)
        print(curr)
        curr.set_weight(0)
        print(curr)

        prev = node_list.copy()  #

        prev = dict.fromkeys(prev, None)  # init all the previous to null

        for v in graph_algo.get_all_v():

            for i in graph_algo.all_out_edges_of_node(curr.id):
                node_index: Node = graph_algo.get_all_v().get(i)

                print(node_index.weight)
                w: float = graph_algo.all_out_edges_of_node(id1).get(i)  # weight of the the  d1-->i edge
                temp_dist = curr.get_weight() + w
                if temp_dist <= node_index.weight:
                    node_index.set_weight(temp_dist)

                    print(node_index.weight)

            n: Node = graph_algo.get_all_v().get(v)
            print("---->", n)
            curr = n

    pass


def plot_graph(self) -> None:
    pass


if __name__ == '__main__':
    g = DiGraph()
    pos = (0, 0, 0)
    pos1 = (11, 11, 11)
    pos2 = (12, 12, 12)
    pos3 = (13, 13, 13)

    node1 = Node(0, pos)
    node2 = Node(1, pos1)
    node3 = Node(2, pos2)
    node4 = Node(3, pos3)

    g.add_node(node1.id, node1.pos)
    g.add_node(node2.id, node2.pos)
    g.add_node(node3.id, node3.pos)
    g.add_node(node4.id, node4.pos)

    g.add_edge(node1.id, node2.id, 1)
    g.add_edge(node1.id, node3.id, 2)
    g.add_edge(node1.id, node4.id, 1)
    g.add_edge(node3.id, node4.id, 1)

    algo = GraphAlgo(g)

    # print(algo.get_graph())

    algo.shortest_path(node1.id, node2.id)
