s = input()
d = {}
L = s.split()
n = len(L)
for word in L:
    if word in d:
        d[word]+=1
    else:
        d[word] = 1
for key, value in d.items():
    print(key, value)
