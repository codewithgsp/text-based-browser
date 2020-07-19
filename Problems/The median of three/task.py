def partition(lst, start, end):
    j = start
    for i in range(start + 1, end + 1):
        if lst[start] > lst[i]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[j], lst[start] = lst[start], lst[j]

    same = j
    for k in range(j + 1, end + 1):
        if lst[j] == lst[k]:
            same += 1
            lst[same], lst[k] = lst[k], lst[same]

    lst[same], lst[j] = lst[j], lst[same]

    return j, same


def quicksort(lst, start, end):
    global l, r
    if start >= end:
        return

    j, same = partition(lst, start, end)
    if same - j >= r - l:
        l, r = j, same

    if start == l and same + 1 == r:
        quicksort(lst, start, j - 1)
        quicksort(lst, same + 1, end)


lst = [int(x) for x in input().split()]
quicksort(lst, 0, len(lst) - 1)
print(l, r)
print(*lst)
