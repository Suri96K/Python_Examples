arr = []
for i in range(0,5):
    inp = input("Enter number : ")
    arr.append(inp)

def PARTITION(A,p,r):
    x = A[r]
    i = p-1
    for j  in range(p,r):
        if(A[j] <= x):
            i = i+1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp1 = arr[i+1]
    arr[i+1] = arr[r]
    arr[r] = temp1
    return i+1

def QUICKSORT(A,p,r):
    if(p<r):
        q=PARTITION(A,p,r)
        QUICKSORT(A,p,q-1)
        QUICKSORT(A,q+1,r)

QUICKSORT(arr,0,len(arr)-1)
print "Sorted Array : "
print arr
