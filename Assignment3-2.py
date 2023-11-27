def ifSubstring(s1,s2):
    #Make character set from input strings
    set1 = set(s1)
    set2 = set(s2)
    
    if len(set1) == 0 or len(set2) == 0:
        raise ValueError("Input string cannot be empty.")
    
    #Loop through shorter set.
    if len(set1) >= len(set2):
        for char in set2:
            #If there is at least one common character, it is assured that there is a common substring.
            if char in set1:
                print("\nTrue")
                return
        #If there is no common character, 2 strings cannot have common substring.
        print("\nFalse")
        return
                
    else:
        for char in set1:
            if char in set2:
                print("\nTrue")
                return
        
        print("\nFalse")
        return
                
if __name__ == "__main__":
    while True:
        try:
            string1 = input("Input first string: ")
            string2 = input("Input second string: ")
            ifSubstring(string1,string2)
            break
        
        except ValueError as msg:
            print(msg)
