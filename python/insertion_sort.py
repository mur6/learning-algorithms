# encoding: utf-8
import sys
import random


def get_random_list(n):
    lis = list(range(n))
    random.shuffle(lis)
    return lis


def ins_sort(a):
    n = len(a)
    for j in range(1, n):
        key = a[j]
        i = j - 1
        # print(f"{j}: {a}, {key}|{i}")
        while (a[i] > key) and (i >= 0):
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key
    return a


def main():
    num = int(float(sys.argv[1]))
    a = get_random_list(num)
    ins_sort(a)
    print(a)


if __name__ == '__main__':
    main()
