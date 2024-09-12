import sys
t = int(sys.stdin.readline())  #테스트 개수
for _ in range(t):
    n = int(sys.stdin.readline())  #전화번호 개수
    #공백 제거 필요
    num_list = [sys.stdin.readline().strip()
                for j in range(n)]  #이 줄로 밑에 줄 내용 해결
    # for j in range(n):
    #     call_num = int(sys.stdin.readline())
    #     num_list.append(call_num)
    num_list = sorted(num_list)
    flag = True
    for i in range(n - 1):
        long = len(num_list[i])
        if num_list[i] == num_list[i + 1][:long]:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
