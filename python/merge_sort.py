# encoding: utf-8
import sys
import random


def get_random_list(n=1000):
    lis = list(range(n))
    random.shuffle(lis)
    return lis


def merge(A, p, q, r):
    n1 = q - p
    n2 = r - q
    global L, R
    L[0:n1] = A[p:q]
    L[n1] = sys.maxsize
    R[0:n2] = A[q:r]
    R[n2] = sys.maxsize
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, start, end):
    if (start + 1) < end:
        middle = (start + end) // 2
        merge_sort(A, start, middle)
        merge_sort(A, middle, end)
        merge(A, start, middle, end)


def main():
    A = get_random_list()
    num = len(A)
    global L, R
    L = [0] * num
    R = [0] * num
    merge_sort(A, 0, num)
    print(A)


if __name__ == '__main__':
    main()
