from sys import stdin

string = stdin.readline()
nums = string.split('-')
sum = 0
for n in range(len(nums)):
    if n == 0:
        for i in nums[n].split('+'):
            sum += int(i)
    else:
        for i in nums[n].split('+'):
            sum -= int(i)
        
print(sum)
