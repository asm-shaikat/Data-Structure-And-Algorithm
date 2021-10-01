def merge(a,p,q,r):
    L=a[p:q+1]  #to copy form array a
    R=a[q+1:r+1]
    L.append(float('inf'))
    R.append(float('inf'))

    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
def merge_sort(a,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a,p,q,r)
a=[0,100,2,3,7,90,300]
merge_sort(a, 0,len(a)-1)
print(a)