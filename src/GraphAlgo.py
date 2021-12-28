import copy
import math
import random
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
    """
    get_graph:
        This method return the current graph 
    """

    def get_graph(self) -> GraphInterface:
        return self.graph

    """
    load_from_json:
            initialize the graph from a json file 
    """

    def load_from_json(self, file_name: str) -> bool:
        try:

            with open(file_name, "r") as f:
                dic = {}
                g = DiGraph()
                dic = json.load(fp=f)

            for n in dic["Nodes"]:
                if len(n.keys()) == 1:
                    # x = None
                    # y = None
                    # pos = (x, y, 0)
                    g.add_node(node_id=n["id"], pos=None)

                else:
                    p = n["pos"].split(",")
                    pos = (p[0], p[1], p[2])
                    g.add_node(node_id=n["id"], pos=pos)

            for e in dic["Edges"]:
                g.add_edge(id1=e["src"], id2=e["dest"], weight=e["w"])

            self.graph = g
            return True
        except Exception:
            print(Exception.args)
            return False

    """
    save_to_json:
        This method get a graph and save it in a json file
    """

    def save_to_json(self, file_name: str) -> bool:
        node = []
        edge = []
        for i in self.graph.get_all_v():
            curr: Node = self.graph.get_all_v().get(i)
            pos = str(curr.pos[0]) + "," + str(curr.pos[1]) + "," + str(curr.pos[2])
            n = {"id": curr.id, "pos": pos}
            node.append(n)
            for j in self.graph.all_out_edges_of_node(curr.id):
                dest: Node = self.graph.get_all_v().get(j)
                e = {"src": curr.id, "w": self.graph.all_out_edges_of_node(curr.id).get(j), "dest": dest.id}
                edge.append(e)

        dic = {"Edges": edge, "Nodes": node}

        try:
            with open(file_name, "w") as f:
                ## indenter is number rof space
                json.dump(dic, fp=f, indent=4, default=lambda o: o.__dict__)
                return True
        except Exception:
            print(Exception.args)
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

            if graph_algo.all_out_edges_of_node(curr.id) is None:
                return math.inf, path_list

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

            curr = pq.pop()  # the minimum of current adjacency is now current

        path_list.append(id2)
        id = prev[id2]

        while id is not None:
            path_list.append(id)
            id = prev[id]
        path_list.reverse()
        ans: Node = graph_algo.get_all_v().get(id2)
        return ans.weight, path_list

    """ 
    centerPoint :
        this algorithm using dijkstra(all_path) and search for each node the maximum weight from him to all the other  
        and then search for the minimum of all the max weight of each 
        @return: id of Node  with the minimum from the maximum group of weight ,and value (weight)
    """

    def centerPoint(self) -> (int, float):
        graph_algo = copy.deepcopy(self.get_graph())

        final_center = math.inf
        center = None

        for i in graph_algo.get_all_v():
            curr: Node = graph_algo.get_all_v().get(i)
            dist = []

            self.intDist(dist)

            self.all_path(curr.id, dist)
            print(dist)
            max_of_the_list = max(dist)

            if max_of_the_list < final_center:
                center = curr.id
                final_center = max_of_the_list

        return center, final_center

    def all_path(self, id: int, dist: []) -> list:

        graph_algo = copy.deepcopy(self.get_graph())
        curr: Node = graph_algo.get_all_v().get(id)
        curr.set_weight(0)

        pq = PriorityQueue()
        pq.add(curr)

        while not pq.isEmpty():
            curr = pq.pop()
            curr.set_tag(2)

            # if graph_algo.all_out_edges_of_node(curr.id) is None:
            #     continue

            for i in graph_algo.all_out_edges_of_node(curr.id):

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
                        dist[node_dest.id] = node_dest.weight

        return dist

    def intDist(self, dist: []):
        for j in self.get_graph().get_all_v():
            dist.insert(j, 0)


################################################################
# is connected


def plot_graph(self) -> None:
    pass


if __name__ == '__main__':
    graph: GraphInterface = DiGraph()
    pos = (0, 0, 0)
    graph.add_node(0, pos)
    graph.add_node(1, pos)
    graph.add_node(2, pos)
    graph.add_node(3, pos)
    graph.add_node(4, pos)
    graph.add_node(5, pos)

    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 5, 2)

    graph.add_edge(1, 2, 3)

    graph.add_edge(2, 3, 1)
    graph.add_edge(2, 4, 4)

    graph.add_edge(3, 0, 1)

    graph.add_edge(4, 3, 3)
    graph.add_edge(4, 1, 6)

    graph.add_edge(5, 4, 4)

    graph_algo: GraphAlgoInterface = GraphAlgo(graph)
    graph_algo.load_from_json("../data/A1.json")
    graph_algo.save_to_json("../data/T1.json")

# print(graph.)
