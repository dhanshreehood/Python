yr = int(input("Enter the year you want to check if it is leap or not! "))

#condition
if yr % 4 == 0:
    if yr % 100 != 0:
        print("Leap year")
    elif yr % 100 == 0:
        if yr % 400 == 0:
            print("Leap year")
        else:
            print("Not a Leap Year")
else:
    print("Not a Leap year.")   
