from collections import Counter
import sys
n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    a = int(sys.stdin.readline())
    num_list.append(a)

num_list = sorted(num_list)
num_tuple = tuple(num_list)
#산술평균
print(round(sum(num_list) / n))
#중앙값
print(num_list[int(n / 2)])

max_num = max(num_list)
min_num = min(num_list)
#최빈값 계산
mode = 0

counter = Counter(num_list)
not_overlap_list = []
# for i in range(len(num_list)):
#     if num_list[i] not in not_overlap_list:
#         not_overlap_list.append(num_list[i])
#print(not_overlap_list)

for i in range(len(not_overlap_list)):
    if i == 0:
        mode = counter[num_list[i]]
        mode_1 = num_list[i]
        mode_2 = ''
    else:
        if counter[num_list[i]] == mode:
            if mode_1 > num_list[i]:
                mode_2 = mode_1
                mode_1 = num_list[i]
            if mode_2 != '':
                if mode_1 < num_list[i] < mode_2:
                    mode_2 = num_list[i]
            else:
                if mode_1 < num_list[i]:
                    mode_2 = num_list[i]
                else:
                    mode_2 = mode_1
                    mode_1 = num_list[i]
        elif counter[num_list[i]] > mode:
            mode = counter[num_list[i]]
            mode_1 = num_list[i]
            mode_2 = ''

if mode_2 == '':
    print(mode_1)
else:
    print(mode_2)
#범위
print(max_num - min_num)