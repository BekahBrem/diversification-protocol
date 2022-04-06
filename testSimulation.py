import unittest
from main import Simulation
import networkx as nx
import os


class TestSimulation(unittest.TestCase):

    def test_simulation_creation(self):
        """
        Test that it creates a graph
        parameters: agents, colours, weightsDict, createDrawing
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = Simulation(test_agents, test_colours, test_weights_dict, test_create_drawing)

        #Assert a simulation is created with all the required params
        self.assertEqual(test_agents, testSimulation.numOfAgents)
        self.assertEqual(test_colours, testSimulation.numOfColours)
        self.assertEqual(test_weights_dict, testSimulation.weights)
        self.assertEqual(test_create_drawing, testSimulation.createDrawing)

    def test_total_weights(self):
        """
        Test that it adds the weights correctly
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = Simulation(test_agents, test_colours, test_weights_dict, test_create_drawing)
        #Check total of weights
        self.assertEqual(4, testSimulation.totalWeights)


    def test_simulation_graph(self):
        """
        Test that the simulation creates a correct graph
        parameters: agents, colours, weightsDict, createDrawing
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = Simulation(test_agents, test_colours, test_weights_dict, test_create_drawing)

        test_network = testSimulation.network

        self.assertEqual(test_agents, len(testSimulation.network.graph.nodes))
        self.assertTrue(len(testSimulation.network.graph.edges) > 1)


    def test_colour_agents_in_graph(self):
        """
        Test that the simulation creates at least one agent of each colour
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = Simulation(test_agents, test_colours, test_weights_dict, test_create_drawing)
        
        for colour in range(test_colours):
            self.assertTrue(testSimulation.findNumberInGraph(colour) >= 1)

    def test_get_shared_edges(self):
        """
        Test that the simulation creates at least one agent of each colour
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = Simulation(test_agents, test_colours, test_weights_dict, test_create_drawing)

        #Get the nodes that agent 0 shares edges with
        otherNodes = testSimulation.getSharedEdges(0)

        #Ensure it shares at least one edge - connected
        self.assertTrue(len(otherNodes) > 1)

    def test_get_observed_node(self):
        """
        Test that the simulation can find a connected node
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = Simulation(test_agents, test_colours, test_weights_dict, test_create_drawing)

        #Get the nodes that agent 0 shares edges with
        otherNodes = testSimulation.getSharedEdges(0)

        #Find observed node
        observedNode = testSimulation.getObservedNode(0, otherNodes)

        #Ensure it shares at least one edge - connected
        self.assertTrue((observedNode[1] in otherNodes) and (observedNode[1] != 0))

    def test_create_agents(self):
        """
        Test that the simulation can find a connected node
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = Simulation(test_agents, test_colours, test_weights_dict, test_create_drawing)

        agents = testSimulation.createAgentsTest()
        self.assertEqual(test_agents, len(agents))

    def test_simulation_get_agents(self):
        """
        Test that it creates a graph
        parameters: agents, colours, weightsDict, createDrawing
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = Simulation(test_agents, test_colours, test_weights_dict, test_create_drawing)

        #Assert a simulation is created with all the required params
        self.assertEqual(test_agents, testSimulation.getAgents())

    def test_simulation_get_agents(self):
        """
        Test that it creates a graph
        parameters: agents, colours, weightsDict, createDrawing
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testSimulation = Simulation(test_agents, test_colours, test_weights_dict, test_create_drawing)

        #Assert a simulation is created with all the required params
        self.assertEqual(test_agents, len(testSimulation.getAgents()))


if __name__ == '__main__':
    unittest.main()