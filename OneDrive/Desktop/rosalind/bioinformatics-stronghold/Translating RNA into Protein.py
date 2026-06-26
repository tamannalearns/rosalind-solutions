f = open("C:/Users/Tammanna Datta/Downloads/codon table.txt", 'r')
cont = f.read()
codon = cont.split()
d = ""
s = input()
stri = ""
l = len(s)
n = len(codon)
for i in range(0,l,3):
    d = ""
    a = s[i:i+3:1]
    for j in range(0,n,2):
        if codon[j] == a:
            d = codon[j+1]
            break
    if d == "Stop":
        break
    else:
        stri+=d
print(stri)
            
