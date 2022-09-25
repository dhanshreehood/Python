#Taking user data of ht and wt:
ht = float(input("What is your ht(in meters)? "))
wt = float(input("What is your wt(in kg)? "))

#bmi formula:
result = wt / (ht**2)

print("Your bmi is ", int(result))