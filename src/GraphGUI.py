import pygame
import os
from GraphAlgo import *
from DiGraph import *
from pygame.constants import RESIZABLE
import math

pygame.font.init()
FONT = pygame.font.SysFont("Ariel", 22)

screen = pygame.display.set_mode((700, 500), flags=RESIZABLE)  # check!


class Button:
    def __init__(self, rect: pygame.Rect, color, text, func=None):
        self.rect = rect
        self.color = color
        self.text = text
        self.func = func
        self.is_clicked = False

    def press(self):
        self.is_clicked = not self.is_clicked


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


"""------------------> END SCALE METHODS <------------------"""

"""------------------> START Draw Methods <-----------------"""


def arrow(start, end, d, h, color):
    dx = float(end[0] - start[0])
    dy = float(end[1] - start[1])
    D = float(math.sqrt(dx * dx + dy * dy))
    xm = float(D - d)
    xn = float(xm)
    ym = float(h)
    yn = -h
    sin = dy / D
    cos = dx / D
    x = xm * cos - ym * sin + start[0]
    ym = xm * sin + ym * cos + start[1]
    xm = x
    x = xn * cos - yn * sin + start[0]
    yn = xn * sin + yn * cos + start[1]
    xn = x
    points = [(end[0], end[1]), (int(xm), int(ym)), (int(xn), int(yn))]

    pygame.draw.line(screen, color, start, end, width=4)
    pygame.draw.polygon(screen, color, points)


algo_results = []


def on_clicked(button: Button):
    global algo_results
    center = button.func()
    algo_results = center[0]

def draw(graph: GraphInterface):
    pygame.draw.rect(screen, button.color, button.rect)
    for src in graph.get_all_v().values():
        node: Node = src
        x = my_scale(data=node.pos[0], x=True)
        y = my_scale(data=node.pos[1], y=True)
        src_text = FONT.render(str(node.id), True, (0, 0, 0))
        node_center = (int(node.pos[0]), int(node.pos[1]))
        # print(node)
        node_radius = 10
        pygame.draw.circle(screen, color=(250, 204, 58, 255), center=(x, y), radius=node_radius)
        screen.blit(src_text, (x - (node_radius / 2), y - (node_radius / 2)))
        for dest in graph.all_out_edges_of_node(node.id):
            dest: Node = graph.get_all_v()[dest]
            dest_x = my_scale(data=dest.pos[0], x=True)
            dest_y = my_scale(data=dest.pos[1], y=True)
            arrow((x, y), (dest_x, dest_y), 17, 7, color=(255, 255, 255))
            # if(node.id, dest.id) in algo_results:
            #     arrow((x, y), (dest_x, dest_y), 17, 7, color=(0, 0, 255))
            # else:
            #     arrow((x, y), (dest_x, dest_y), 17, 7, color=(255, 255, 255))


"""------------------> END Draw Methods <-----------------"""


def display(algo: GraphAlgoInterface):
    button.func = algo.centerPoint
    min_max(algo.get_graph())
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(e.pos):
                    on_clicked(button)
        screen.fill((155, 117, 117, 255))
        draw(algo.get_graph())
        pygame.display.update()


button = Button(pygame.Rect((0, 0), (100, 40)), (200, 200, 0), "Algo")
if __name__ == '__main__':
    graph: GraphInterface = DiGraph()
    graph: GraphInterface = DiGraph()
    graph_algo: GraphAlgoInterface = GraphAlgo(graph)
    graph_algo.load_from_json("../data/A0.json")

    # graph: GraphInterface = DiGraph()
    # graph_algo: GraphAlgoInterface = GraphAlgo(graph)
    #
    # graph.add_node(0, (35.18753053591606, 32.10378225882353, 0.0))
    # graph.add_node(1, (35.18958953510896, 32.10785303529412, 0.0))
    # graph.add_node(2, (35.19341035835351, 32.10610841680672, 0.0))
    # graph.add_node(3, (35.197528356739305, 32.1053088, 0.0))
    # graph.add_node(4, (35.2016888087167, 32.10601755126051, 0.0))
    # graph.add_node(5, (35.20582803389831, 32.10625380168067, 0.0))
    #
    # graph.add_edge(0, 2, 5)
    # graph.add_edge(1, 0, 42)
    # graph.add_edge(1, 3, 5)
    # graph.add_edge(2, 0, 7)
    # graph.add_edge(2, 5, 1)
    # graph.add_edge(3, 1, 11)
    # graph.add_edge(3, 2, 1)
    # graph.add_edge(3, 4, 3)
    # graph.add_edge(4, 5, 1)
    # graph.add_edge(5, 3, 5)
    # print(graph_algo.get_graph())
    display(graph_algo)
