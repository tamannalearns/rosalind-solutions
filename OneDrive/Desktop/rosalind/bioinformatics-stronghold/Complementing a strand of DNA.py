s = input()
sc = s[::-1]
L = list(sc)

for i in range(0, len(L), 1):
    if L[i] == 'T':
        L[i] = 'A'
    elif L[i] == 'A':
        L[i] = 'T'
    elif L[i] == 'C':
        L[i] = 'G'
    elif L[i] == 'G':
        L[i] = 'C'
for i in L:
    print(i, end = '')
        
        
