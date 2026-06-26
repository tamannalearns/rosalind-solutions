f = input()
L = f.split('>')
dn = len(L)
s = ''
gc = 0
c = 0
tag = []
perc = []
for sec in L:
    if sec == '':
        continue
    part = sec.split('\n')
    n = len(part)
    for i in range(0,n,1):
        if i == 0:
            tag.append(part[0])
            continue
        s += part[i]
    no = len(s)
    for i in range(0,no,1):
        if s[i] == 'G'or s[i] == 'C':
            gc+=1
        c+=1
    perc.append(float(gc/c*100))
    c = 0
    gc = 0
maxi = max(perc)
for i in range(0,dn,1):
    if perc[i] == maxi:
        print(tag[i], '\n')
print(maxi)
        
        
