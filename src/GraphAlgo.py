import copy
import math
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





    """ 
    shortest path :
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        
        the algorithm  check if d[u] + edgeD[u,v] < d[v] -->d[u] = d[v] + edgeD[u,v]
        by going throw all the node and the edge in graph and update every node distance 
        we can find the shorted path between every two node 
         
        .. 
        note that if there is not a path between the two  node
        the return will be infinity and the empty list  .                    
        
    """
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path_list = []

        if id1 == id2:
            path_list.append(id1)
            return 0, path_list

        graph_algo = copy.deepcopy(self.get_graph())

        if not graph_algo.get_all_v().__contains__(id1):
            return math.inf, []
        if not graph_algo.get_all_v().__contains__(id2):
            return math.inf, []

        node_list = graph_algo.get_all_v()  # dic of node

        curr: Node = graph_algo.get_all_v().get(id1)
        curr.set_weight(0)

        prev = node_list.copy()

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

                    w: float = graph_algo.all_out_edges_of_node(curr.id).get(i)  # weight of the the  d1-->i edge
                    temp_dist = curr.get_weight() + float(w)

                    if node_dest.get_tag() == 0:
                        pq.add(node_dest)
                        node_dest.set_tag(1)

                    if temp_dist <= node_dest.weight:
                        node_dest.set_weight(temp_dist)
                        prev[node_dest.id] = curr.id


            curr = pq.pop()   #  the minimum of current adjacency is now current



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

    for i in range(6):
        graph.add_node(i)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 0, 42)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 0, 7)
    graph.add_edge(2, 5, 1)
    graph.add_edge(3, 1, 11)
    graph.add_edge(3, 2, 1)
    graph.add_edge(3, 4, 3)
    graph.add_edge(4, 5, 1)
    graph.add_edge(5, 3, 5)

    print(graph_algo.shortest_path(10, 2))
