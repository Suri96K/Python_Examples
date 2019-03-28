arr = []
for i in range(0,8):
    inp = input("Enter number : ")
    arr.append(inp)

def INSERTIONSORT(A):
    for j in range(2 , len(arr)):
        key = A[j]
        i = j-1
        while(i>-1 and A[i]>key):
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key


print("Sorted Array : ")
INSERTIONSORT(arr)
print arr

