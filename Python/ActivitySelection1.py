n=int(input("How many activity:"))
print("Enter start and finish time")

temp=[]
for i in range(n):
    a,b=map(int,input("Activity %d:"%i).split())
    temp.append([a,b])
sortedAry=sorted(temp,key= lambda x:x[1])
A=[0]
i=0
for z in range(1,n):
    if(sortedAry[z
    ][0]>=sortedAry[i][1]):
        A.append(z)
        i=z
print(A)