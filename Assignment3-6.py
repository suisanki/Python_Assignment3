import matplotlib.pyplot as plt
import random

class Dice():
    def __init__(self):
        self.list = []
    
    def plot(self,num):
        if type(num) != int:
            raise ValueError("Input not valid")
        
        for i in range(num):
            self.list.append(random.randint(1,6))
            
        plt.figure(figsize=(8,6), dpi = 200)
        plt.hist(self.list, bins=6, color='green', edgecolor='black')
        
        plt.xlabel("Appearing Dots")
        plt.ylabel("Frequency")
        plt.title("Diceroll Simulation")

gambler = Dice()

gambler.plot("hello")