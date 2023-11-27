def binary_search(inputList,value):
    inputList.sort()
    low, high = 0, len(inputList)-1

    while low <= high:
        middle = (low+high)//2
        midVal = inputList[middle]
        
        if midVal == value:
            return middle
    
        elif midVal < value:
            low = middle + 1
        
        else:
            high = middle - 1
            
    return -1
    

if __name__ == "__main__":
        try:
            print(binary_search(["dog","cat","shit","planet","what"],"what"))
        except TypeError:
            print("List with different types cannot be sorted.")
    