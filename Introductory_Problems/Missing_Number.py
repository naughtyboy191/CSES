n=int(input())
lst=map(int,input().split())

s=n*(n+1)
s=s//2
print(s-sum(lst))