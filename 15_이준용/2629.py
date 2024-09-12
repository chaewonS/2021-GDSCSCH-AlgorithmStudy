from sys import stdin
input = stdin.readline

def solve(w_idx, weight):
    if w_idx > w_count or dp[w_idx][weight]:
        #모든 추를 다 쓰거나 이미 해당 무게를 만들었다면 종료
        return
    dp[w_idx][weight] = 1

    solve(w_idx+1, weight)  #해당 추 선택 X
    solve(w_idx+1, weight+ weight_list[w_idx])  #구슬의 반대편 저울
    solve(w_idx+1, abs(weight - weight_list[w_idx]))    #구슬쪽 저울
    
w_count = int(input())    #추의 개수
weight_list = list(map(int, input().split()))   #추 리스트
weight_list.append(0)
dp = [[0 for j in range(i*500+1)] for i in range(w_count+1)]


solve(0,0)  #모든 경우의 수 구함

m_count = int(input())  #구슬 개수
marble_list = list(map(int, input().split()))   #구슬 리스트

for marble in marble_list:
    if marble > 15000:
        print('N', end=' ')
    elif(dp[w_count][marble]):
        print('Y', end=' ')
    else:
        print('N', end=' ')