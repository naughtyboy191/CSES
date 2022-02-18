seq=input()
cur=seq[0]
cnt=1
mx=1
for i in range(1,len(seq)):
    if seq[i]==cur:
        cnt+=1
        mx=max(mx,cnt)
    else:
        cur=seq[i]
        cnt=1

print(mx) 