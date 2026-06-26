f = open("C:/Users/Tammanna Datta/Downloads/rosalind_hamm.txt", 'r')
cont = f.read()
L = cont.split('\n')
n = 0
c = 0
s1 = L[0]
s2 = L[1]
n = len(s1)
print(s1,'\n', s2)
for i in range(0,n,1):
    if s1[i]!=s2[i]:
        c+=1
print(c)        
