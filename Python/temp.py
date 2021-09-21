list1=[1,3,7,8,1,1,3]
maximum=max(list1)
list2=[0]*(maximum+1)
Final=[None]*len(list1)
for i in list1:
    list2[i]=list2[i]+1
for j in range(1,len(list2)):
    list2[j]=list2[j-1]+list2[j]
for k in reversed(list1):
    Final[list2[k]-1]=k
    list2[k]-=1
print("Sorted array")
for item in Final:
    print(item,end=" ")
    