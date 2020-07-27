# created
# by
# Sarvesh
# kumar
# sharma


def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python
    """

    def merge(left, right):
        """merge left and right
        :param left: left collection
        :param right: right collection
        :return: merge result
        """
        result = []
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*merge_sort(unsorted), sep=",")
