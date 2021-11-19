'''
array insertion
deletation
update
scarching
'''
x=input("Enter array:").split(" ")
x=[int(i) for i in x]
print("Array after insertion")
print(x)

def delete(a):
    x.remove(a)
    print("Array after deletation")
    print(x) 

def update(a,b):
    x.insert(a,b)
    print("After adding new element")
    print(x)

q=int(input("Enter array value to delete:"))
delete(q)
a,b=input("Enter array index and value for update array:").split(" ")
a=int(a)
b=int(b)
update(a,b)
def searching():
    count=0
    r=len(x)-1
    while x[r]!=w:
        r-=1
    if r==0:
        print("Element not found")
    else:
        print("Element found at position: %d"%r)

w=int(input("Value for you are scarching:"))
x.insert(0,w)
searching()