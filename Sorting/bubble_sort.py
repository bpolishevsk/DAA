# bubble sorting
def bubble_sort(list2):
    # Traverse through array elements 1 less then size of array
    n = len(list2)
    for i in range(0, n - 1):
        # swap_test = False
        swap_test = False
        for j in range(0, n - i - 1):
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]  # swapping
            swap_test = True
        if swap_test == False:
            break
    return list2


# main
l = list(map(int, input("enter list items ").split(" ")))
print(bubble_sort(l))

# output-----
# enter list items 40 10 39 99 46 15
# [10, 15, 39, 40, 46, 99]
#
# Process finished with exit code 0
