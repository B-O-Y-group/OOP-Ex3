from unittest import TestCase
from DiGraph import *
from GraphAlgo import *


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        graph: GraphInterface = DiGraph()
        """# INIT graph with nodes [5-9] and edges {5-6} {5-9} {9-5} {8-7} {7-8} {7-9}"""
        for i in range(5, 10):
            graph.add_node(i, (0, 0, 0))
        graph.add_edge(5, 6, 2)
        graph.add_edge(5, 9, 3)
        graph.add_edge(9, 5, 4)
        graph.add_edge(8, 7, 5)
        graph.add_edge(7, 8, 6)
        graph.add_edge(7, 9, 7)
        graph_algo: GraphAlgoInterface = GraphAlgo(graph)
        graph_temp: GraphInterface = graph_algo.get_graph()

        """# check if all databases are the same. (by values). expected -> TRUE"""

        print("get_graph -> test 1")
        """# e_size method"""
        self.assertEqual(graph_temp.e_size(), graph.e_size())
        print("Passed!")

        print("get_graph -> test 2")
        """# v_size method"""
        self.assertEqual(graph_temp.v_size(), graph.v_size())
        print("Passed!")

        print("get_graph -> test 3")
        """# get_all_v method"""
        self.assertEqual(graph_temp.get_all_v(), graph.get_all_v())
        print("Passed!")

        print("get_graph -> test 4")
        """# all_out_edges_of_node method. node_checked (5)"""
        self.assertEqual(graph_temp.all_out_edges_of_node(5), graph.all_out_edges_of_node(5))
        print("Passed!")

        print("get_graph -> test 5")
        """# all_in_edges_of_node method. node_checked (9)"""
        self.assertEqual(graph_temp.all_out_edges_of_node(9), graph.all_out_edges_of_node(9))
        print("Passed!")

        """# try to remove node from original graph and check differences with temp_graph. should effect both graphs."""
        graph.remove_node(5)
        print("get_graph -> test 6")
        """# v_size method"""
        self.assertEqual(graph_temp.v_size(), graph.v_size())
        print("Passed!")

        print("get_graph -> test 7")
        """# e_size method"""
        self.assertEqual(graph_temp.e_size(), graph.e_size())
        print("Passed All!")

    def test_load_from_json(self):
        graph: GraphInterface = DiGraph()
        graph_algo: GraphAlgoInterface = GraphAlgo(graph)
        graph_algo.load_from_json("data/A0.json")

        print("load_from_json -> test 1")
        """# try to add to the init graph 2 nodes that exist in json file. expected -> FALSE"""
        self.assertFalse(graph.add_node(0))
        self.assertFalse(graph.add_node(1))

        print("load_from_json -> test 2")
        """# try to add edge that exist in json file. expected -> FALSE"""
        self.assertFalse(graph.add_edge(0, 1, 0))

        print("load_from_json -> test 3")
        """# try to remove edge from graph that exist in json file. expected -> TRUE"""
        self.assertTrue(graph.remove_edge(0, 1))

        print("load_from_json -> test 4")
        """# try to remove node that exist in json file. expected -> TRUE"""
        self.assertTrue(graph.remove_node(9))

        print("load_from_json -> test 5")
        """# try to remove node that do not exist in json file. expected -> FALSE"""
        self.assertFalse(graph.remove_node(99))

        """# manual INIT new graph that is identical to "T0.json" file"""
        graph_t: GraphInterface = DiGraph()
        graph_t_algo: GraphAlgoInterface = GraphAlgo(graph_t)
        graph_t_algo.load_from_json("data/T0.json")

        man_graph: GraphInterface = DiGraph()
        for i in range(4):
            man_graph.add_node(i)
        man_graph.add_edge(0, 1, 1)
        man_graph.add_edge(1, 0, 1.1)
        man_graph.add_edge(1, 2, 1.3)
        man_graph.add_edge(1, 3, 1.8)
        man_graph.add_edge(2, 3, 1.1)

        """# compare all databases between the two graphs. expected -> TRUE on each"""

        print("load_from_json -> test 6")
        """# e_size method"""
        self.assertEqual(man_graph.e_size(), graph_t.e_size())
        print("Passed!")

        print("load_from_json -> test 7")
        """# v_size method"""
        self.assertEqual(man_graph.v_size(), graph_t.v_size())
        print("Passed!")

        print("load_from_json -> test 8")
        """# get_all_v method"""
        self.assertEqual(man_graph.get_all_v(), graph_t.get_all_v())
        print("Passed!")

        print("load_from_json -> test 9")
        """# all_out_edges_of_node method. node_checked (5)"""
        self.assertEqual(man_graph.all_out_edges_of_node(1), graph_t.all_out_edges_of_node(1))
        print("Passed!")

        print("load_from_json -> test 10")
        """# all_in_edges_of_node method. node_checked (9)"""
        self.assertEqual(man_graph.all_out_edges_of_node(3), graph_t.all_out_edges_of_node(3))
        print("Passed!")

        """# load_json to already initialized graph. expected -> clear the existed graph and make new one as json"""
        new_graph: GraphInterface = DiGraph()
        """# INIT graph with nodes [5-9] and edges {5-6} {5-9} {9-5} {8-7} {7-8} {7-9}"""
        for i in range(5, 10):
            new_graph.add_node(i, (0, 0, 0))
        new_graph.add_edge(5, 6, 2)
        new_graph.add_edge(5, 9, 3)
        new_graph.add_edge(9, 5, 4)
        new_graph.add_edge(8, 7, 5)
        new_graph.add_edge(7, 8, 6)
        new_graph.add_edge(7, 9, 7)
        new_graph_algo: GraphAlgoInterface = GraphAlgo(new_graph)
        new_graph_algo.load_from_json("data/T0.json")

        """# try to remove node_id 5. the graph that described in T0.json does not have node_id 5 like the previous 
        graph. expected -> FALSE """

        print("load_from_json -> test 11")
        self.assertFalse(new_graph.remove_node(5))
        print("Passed All!")


    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_center_point(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()