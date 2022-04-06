#Using pythonwx to create the UI
import wx

#Frame of the inout, holds all out input fields, labels & buttons
class MyFrame(wx.Frame):

    def __init__(self):
        self.agents = 0
        self.colours = 0
        self.weights = ''
        self.weightsDict = {}

        super().__init__(parent=None, title='Population Protocol: User Input', size = (700, 350))
        panel = wx.Panel(self)

        #will use vbox and hbox to automatically layout the fields & labels
        #REFERENCE - I used the following tutorial to implement the layout: https://zetcode.com/wxpython/layout/
        vbox = wx.BoxSizer(wx.VERTICAL)

        #get number of agents the user wants
        self.labelAgents = wx.StaticText(panel, label="Number of agents")
        self.number_of_agents = wx.TextCtrl(panel, pos=(5, 50))

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.labelAgents, flag=wx.RIGHT, border=8)
        hbox1.Add(self.number_of_agents)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))

        #get number of colors the user wants
        self.labelColours = wx.StaticText(panel, label="Number of Colours")
        self.number_of_colours = wx.TextCtrl(panel)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.labelColours, flag=wx.RIGHT, border=8)
        hbox2.Add(self.number_of_colours)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
        vbox.Add((-1, 10))

        #get weights of colors the user wants
        self.labelWeights = wx.StaticText(panel, label="Weights of Colours")

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.labelWeights, flag=wx.RIGHT, border=8)
        vbox.Add(hbox3, flag=wx.LEFT | wx.TOP, border=10)

        #Weights instruction
        self.instruction = wx.StaticText(panel, label="Please enter as a list of weights seperated with commas (e.g. for 3 colours you could input: 3,4,5)")
        font = wx.Font(11, wx.DEFAULT, wx.ITALIC, wx.NORMAL)
        self.instruction.SetFont(font)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.instruction)
        vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)

        #Space for user to input desired weights
        self.weight_of_colours = wx.TextCtrl(panel)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5.Add(self.weight_of_colours)
        vbox.Add(hbox5, flag=wx.LEFT | wx.TOP, border=10)

        #Run simulation button
        my_btn = wx.Button(panel, label='Start Simulation')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6.Add(my_btn, flag=wx.RIGHT, border=8)
        vbox.Add(hbox6, flag=wx.LEFT | wx.TOP, border=10)

        panel.SetSizer(vbox)

        self.Show()

    #When we press on the Start Simulation button
    def on_press(self, event):
        try:
            #Keep these as ints
            value_agents = int(self.number_of_agents.GetValue())
            value_colours = int(self.number_of_colours.GetValue())
            self.agents = value_agents
            self.colours = value_colours

            #Weigth input isn't in the format we want, so convert it
            value_weights = self.weight_of_colours.GetValue()
            self.convertWeightsToDictionary(value_weights)

            #Make sure we have values for all
            if not value_agents or not value_colours or not value_weights:
                print("Tip: you're missing a field")
            else:
                self.Destroy()
        except:
            print('Make sure you input everything in the correct format (all ints, not strings!) & no fields are empty!')

    def convertWeightsToDictionary(self, weightsString):
        #The expected input of our weights is a string such as: '3,4,5' so we need to seperate this for our Colours
        weightsList = weightsString.split(",")
        print(weightsList)
        if len(weightsList) != self.colours:
            print("Make sure you have the same number of weights as the number of colours.")
        else:
            for colour in range(self.colours):
                self.weightsDict[colour] = int(weightsList[colour])


class UserInput():
    def onCall(self):
        app = wx.App()
        frame = MyFrame()
        app.MainLoop()
        #print("frame agents: ", frame.agents)
        return(frame.agents, frame.colours, frame.weightsDict)