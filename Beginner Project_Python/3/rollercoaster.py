print("Welcome to the Rollercoaster!")
ht = float(input("Please enter your ht(in cm) here: "))
bill = 0
#condition for bill after knowing their age:
if ht >= 120:
    print("You can ride!")
    age = int(input("Enter Your age: "))

    if age < 12:
        bill = 5
        #print("Child have to pay $5.")
    elif age <= 18:
        bill = 7
        #print("Youth have to pay $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Aged people can enjoy a Free ride on us!.")
    else:
        bill = 12
        #print("Youth have to pay $12.")
    
    #condition for photo and total bill
    pic = input("Do you want to be photo taken?(y/n): ").strip().lower()
    if pic == "y":
        bill += 3
        print(f"Total bill: ${bill}")
    else:
        print(f"Total bill: ${bill}")    

else:
    print("You can't ride!")