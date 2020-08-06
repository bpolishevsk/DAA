'''
created
by
Sarvesh
kumar
sharma
'''


def largestNumber(array):
    extval, ans = [], ""
    l = len(str(max(array))) + 1
    for i in array:
        temp = str(i) * l
        extval.append((temp[:l:], i))
    extval.sort(reverse=True)
    for i in extval:
        ans += str(i[1])
    if int(ans) == 0:
        return "0"
    return ans


a = [1, 34, 3, 98, 9, 76,
     45, 4, 12, 121]

print(largestNumber(a))
