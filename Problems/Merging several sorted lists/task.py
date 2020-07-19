n = int(input())
list_4 = []
for _ in range(n):
    list_4.append(input().split())

list_5 = []
for e in list_4:
    for i in e:
        list_5.append(i)

print(" ".join(sorted(list_5)))

