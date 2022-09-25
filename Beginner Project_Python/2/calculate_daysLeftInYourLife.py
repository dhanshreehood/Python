#taking user data:
age = input("Eenter your age here: ")

# Cqalculating total days, weeks, and months:
remaining_age = int(90 - int(age))
total_days = remaining_age*365
total_weeks = remaining_age*52
total_months = remaining_age*12

#Result:
print(f"You have {total_days} days, {total_weeks} weeks, and {total_months} months left in your life.")

