#Treaure Island Game:
print("Welcome to the treasure Island. Your mission is to find the treasure.")
left_right = input("\nDo you want to take 'left' or 'right'?: ").strip().lower()

#left or right condition:
if left_right == "left":
    #swim or wait condition:
    swim_wait = input("\nThere is an island. Type 'wait' to wait for the boat or type 'swim' to swim across the lake: ").strip().lower()
    if swim_wait == "wait":
        #condition for door:
        door = input("\nYou have reached the island unharmed! There are 3 doors in front of you of color 'red', 'blue' and 'yellow'. Enter which color do you choose?: ").strip().lower()
        if door == "yellow":
            print("Congratulations!!! You Win!!!")
        elif door == "red":
            print("You enter into a room of sea beasts. Game Over!!!")
        elif door == "blue":
            print("You enter into a long ditch. Game Over!!!")
    else:
        #game over
        print("You are eaten by sharks. Game Over!!!")
else:
    #game over
    print("You enter into a zombie jungle. Game Over!!!")