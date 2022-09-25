known_users = ["Almond_man", "Walnut_women", "Pistachio_sister", "Cashew_mommy", "Apricot_brother"]

print(len(known_users))

while True:
    print("\nHi! my name is Dhanshree your one an only a ridiculous security programme")
    
    #to take input from user
    # strip() for extra security, if user puts space while giving input name.
    #capitalize() if i write name starting 1st letter from small letter, it will convert it to capital and then read with capital 1st letter, in this way u can give user flexibility.
    name = input("What is your name hon ?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}".format(name))
        remove = input("would you like to removed from the system (y/n)?: ").strip().lower() #if user put value Y/N instead of y/n lower() will convert it to lowercase, and then it will be read into lower case, will provide flexibility to user.
    
        if remove == "y":
                print(known_users)
                known_users.remove(name)
                print("After removing: \n {}".format(known_users))

        elif remove == "n":
            print("No problem! I didn't want you to leave anyway!")

    else:
        print("hmm... I don't think I've met you yet {}".format(name))
        add_me = input("would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print("After adding you in the system: \n {}".format(known_users))

        elif add_me == "n":
            print("No worries! see you around!")
