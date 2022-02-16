import random

class Agent:
    #Initialise agent with the starting variables
    def __init__(self, colour, shade, id):
        """Variables the agent stores"""
        #The colour of the node
        self.colour = colour
        #The shade aka confidence the node has in its current colour
        self.shade = shade
        self.id = id

    #Method for sampling another agent
    def sampleAgent(self):
        return

    #Returns the current shade
    def getShade(self, newShade):
        return self.shade

    #Returns the current colour
    def getColour(self, newColour):
        return self.colour

    #Sets the shade to the shade passed in as a parameter
    def changeShade(self, newShade):
        self.shade = newShade

    #Sets the colour to the shade passed in as a parameter
    def changeColour(self, newColour):
        self.colour = newColour

    #Method for determining if we change shade / colour
    def determineAction(self, otherAgent):
        """
        Simple notation I'm using to explain what's happening:
            Cu(t) => colour of u at time-step t (so following from this: Cv(t) is the colour of v at time t)
            Su(t) => shade of u at time-step t (so following from this: Sv(t) is the shade of v at time t)
            w_i is simply the weight of colour i

        The Diversification Protocol works in teh following way for a node u that observes node v:
            (1)     (Cu(t+1), Su(t+1)) = (Cv(t), 1)         if Sv(t) = 1 and Su(t) = 0
            (2)     (Cu(t+1), Su(t+1)) = (Cu(t), 0)         w/ prob: 1/w_i) if Sv(t) = Su(t) = 1 and Cu(t) = Cv(t)
            (3)     (Cu(t+1), Su(t+1)) = (Cu(t), Su(t))     if not the 2 conditions, remain as was in last time-step
        """
        #(1) & (2)
        if (otherAgent.colour == self.colour):
            #(2)
            if ((otherAgent.shade == self.shade) and (self.shade == 1)):
                #Change to light w/ probability 1/(weight of the colour)
                if random.random() < (1/2):
                    self.shade = 0
            #(1)
            elif ((otherAgent.shade == 1) and (self.shade == 0)):
                #remain same colour, effectively: self.colour = otherAgent.colour
                self.shade = 1
        else:
            #(1)
            if ((otherAgent.shade != self.shade) and (self.shade == 0)):
                self.colour = otherAgent.colour
                self.shade = otherAgent.shade
            #(3) Otherwise, the agent remains unchanged from the previous time-step
