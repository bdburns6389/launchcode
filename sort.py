mylist = [5, 3, 7, 2, 8, 4]
print(mylist)
n = len(mylist)


for i in range(n):
    for j in range(1, n-i):
        # swap if prev value is less than current value
        # change < to > to reverse the order
        if mylist[j-1] > mylist[j]:
            # do a tuple swap
            (mylist[j-1], mylist[j]) = (mylist[j], mylist[j-1])
print(mylist)