list_ = list(map(int, input().split()))
target = int(input())
k = int(input())


def kth(numbers, target, k):
    tar_list = []
    for i, value in enumerate(numbers):
        if value == target:
            tar_list.append(i)

    try:
        print(tar_list[k - 1])
    except IndexError:
        print(-1)

kth(list_, target, k)
