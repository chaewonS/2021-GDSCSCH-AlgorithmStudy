n = int(input())
score = list(map(int, input().split()))
new_score = []
M = max(score)
sum = 0

for i in range(n):
    new_score.append(score[i] / M * 100)
    sum += new_score[i]
    
mean = sum / n
print(mean)