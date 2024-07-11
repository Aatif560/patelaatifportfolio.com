n = int(input())


for num in range(1,n+1):

    sum = 0
    temp = num

    while num > 0:

        order = len(str(num))
        digit = temp % 10

        sum += digit ** order

        temp //= 10

    if sum == num:
        print(num)