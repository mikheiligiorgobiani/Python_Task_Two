
prices = [1336, 4434, 5100, 2000,750, 1000, 1250, 500, 14050, 3000, 2300, 5110]
budget = int(input("please your budget:"))
result = 500
for i, number in enumerate(prices):
    if prices[i] + result < budget or budget < prices[i]:
        print(prices[i])
    