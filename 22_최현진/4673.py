num_set = set(range(1, 10000))
generator_set = set() # 생성자

for num in num_set:
    for n in str(num):
        num += int(n)
    generator_set.add(num)

self_set = num_set - generator_set # 차집합
for self_num in sorted(self_set): # 정렬
    print(self_num)