import copy
from abc import ABC

from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import json
from DiGraph import *
from Node import *
from PriorityQueue import *
import heapq


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
        #print(curr)
        curr.set_weight(0)

        #print(curr)

        prev = node_list.copy()  #

        prev = dict.fromkeys(prev, None)  # init all the previous to null

        pq = PriorityQueue()

        for _ in graph_algo.get_all_v():
            if curr.id == id2:
                break
            curr.set_tag(2)

            for i in graph_algo.all_out_edges_of_node(curr.id):
                print(i)
                temp_dist = 0
                node_dest: Node = graph_algo.get_all_v().get(i)
                if node_dest.get_tag() != 2:
                   # print(node_dest.weight)

                    w: float = graph_algo.all_out_edges_of_node(curr.id).get(i)  # weight of the the  d1-->i edge
                    #print("w",graph_algo.all_out_edges_of_node(curr.id).get(i))


                    temp_dist = curr.get_weight() + float(w)
                    print("temp ", temp_dist)
                    if node_dest.get_tag() == 0:
                        pq.add(node_dest)
                        node_dest.set_tag(1)

                    if temp_dist <= node_dest.weight:
                        node_dest.set_weight(temp_dist)
                       # prev[node_dest.id] = curr.id
            # find the min from the adjacency

            curr = pq.pop()

        # prev , path list
        path_list.append(id2)
        id = prev[id2]


        while id is not None:
            path_list.append(id)
            id = prev[id]
        path_list.reverse()
        ans: Node = graph_algo.get_all_v().get(id2)
        return ans.weight, path_list


    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':
    graph: GraphInterface = DiGraph()
    graph_algo: GraphAlgoInterface = GraphAlgo(graph)

    for i in range(7):
        graph.add_node(i)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 4)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 7)
    graph.add_edge(2, 4, 3)
    graph.add_edge(4, 3, 2)
    graph.add_edge(3, 5, 1)
    graph.add_edge(4, 5, 5)



    print(graph_algo.shortest_path(0,5))
