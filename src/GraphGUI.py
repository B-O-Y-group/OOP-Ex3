import pygame
import os
from GraphAlgo import *
from DiGraph import *
from pygame.constants import RESIZABLE
import math

screen = pygame.display.set_mode((700, 500), flags=RESIZABLE)  # check!


def draw(graph: DiGraph = None):
    for src in graph.get_all_v().values():
        node: Node = src
        print(node)
        pygame.draw.circle(screen, color=(253, 225, 70), center=(node.pos.__getitem__(0), node.pos.__getitem__(1)), radius=10)


def display(algo: GraphAlgoInterface = None):
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        screen.fill((216, 158, 154))
        draw(algo.get_graph())
        pygame.display.update()


if __name__ == '__main__':
    graph: GraphInterface = DiGraph()
    graph_algo: GraphAlgoInterface = GraphAlgo(graph)
    graph_algo.load_from_json("../data/A0.json")
    display(graph_algo)
