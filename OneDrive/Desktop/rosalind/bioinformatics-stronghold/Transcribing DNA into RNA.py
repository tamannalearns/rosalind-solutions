s = input()
L = list(s)
for i in range(0, len(L), 1):
    if L[i] == 'T':
        L[i] = 'U'
for i in L:
    print(i, end = '')
        
        
