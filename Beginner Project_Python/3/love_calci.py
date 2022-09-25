#Love Calculator Project
print("Welcome to Love calculator!")
name1 = input("Enter your name: ").lower()
name2 = input("Enter their name: ").lower()

combined_name = name1 + name2
#print(combined_name)

#to count the letter:
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = str(t + r + u + e)

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = str(l + o + v + e)

love_score = int(true + love)
print(love_score)

#condition for print
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, You go together like Coke and Mentos!")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score},  your alright together!")
else:
    print(f"Your score is {love_score}.")

