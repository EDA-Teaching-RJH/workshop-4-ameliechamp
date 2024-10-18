money = 0
change = 0
while money <= 75:
    moneyinput = int(input("Enter money:"))
    money += moneyinput
    print(money)
    change = money - 75
print("You entered in:",money,". Your change is:", change)
