a=[1,3,0,5,3,5,6,8,8,2,12]
b=[4,5,6,7,8,9,10,11,12,13,14]

x=0
q=[0]
for i in range(1,len(a)):
    if(a[i]>=b[x]):
        q.append(i)
        x=i
print(q)

