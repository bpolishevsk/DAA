# bubble sorting
def bubble_sort(list2):
    # swap_test = False
    for i in range(0, len(list2) - 1):
        swap_test = False
        for j in range(0, len(list2) - i - 1):
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]  # swapping
            swap_test = True
        if swap_test == False:
            break
    return list2


# main
l = list(map(int, input("enter list items ").split(" ")))
print(bubble_sort(l))
