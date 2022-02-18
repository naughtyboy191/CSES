n=int(input())

for i in range(1,n+1):
    tot=i**2
    k=tot*(tot-1)
    k=k//2
    if i>2:
        k-=4*(i-2)*(i-1)
    print(k)
