with open("C:/Users/Tammanna Datta/Downloads/rosalind_ini5 (1).txt") as f:
    c = 1
    for line in f:
        if c%2==0:
            print(line)
        c+=1
    
