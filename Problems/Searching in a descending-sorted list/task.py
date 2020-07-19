list_ = list(map(int, input().split()))
target = int(input())
index = -1

for i, value in enumerate(list_):
    if target == value:
        index = -1
        break

print(index)
