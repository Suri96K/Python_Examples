arr = []
for i in range(0,10):
    inp = input("Enter number : ")
    arr.append(inp)


def SELECTIONSORT(A):
    n = len(A)
    for j in range(0,n-1):
        smallest = j
        for i in range(j+1,n):
            if(A[i] < A[smallest]):
                smallest = i
        temp = arr[j]
        arr[j] = arr[smallest]
        arr[smallest] = temp

print "Sorted Array : "
SELECTIONSORT(arr)
print arr
