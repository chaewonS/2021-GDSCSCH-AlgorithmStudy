word = input().upper()
re_word = list(set(word)) # 입력받은 문자열에서 중복 값 제거

cnt_list = []

for x in re_word:
    cnt = word.count(x)
    cnt_list.append(cnt) # 알파벳 카운드하여 리스트에 저장

if cnt_list.count(max(cnt_list)) > 1: #  카운트 숫자 최대값이 중복되면
    print('?') 
else:
    max_index = cnt_list.index(max(cnt_list)) # 카운트 숫자 최대값 인덱스
    print(re_word[max_index])