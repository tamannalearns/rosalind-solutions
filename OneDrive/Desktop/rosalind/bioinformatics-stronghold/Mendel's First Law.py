k, m, n = map(int, input().split())
pd = 0
o = k+m+n
pk = k/o
pm = m/o
pn = n/o
pr = 0.25*(pm*(m-1)/(o-1)) + (m*n)/(o*(o-1)) + pn*(n-1)/(o-1)
pd = 1 -pr
print(pd)
