import unittest
from graph import Graph
import networkx as nx
import os


class TestGraph(unittest.TestCase):

    def test_graph_Creation(self):
        """
        Test that it creates a graph
        parameters: (self, agents, numColours, createDrawing)
        """
        #Create 3 agents
        data = [(0, {"colour": 0, "shade": 1}), (1, {"colour": 1, "shade": 1}), (2, {"colour": 0, "shade": 1})]

        #Create graphwith data
        testGraph = Graph("connected", data, 2, True)
        nodes = len(testGraph.graph.nodes)

        #Assert a graph is create with exactly 3 nodes
        self.assertEqual(nodes, 3)

    def test_edges_connected(self):
        """
        Test that it creates a graph with edges
        """
        #Create 3 agents
        data = [(0, {"colour": 0, "shade": 1}), (1, {"colour": 1, "shade": 1}), (2, {"colour": 0, "shade": 1}), (3, {"colour": 0, "shade": 1})]
        #Create graph with data
        testGraph = Graph("connected", data, 2, True)
        edges = len(testGraph.graph.edges)

        #Assert a graph is create with exactly 3 nodes
        self.assertTrue(edges == 6)

    def test_edges_cycle(self):
        """
        Test that it creates a graph with edges
        """
        #Create 3 agents
        data = [(0, {"colour": 0, "shade": 1}), (1, {"colour": 1, "shade": 1}), (2, {"colour": 0, "shade": 1})]
        #Create graph with data
        testGraph = Graph("cycle", data, 2, True)
        edges = len(testGraph.graph.edges)

        #Assert a graph is create with exactly 3 nodes
        self.assertTrue(edges == 3)

    def test_edges_line(self):
        """
        Test that it creates a graph with edges
        """
        #Create 3 agents
        data = [(0, {"colour": 0, "shade": 1}), (1, {"colour": 1, "shade": 1}), (2, {"colour": 0, "shade": 1})]
        #Create graph with data
        testGraph = Graph("line", data, 2, True)
        edges = len(testGraph.graph.edges)

        #Assert a graph is create with exactly 3 nodes
        self.assertTrue(edges == 2)

    def test_draw_graph(self):
        """
        Test that it creates a graph with edges
        """
        #Create 3 agents
        data = [(0, {"colour": 0, "shade": 1}), (1, {"colour": 1, "shade": 1}), (2, {"colour": 0, "shade": 1})]
        #Create graph with data
        testGraph = Graph("connected", data, 2, True)

        #Check to see that a graph was generated
        self.assertTrue(os.path.isfile('graph.png'))


if __name__ == '__main__':
    unittest.main()