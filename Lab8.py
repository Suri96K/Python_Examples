#lab 8
#Question1
'''A = [9,12,10,2,1,5]

def SelectionSort(A):
    n = len(A)
    for j in range(0,n-1):
        smallest = j
        for i in range(j+1,n):
            if A[i]<A[smallest]:
                smallest = i
        A[j],A[smallest] = A[smallest],A[j]

def printArray(A):
    for i in range(0,len(A)):
        print A[i]

SelectionSort(A)
printArray(A)'''


#Question2

A = [2,8,7,1,3,5,6,4]

def printArray(A):
    for i in range(0,len(A)):
        print A[i]

def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
            if A[j]<=x:
                i=i+1
                A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def printArray(A):
    print "After sorting"
    for i in range(0,len(A)):
        print A[i]

partition(A,0,7)
printArray(A)



