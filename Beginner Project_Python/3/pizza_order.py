print("\nWelcome to the online Pizza Delivery!")
size = input("\nWhat size pizza do you want? S / M / L: ").strip().upper()
pepperoni = input("\nDo you want to add pepperoni? Y / N: ").strip().upper()
extra_cheese = input("\nDo you want to add extra cheese? Y / N: ").strip().upper()

#condition for bill according to the size:
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

#condition to add extra pepperoni:
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

#condition to add extra cheese:
if extra_cheese == "Y":
        bill += 1
        print(f"Total bill: ${bill}")
else:
    print(f"Total bill: ${bill}")

