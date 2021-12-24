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
        curr = node_list.get(id1)  # src


        prev = node_list.copy()  #

        prev = dict.fromkeys(prev, None)  # init all the previous to null

        print(node_list)
        print(prev)

        for i in graph_algo.all_out_edges_of_node(curr):
             temp_dist = Node.get_weight(curr) + i.get_weight ## idea
            

    # print(temp_dist)

        pass


    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':
    g = DiGraph()
    pos = (1, 2, 3)
    g.add_node(1, pos)
    g.add_node(2, pos)
    g.add_edge(1, 2, 0)
    g.add_edge(2, 1, 0)
    g.add_node(3, pos)

    algo = GraphAlgo(g)

    algo.shortest_path(1, 2)
