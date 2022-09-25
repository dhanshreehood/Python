print("Welcome to the tip calculator!")

#taking user data:
total_bill = float(input('What was the total bill? $'))
percent = int(input("What percent tip would you like to give? "))
split = int(input("How many people to split the bill? "))

#result:
result = (total_bill + ((percent/100)*total_bill)) / split

print("Each one have to give: $", round(result,2))