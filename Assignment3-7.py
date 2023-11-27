import matplotlib.pyplot as plt
import random

class RandomWalker():
    
    def __init__(self,x,y):
        self.start_x = x
        self.start_y = y
        self.XP = [x]
        self.YP = [y]
        
    def RandomWalkPlot(self,steps):
        for i in range(steps):
            self.start_x = self.start_x + random.randint(-1,1)
            self.start_y = self.start_y + random.randint(-1,1)
            
            self.XP.append(self.start_x)
            self.YP.append(self.start_y)

        plt.figure(figsize=(8,6), dpi = 200)
        plt.scatter(self.XP, self.YP, color='black', s=0.1, marker='o')

if __name__ == "__main__":

    while True:
        try:
            x = input("Enter starting x coordination: ")
            y = input("Enter starting y coordination: ")
            try:
                x,y = float(x),float(y)
                
            except ValueError:
                print("Enter integer or float.")
                continue
            
            steps = input("Enter number of steps (positive integer): ")
            
            if steps.isnumeric():
                steps = int(steps)
            else:
                raise ValueError("Step should be positive integer")
            
            wallStreet = RandomWalker(x,y)
            wallStreet.RandomWalkPlot(steps)
            print("Plotted.")
            break

        except ValueError as msg:
            print(msg)
    
    
    