def quit_sort(A,p,q):
    if(p<q):
        r=partision(A,p,q)
        quit_sort(A, p,r-1)
        quit_sort(A, r+1,q)

def partision(A,p,q):
    x=A[q]
    i=p-1
    for j in range(p,q):
        if(A[j]<=x):
            i+=1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[q] = A[q], A[i+1]
    return i+1
A=[2,1,5,7,10,0,3]
quit_sort(A,0,len(A)-1)
print(A)