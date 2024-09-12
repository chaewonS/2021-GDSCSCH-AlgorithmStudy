def solution(enroll, referral, seller, amount):
    TB_PROFIT = 100
    enroll = {name:i for i, name in enumerate(enroll)}
    answer = [0 for _ in range(len(enroll))]

    for i in range(len(amount)):
        total_income = amount[i] * TB_PROFIT
        enr_idx = enroll[seller[i]]

        while referral[enr_idx] != '-':
            if total_income < 1:
                break
            next_income = total_income//10 #다음사람이 가져가는 10%
            answer[enr_idx] += total_income - next_income    #결과 배열에 본인의 수익 저장
            total_income = next_income  #다음 사람에게 넘어가는 전체 수익            
            father = referral[enr_idx]  #추천인 탐색   
            enr_idx = enroll[father]
            
        income = total_income - total_income//10
        answer[enr_idx] += income 
    return answer