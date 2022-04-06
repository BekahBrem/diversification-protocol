import unittest
from experiment import Experiment
import networkx as nx
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *


class TestExperiment(unittest.TestCase):

    #Create root window
    global test_window 
    test_window = tk.Tk()

    def test_simulation_creation(self):
        """
        Test that it creates an experiment correctly
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testExperiment = Experiment(test_window, "connected", test_agents, test_colours, test_weights_dict)

        #Assert a simulation is created with all the required params
        self.assertEqual(test_agents, testExperiment.numOfAgents)
        self.assertEqual(test_colours, testExperiment.numOfColours)
        self.assertEqual(test_weights_dict, testExperiment.weights)

        self.assertEqual(0, testExperiment.stepNum)

    def test_window_creation(self):
        """
        Test that it creates a window
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testExperiment = Experiment(test_window, "connected", test_agents, test_colours, test_weights_dict)

        #Assert window is created 
        self.assertIsInstance(testExperiment.output, Toplevel)

    def test_get_total_weight(self):
        """
        Test that it calculates total weight correctly
        """
        #Create input
        test_agents = 5
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 2}
        test_create_drawing = False
        
        #Create graph with data
        testExperiment = Experiment(test_window, "connected", test_agents, test_colours, test_weights_dict)

        #Assert total weight calculated correctly
        self.assertEqual(4, testExperiment.getTotalWeight())

    def test_get_proportional_weight(self):
        """
        Test that it calculates proportional weight correctly
        """
        #Create input
        test_agents = 3
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 1}
        test_create_drawing = False
        
        #Create graph with data
        testExperiment = Experiment(test_window, "connected", test_agents, test_colours, test_weights_dict)

        propWeight = testExperiment.getProportionWeight(0)
        #Assert total weight calculated correctly
        self.assertEqual(33.33, propWeight)

    def test_calculate_colour_representation(self):
        """
        Test that it calculates colour representation correctly
        """
        #Create input
        test_agents = 3
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 1}
        test_create_drawing = False
        
        #Create graph with data
        testExperiment = Experiment(test_window, "connected", test_agents, test_colours, test_weights_dict)

        colourRep = testExperiment.calculateColourRepresentation(0)
        #Assert total weight calculated correctly
        self.assertEqual(1, colourRep)

    def test_calculate_colour_expected_nodes(self):
        """
        Test that it calculates colour representation correctly
        """
        #Create input
        test_agents = 6
        test_colours = 3
        test_weights_dict = {0: 1, 1: 1, 2: 1}
        test_create_drawing = False
        
        #Create graph with data
        testExperiment = Experiment(test_window, "connected", test_agents, test_colours, test_weights_dict)

        expectedNodes = testExperiment.calculateExpectedNodes(0)
        #Assert total weight calculated correctly
        self.assertEqual(2, expectedNodes)

    def test_perform_steps(self):
        """
        Test that it calculates colour representation correctly
        """
        #Create input
        test_agents = 10
        test_colours = 2
        test_weights_dict = {0: 9, 1: 1}
        test_create_drawing = False
        
        #Create graph with data
        testExperiment = Experiment(test_window, "connected", test_agents, test_colours, test_weights_dict)

        testExperiment.x_values = []
        testExperiment.y_values = {}

        testExperiment.doSteps(40)

        #Assert total weight calculated correctly
        self.assertEqual(len(testExperiment.y_values[0]), len(testExperiment.x_values))

    def test_calculate_accuracy(self):
        """
        Test that it calculates colour representation correctly
        """
        #Create input
        test_agents = 10
        test_colours = 2
        test_weights_dict = {0: 1, 1: 1}
        test_create_drawing = False
        
        #Create graph with data
        testExperiment = Experiment(test_window, "connected", test_agents, test_colours, test_weights_dict)

        test_experimentsList = [{0: 5, 1: 5}]
        test_accuracy = testExperiment.calculateAccuracy(test_experimentsList)

        self.assertEqual(98, test_accuracy)

    def test_draw_graph(self):
        """
        Test that it creates a graph with edges
        """
        #Create input
        test_agents = 10
        test_colours = 2
        test_weights_dict = {0: 1, 1: 1}
        test_create_drawing = False
        
        #Create graph with data
        testExperiment = Experiment(test_window, "connected", test_agents, test_colours, test_weights_dict)

        #Check to see that a graph was generated
        self.assertTrue(os.path.isfile('experimentGraph.png'))

 
if __name__ == '__main__':
    unittest.main()