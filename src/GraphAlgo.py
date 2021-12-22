from abc import ABC

from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import json


class GraphAlgo(GraphAlgoInterface, ABC):

    def __init__(self, graph: GraphInterface):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        # super().get_graph()
        return self.graph

    # add_edge(self, id1: int, id2: int, weight: float)
    ##    add_node(self, node_id: int, pos: tuple = None)

    def load_from_json(self, file_name: str) -> bool:
        dic = {}

        with open(file_name, "r") as f:
            dic = json.load(fp=f)
        for n in dic["Nodes"].values():
            ##p = n["pos"].values()
            ## pos = tuple(map(float, pos.split(",")))
            self.graph.add_node(node_id=n["id"], pos=n["pos"])

        for e in dic["Edges"].values():
            self.graph.add_edge(id1=["src"], id2=["dest"], weight=["w"])
        return True

    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, "w") as f:
            ## indenter is number rof space
            ## default= lambda  o :o.__dict__ taking the self and change him to dictionaries
            json.dump(self, filePointer=f, indent=4, default=lambda o: o.__dict__)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':

