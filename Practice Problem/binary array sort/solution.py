# created
# by
# Sarvesh
# kumar
# sharma


def Sort(a):
    zeros = 0
    for i in range(len(a)):
        if a[i] == 0:
            zeros += 1
    k = 0
    while zeros > 0:
        a[k] = 0
        k += 1
        zeros -= 1
    while k < len(a):
        a[k] = 1
        k += 1
    print(a)


if __name__ == '__main__':
    A = [1, 0, 1, 1, 0]
    Sort(A)
