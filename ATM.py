def solve(n):
    if n % 10 != 0:
        return -1
    current_value = 0
    ten_bill = 0
    twenty_bill = 0
    fifty_bill = 0
    hundred_bill = 0
    twohund_bill = 0
    fivehun_bill = 0
    while current_value < n:
        if n - current_value >= 500:
            current_value += 500
            fivehun_bill += 1
        elif n - current_value >= 200:
            current_value += 200
            twohund_bill += 1
        elif n - current_value >= 100:
            current_value += 100
            hundred_bill += 1
        elif n - current_value >= 50:
            current_value += 50
            fifty_bill += 1
        elif n - current_value >= 20:
            current_value += 20
            twenty_bill += 1
        elif n - current_value >= 10:
            current_value += 10
            ten_bill += 1
    return(ten_bill + twenty_bill + fifty_bill + hundred_bill + twohund_bill + fivehun_bill)

solve(770)
solve(1250)
solve(125)