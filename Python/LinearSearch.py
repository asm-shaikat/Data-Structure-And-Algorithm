A=input("Enter array: ").split(" ")
A=[int(i) for i in A]
key_value=int(input("Enter key value to searching: "))
A.insert(0,key_value)
i=len(A)-1
while(A[i]!=key_value):
    i-=1
if(i==0):
    print("Element not found")
else:
    print(key_value,"found at position:",i)