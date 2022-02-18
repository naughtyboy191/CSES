N=int(input())

cnt=0
while(N>=5):
    N=N//5
    cnt+=N

print(cnt)