def bubble_sort(alist):
    is_sorted = False
    while is_sorted == False:
        num_swaps = 0
        for a in range(len(alist) -1):
            if alist[a] > alist[a +1]:
                alist[a], alist[a +1] = alist[a +1], alist[a]
                num_swaps = num_swaps + 1
        if num_swaps == 0:
            is_sorted = True
    return alist