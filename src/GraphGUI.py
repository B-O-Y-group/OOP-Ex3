import pygame
import os
from GraphAlgo import *
from DiGraph import *
from pygame.constants import RESIZABLE
import math

screen = pygame.display.set_mode((700, 500), flags=RESIZABLE)  # check!

"""------------------> START SCALE METHODS"""


def scale(data, min_screen, max_screen, min_data, max_data):
    """
    get the scaled data with proportions min_data, max_data
    relative to min and max screen dimensions
    """
    return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


min_x = min_y = max_x = max_y = 0


def min_max(graph: GraphInterface = None):
    global min_x, min_y, max_x, max_y
    min_x = min(list(graph.get_all_v().values()), key=lambda n: n.pos[0]).pos[0]
    min_y = min(list(graph.get_all_v().values()), key=lambda n: n.pos[1]).pos[1]
    max_x = max(list(graph.get_all_v().values()), key=lambda n: n.pos[0]).pos[0]
    max_y = max(list(graph.get_all_v().values()), key=lambda n: n.pos[1]).pos[1]


def my_scale(data, x=False, y=False):
    if x:
        return scale(data, 50, screen.get_width() - 50, min_x, max_x)
    if y:
        return scale(data, 50, screen.get_height() - 50, min_y, max_y)


"""------------------> END SCALE METHODS"""


def draw(graph: GraphInterface):
    for src in graph.get_all_v().values():
        node: Node = src
        x = my_scale(data=node.pos[0], x=True)
        y = my_scale(data=node.pos[1], y=True)
        node_center = (int(node.pos[0]), int(node.pos[1]))
        # print(node)
        pygame.draw.circle(screen, color=(253, 225, 70), center=(x, y), radius=10)
        for dest in graph.all_out_edges_of_node(node.id):
            dest: Node = graph.get_all_v()[dest]
            dest_x = my_scale(data=dest.pos[0], x=True)
            dest_y = my_scale(data=dest.pos[1], y=True)
            pygame.draw.line(screen, (255, 255, 255), start_pos=(x, y), end_pos=(dest_x, dest_y), width=5)


def display(algo: GraphAlgoInterface):
    min_max(algo.get_graph())

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        screen.fill((216, 158, 154))
        draw(algo.get_graph())
        pygame.display.update()


if __name__ == '__main__':
    # graph: GraphInterface = DiGraph()
    # graph_algo: GraphAlgoInterface = GraphAlgo(graph)
    # graph_algo.load_from_json("../data/A0.json")
    graph: GraphInterface = DiGraph()
    graph_algo: GraphAlgoInterface = GraphAlgo(graph)

    graph.add_node(0, (35.18753053591606, 32.10378225882353, 0.0))
    graph.add_node(1, (35.18958953510896, 32.10785303529412, 0.0))
    graph.add_node(2, (35.19341035835351, 32.10610841680672, 0.0))
    graph.add_node(3, (35.197528356739305, 32.1053088, 0.0))
    graph.add_node(4, (35.2016888087167, 32.10601755126051, 0.0))
    graph.add_node(5, (35.20582803389831, 32.10625380168067, 0.0))

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
    print(graph_algo.get_graph())
    display(graph_algo)