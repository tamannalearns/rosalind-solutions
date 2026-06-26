s = input()
a = 0
g = 0
c = 0
t = 0
for l in s:
    if l == 'A':
        a+=1
    if l == 'G':
        g+=1
    if l == 'T':
        t+=1
    if l == 'C':
        c+=1
print(a,c,g,t)
