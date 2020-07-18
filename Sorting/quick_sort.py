# quick sort
def quick_sort(list2):
    quick_sort_r(list2, 0, len(list2) - 1)
    return list2


# quick_sort_r, recursive (used by quick_sort)
def quick_sort_r(list2, first, last):
    if last > first:
        pivot = partition(list2, first, last)
        quick_sort_r(list2, first, pivot - 1)
        quick_sort_r(list2, pivot + 1, last)


# partition (used by quick_sort_r)
def partition(list2, first, last):
    sred = (first + last) / 2
    if list2[first] > list2[sred]:
        list2[first], list2[sred] = list2[sred], list2[first]  # swap
    if list2[first] > list2[last]:
        list2[first], list2[last] = list2[last], list2[first]  # swap
    if list2[sred] > list2[last]:
        list2[sred], list2[last] = list2[last], list2[sred]  # swap
    list2[sred], list2[first] = list2[first], list2[sred]  # swap
    pivot = first
    i = first + 1
    j = last

    while True:
        while i <= last and list2[i] <= list2[pivot]:
            i += 1
        while j >= first and list2[j] > list2[pivot]:
            j -= 1
        if i >= j:
            break
        else:
            list2[i], list2[j] = list2[j], list2[i]  # swap
    list2[j], list2[pivot] = list2[pivot], list2[j]  # swap
    return j
