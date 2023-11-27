import random
import statistics
        
def listMaker(seed):
    returnList = []
    for i in range(seed):
        returnList.append(random.randint(0,1000))
        
    return returnList
            
def listSorter(inputList):
    #imprement quick sort
    if len(inputList) <= 1:
        return inputList
        
    else:
        pivot = inputList[0]
        lesser = [x for x in inputList[1:] if x <= pivot]
        greater = [x for x in inputList[1:] if x > pivot]
            
        return listSorter(lesser) + [pivot] + listSorter(greater)
    
def medianFinder(inputList):
    if len(inputList) % 2 == 0:
        return()
            
def medianChecker(x,inputList):
    if x == statistics.median(inputList):
        return True
    else:
        return False
    
if __name__ == "__main__":
    
     seed = input("Enter length of the list: ")
     
     
        