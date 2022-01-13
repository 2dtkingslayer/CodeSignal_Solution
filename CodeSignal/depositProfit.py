def depositProfit(deposit, rate, threshold):
    n = 0
    res = deposit * ((1 + rate/100)**n)
    while (res < threshold):
        n += 1
    return n
print(2*3)
print(depositProfit(100 , 20 , 170))