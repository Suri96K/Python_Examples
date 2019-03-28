lst = [None]*10

lst = [32,25,36,45,13,65,2,53,65,15]
print "Unsorted Array"

for i in range(0,10):
    print lst[i]

##Method 1

for i in range(1,10):
    for j in range(0,(10-i)):
        if lst[j] > ls[j+1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp

##Method 2
for i in range(1,10):
    for j in range(9,i-1,-1):
        if lst[j] < lst[j-1]:
            temp = lst[j]
            lst[j] = lst[j-1]
            lst[j-1] = temp

print "Sorted Array"
for i in range(0,10):
    print lst[i]
