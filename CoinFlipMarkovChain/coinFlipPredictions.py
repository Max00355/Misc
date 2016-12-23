import random
class Prediction:
    def __init__(self, state):
        self.state = 0
        self.timeOnState = 0 # i
        self.odds = 0.5
        self.weight = 0.05 
        self.variable_weight = 0 # w
        self.convert = {
            0:"Heads",
            1:"Tails"
        }   
    def generatePredictions(self, n):
        longestTimeOnState = 0
        for x in range(n):
            number = float(random.randint(0, 100)) / 100
            if number < self.odds + self.variable_weight:
                longestTimeOnState = max(longestTimeOnState, self.timeOnState)
                self.timeOnState = 0
                self.variable_weight = 0
                if self.state == 0:
                    self.state = 1
                else:
                    self.state = 0
                print self.convert[self.state]
            else:
                self.timeOnState += 1
                self.variable_weight += self.timeOnState * self.weight
        print longestTimeOnState
Prediction(1).generatePredictions(1000000)
