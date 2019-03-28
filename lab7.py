ls = [None]*10
i =0
while(i<=9):
    num = int(input("Enter a number between 10 and 20 : "))
    if(num<10 or num>=20):
        print "Invalid input.!"
    else:
        ls[i] = num
        i+=1;

print "Unsroted Array"
for i in range(0,10):
    print ls[i]



for j in range(1,10):
    key = ls[j]
    i = j-1
    while i>-1 and ls[i]>key:
        ls[i+1] = ls[i]
        i = i-1
        ls[i+1] = key

print "Sorted Array"
for i in range(0,10):
    print ls[i]
