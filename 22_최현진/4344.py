C = int(input())
students = []

for _ in range(C):
    cnt = 0
    students = list(map(int, input().split()))
    avg = sum(students[1:]) / students[0]
    for i in students[1:]:
        if i > avg:
            cnt += 1
    ratio = cnt / len(students[1:])
    print("{:.3f}%".format(ratio * 100))