import matplotlib.pyplot as plt
import random

class randomWalker():
    
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
        
try:
    wallStreet = randomWalker(0,0)
    wallStreet.RandomWalkPlot(0)

except ValueError as msg:
    print(msg)

    
    
    