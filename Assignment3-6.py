import matplotlib.pyplot as plt
import random

class Dice():
    def __init__(self):
        self.list = []
    
    def plot(self,trials):
        if type(trials) != int:
            raise ValueError("Input not valid")
        
        for i in range(trials):
            self.list.append(random.randint(1,6))
            
        plt.figure(figsize=(8,6), dpi = 200)
        plt.hist(self.list, bins=6, color='green', edgecolor='black')
        
        plt.xlabel("Appearing Dots")
        plt.ylabel("Frequency")
        plt.title("Diceroll Simulation")

if __name__ == "__main__":
    while True:
        try:
            trials = input("Enter number of trials (positive integer): ")
            
            if trials.isnumeric():
                trials = int(trials)
            else:
                raise ValueError("Number of trials should be positive integer\n")
            
            gambler = Dice()
            gambler.plot(trials)
            print("Plotted.")
            break

        except ValueError as msg:
            print(msg)
