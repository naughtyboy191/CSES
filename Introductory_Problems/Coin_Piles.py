t=int(input())

for _ in range(t):
    a,b=map(int,input().split())

    if b>a:
        a,b=b,a
    
    if a>2*b:
        print("NO")
        continue

    if (a+b)%3==0:
        print("YES")
    else:
        print("NO")