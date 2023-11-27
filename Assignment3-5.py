import random
import statistics
import time
        
def listMaker(seed):
    if not seed.isnumeric():
        raise ValueError("Invalid input.")
        
    if seed == "0":
        raise ValueError("List length cannot be 0.")
        
    returnList = []
    seed = int(seed)
    
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
    midIndex = len(inputList)//2
    if len(inputList) % 2 == 1:
        return inputList[midIndex]
    else:
        return (inputList[midIndex-1] + inputList[midIndex])/2
               
def medianChecker(x,inputList):
    if x == statistics.median(inputList):
        return True
    else:
        return False
    
if __name__ == "__main__":
    while True:
        try:
            seed = input("Enter the length of the list (positive integer): ")
            start = time.time()
            
            initialList = listMaker(seed)
            
            sortList = listSorter(initialList)
            median = medianFinder(sortList)
            end = time.time()
            
            ellapsedTime = round(end-start,3)
            
            print(f"Median: {median}")
            print(f"Median (standard library): {statistics.median(sortList)}")
            
            if medianChecker(median,initialList):
                print("\nYES!! Result match with standard library!")
                print(f"It took {ellapsedTime} seconds to execute.")
                
            else:
                print("\nNo... Result doesn't match with standard library...")
                print(f"It took {ellapsedTime} seconds to execute.")

            break
            
        except ValueError as msg:
            print(msg + "\n")
            
        except RecursionError:
            print("List is too long to handle... Try something smaller.\n")

            
     
     
        