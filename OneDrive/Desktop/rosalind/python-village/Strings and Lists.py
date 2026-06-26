s = input()
a,b,c,d = map(int, input().split())
L = [a,b,c,d]
if len(s)<=200:
    print(s[a:b+1:1], s[c:d+1:1])
    
    
   
