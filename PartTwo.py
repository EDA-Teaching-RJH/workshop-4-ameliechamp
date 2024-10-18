money = 0
change = 0
coffee = 75
hotchocolate = 80
tea = 70
shot = 5
choice = input("Would you like tea, coffee or hot chocolate?: ").lower()
if choice == "tea":
    option = tea
elif choice == "coffee":
    option = coffee
    extra = input("Would you like to add a shot to your coffee?: ").lower()
    if extra == "yes":
        option = option + shot
    elif extra == "no":
        print("Nevermind.")
    else:
        print("Nevermnd.")
elif choice == "hot chocolate":
    option = hotchocolate
else:
    print("Please enter a drink we have.")

print("Please enter in", option, "p")
while money <= option:
    moneyinput = int(input("Enter money:"))
    money += moneyinput
    print(money)
    change = money - 75
print("You entered in:",money,". Your change is:", change)
