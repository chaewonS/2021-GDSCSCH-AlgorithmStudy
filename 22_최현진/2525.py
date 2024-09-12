clock = input().split()
time = int(input())

clock[0] = int(clock[0])
clock[1] = int(clock[1])

hour = clock[0]
min = clock[1] + time

while(1):
    if min >= 60:
        hour += 1
        if hour >= 24:
            hour = 0
        min -= 60
    else:
        break

print(hour, min)