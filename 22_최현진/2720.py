T = input()
T = int(T)

C = []

for i in range(T):
    C.append(int(input()))
    
    Quarter = C[i] // 25
    temp = C[i] % 25
    Dime = temp // 10
    temp %= 10
    Nickel = temp // 5
    temp %= 5
    Penny = temp // 1
    temp %= 1

    print(Quarter, Dime, Nickel, Penny)
