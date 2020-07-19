from operator import itemgetter

n = int(input())
student_tuples = []
for _ in range(n):
    i = input().split()
    student_tuples.append((int(i[1]), i[0]))

final = sorted(student_tuples, key=itemgetter(0, 1))
for i in final:
    print(i[1])