from math import sqrt

n, w, h = list(map(int, input().split()))
total_area = n * w * h
length = sqrt(total_area)
index = -1
for i, value in enumerate(frames):
    if value >= length:
        index = i
        break

print(index)