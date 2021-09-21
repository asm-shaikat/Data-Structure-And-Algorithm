A=[1,3,7,8,1,1,3]
maximum=max(A)
C=[0]*(maximum+1)
F=[None]*len(A)
for item in A:
    C[item]=C[item]+1
for i in range(1,len(C)):
    C[i]=C[i-1]+C[i]
for item in reversed(A):
    F[C[item]-1]=item
    C[item]-=1
print("Array after sort")
for item in F:
    print(item,end=" ")