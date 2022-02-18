from cmath import sin


s=input()

single=[]
pairs=[]

for c in s:
    if c in single:
        single.remove(c)
        pairs.append(c)
    else:
        single.append(c)

res="".join(pairs)+"".join(single)+"".join(pairs)[::-1]

if res == res[::-1]:
    print(res)
else:
    print("NO SOLUTION")