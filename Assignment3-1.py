import random
import math

class ScientificCalculator():
    def __init__(self, initialValue):
        #Value of the calculator 
        self.value = initialValue
        #Memorized value
        self.memory = 0
    
    def add(self,operand):
        self.value += operand
        
    def subtract(self,operand):
        self.value -= operand
        
    def multiply(self,operand):
        self.value *= operand
        
    def devide(self,operand):
        self.value /= operand
        
    def power(self, operand):
        self.value **= operand
        
    def root(self):
        self.value = math.sqrt(self.value)
        
    def rand(self):
        self.value = random.random()
    
    def memoryStore(self):
        self.memory = self.value
    
    def memoryAdd(self):
        self.memory = self.memory + self.value
        self.value = 0
        
    def memorySubtract(self):
        self.memory = self.memory - self.value
        self.value = 0
        
    def memoryClear(self):
        self.memory = 0
        
    def memoryRecall(self):
        return self.memory
    
    def returner(self):
        return self.value

if __name__ == "__main__":

    while True: 
        try:
            initialValue = input("Enter initial value: ")
            initialValue = float(initialValue)
            break
        
        except ValueError:
            print("Enter integer or float.")    
            continue
    
    
    SC = ScientificCalculator(initialValue)
    print("Operator options:\n +: Add operand to value\n -: Subtract operand from value\n *: Multiply operand with value\n /: Devide value by operand\n **: Power value by operand\n root: Get square root of the value\n rand: Initialize value with random float between 0 and 1\n =: Return value\n MS: Store value in memory. Value will be refreshed to 0\n M+: Add operand to memory value. Value will be refreshed to 0\n M-: Subtract operand from memory value. Value will be refreshed to 0\n MC: Clear memory value\n MR: Return memory value\n quit: Quit calculator\n")

    while True:
        try:
            operator = input("Enter operator: ")
            if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**":
                operand = input("Enter operand: ")
                
                try:
                    operand = float(operand)
                
                except ValueError:
                    print("Enter integer or float.")
                    continue
                
                if operator == "+":
                    SC.add(operand)
                
                elif operator == "-":
                    SC.subtract(operand)
                
                elif operator == "*":
                    SC.multiply(operand)
                    
                elif operator == "/":
                    SC.devide(operand)
                
                elif operator == "**":
                    SC.power(operand)
                
            elif operator == "root" or operator == "rand" or operator == "MS" or operator == "M+" or operator == "M-" or operator == "MC" or operator == "MR" or operator == "=":
                if operator == "root":
                    SC.root
                    ()
                
                elif operator == "rand":
                    SC.rand()

                elif operator == "MS":
                    SC.memoryStore()
                    print("Value stored in memory")
                    
                elif operator == "M+":
                    SC.memoryAdd()
                    print("Current value added to memory value. Current value initialized to 0." )
                    
                elif operator == "M-":
                    SC.memorySubtract()
                    print("Current value subtracted from memory value. Current value initialized to 0." )
                    
                elif operator == "MC":
                    SC.memoryClear()
                    print("Memory value initialized to 0.")
                    
                elif operator == "MR":
                    print(f"Memory value = {SC.memoryRecall()}")
                    
                elif operator == "=":
                    print(f"Value = {SC.returner()}")
        
            elif operator.lower() == "quit":
                break;
            
            else:
                raise ValueError("Incorrect input")
                
        except ValueError as msg:
            print(msg)
            
        