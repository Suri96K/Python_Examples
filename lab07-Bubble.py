arr = []
for i in range(0,5):
    inp = input("Enter number : ")
    arr.append(inp)

def BUBBLESORT(A):
    for i in range(0 , len(A)-1):
        for j in range(len(A)-1, i, -1):
           if(A[j] < A[j-1]):
               temp = A[j]
               arr[j] = arr[j-1]
               arr[j-1] = temp


print ("Sorted Array :")
BUBBLESORT(arr)
print ("arr")
