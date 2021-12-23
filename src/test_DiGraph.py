from unittest import TestCase
from DiGraph import *


class TestDiGraph(TestCase):
    def test_v_size(self):
        graph_1: DiGraph = DiGraph()
        # when the graph just init number of nodes should be 0.
        self.assertEqual(0, graph_1.v_size())

        # adding 2 new nodes, number of nodes should be 2.
        graph_1.add_node(1, pos=(1, 2, 0))
        graph_1.add_node(2, pos=(4, 5, 0))
        self.assertEqual(2, graph_1.v_size())

        # adding new node with existing id in collection, number id should remain as before (2).
        graph_1.add_node(1, pos=(1, 3, 0))
        self.assertEqual(2, graph_1.v_size())

        # adding new node without pos, should increase the node size by one (total - 3).
        graph_1.add_node(3)
        self.assertEqual(3, graph_1.v_size())

        # init new graph, should not be affected by previous graph, size = 0.
        graph_2: DiGraph = DiGraph()
        self.assertEqual(0, graph_2.v_size())

        ## ------> FAILED FROM HERE!
        # try to remove one existing node, node size should be (2).
        graph_1.remove_node(1)
        self.assertEqual(2, graph_1.v_size())

        # try to remove the same node we removed before, should not effect updated size (2).
        graph_1.remove_node(1)
        self.assertEqual(2, graph_1.v_size())

        # try to remove a known non-existing node, should not effect node_size.
        graph_1.remove_node(99999)
        self.assertEqual(2, graph_1.v_size())

    def test_e_size(self):
        graph_1: DiGraph = DiGraph()
        # when the graph just init number of EDGES should be 0.
        self.assertEqual(0, graph_1.e_size())

        # adding 1 new edge with two different nodes_id, number of edges should be 1.
        graph_1.add_node(1, (0, 0, 0))
        graph_1.add_node(2, (0, 0, 0))
        graph_1.add_edge(1, 2, 0)
        self.assertEqual(1, graph_1.e_size())

        # try to connect node to himself, should not add this edge and to not increase edge_size.
        graph_1.add_edge(1, 1, 20)
        self.assertEqual(1, graph_1.e_size())

        # add 2 new nodes and connect between both directions and add 2 new edges (should be 3 total).
        graph_1.add_node(3, (0, 0, 0))
        graph_1.add_node(4, (0, 0, 0))
        graph_1.add_edge(3, 4, 10)
        graph_1.add_edge(4, 3, 10)
        self.assertEqual(3, graph_1.e_size())

        # try to connect existing edge, edge size should remain the same (3).
        graph_1.add_edge(3, 4, 10)
        self.assertEqual(3, graph_1.e_size())

        ## --------> FAILED FROM HERE!

        # try to remove valid edge from graph, edge size should be (2) [decreased by 1]
        # node size should not effected (4).
        graph_1.remove_edge(3, 4)
        self.assertEqual(2, graph_1.e_size())
        self.assertEqual(4, graph_1.v_size())

        # try to remove invalid edge (src == dest), should not effect edge_size (3)
        # and node size(4).
        graph_1.remove_edge(1, 1)
        self.assertEqual(3, graph_1.e_size())
        self.assertEqual(4, graph_1.v_size())

        # remove non existing edge, should not effect edge_size (3) and node size(4).
        graph_1.remove_edge(2, 1)
        self.assertEqual(3, graph_1.e_size())
        graph_1.remove_edge(100000, 999999)
        self.assertEqual(3, graph_1.e_size())
        self.assertEqual(4, graph_1.v_size())

    def test_get_all_v(self):
        self.fail()

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_all_out_edges_of_node(self):
        self.fail()

    def test_get_mc(self):
        graph_1: DiGraph = DiGraph()

        # adding 10 new nodes. expected mc+=10 (total 10)
        for i in range(10):
            graph_1.add_node(i, (0, 0, 0))

        self.assertEqual(10, graph_1.get_mc())

        # adding same nodes twice [0 - 4]
        graph_2: DiGraph = DiGraph()
        flag = True
        for i in range(10):
            if i == 5 and flag:
                flag = False
                i = 0
            graph_2.add_node(i, (0, 0, 0,))
        self.assertEqual(10, graph_2.get_mc())

        # removing all nodes from graph_2. expected -> mc+=10 (total 20)
        for i in range(10):
            graph_2.remove_node(i)

        self.assertEqual(20, graph_2.get_mc())

        # adding 10 valid edges to graph_1 (notice edge 1-1 should not count) . expected ->  mc+=9 (total 19)
        for i in range(10):
            graph_1.add_edge(1, i, 2)
        self.assertEqual(19, graph_1.get_mc())

        # adding 5 invalid edges to graph_1. expected -> mc+=0 (total 19)
        for i in range(90, 95):
            graph_1.add_edge(20, i, 2)
        self.assertEqual(19, graph_1.get_mc())

        # remove valid edge from graph_1. expected -> mc += 1 (total 20)
        graph_1.remove_edge(1, 2)
        self.assertEqual(20, graph_1.get_mc())

        # remove invalid edge from graph_1. expected -> mc+=0 (total 20)
        graph_1.remove_edge(99, 100)
        self.assertEqual(20, graph_1.get_mc())

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        graph_1: DiGraph = DiGraph()
        # adding one valid node. expected -> TRUE
        self.assertTrue(graph_1.add_node(1, (0, 0, 0)))

        # adding the same existing node. expected -> FALSE + print "node id already exists"
        self.assertFalse(graph_1.add_node(1, (0, 0, 0)))

        # adding new node with same pos as another. expected -> TRUE
        self.assertTrue(graph_1.add_node(2, (0, 0, 0)))

        # adding new node without declare pos. expected -> True
        self.assertTrue(graph_1.add_node(3))

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
