def MaxMin(A,i,j):
    if(i==j):
        fmax=A[i]
        fmin=A[i]
    else:
        if(A[i]<A[j]):
            fmax=A[j]
            fmin=A[i]
fmax=0
fmin=0
A=[2]
MaxMin(A, 0, 0)
print(fmax)
print(fmin)