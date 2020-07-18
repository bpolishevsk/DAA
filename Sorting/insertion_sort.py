def insertion_sort(list2):
    n = len(list2)
    for i in range(1, n):
        save = list2[i]
        j = i
        while j > 0 and list2[j - 1] > save:
            list2[j] = list2[j - 1]
            j -= 1
        list2[j] = save
    return list2


# main
l = list(map(int, input("enter list items ").split(" ")))
print(insertion_sort(l))

#  output-----
# enter list items 100 3 20 900 32 11
# [3, 11, 20, 32, 100, 900]
