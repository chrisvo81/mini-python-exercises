from art import logo
print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
flag = False

while not flag:
    step1 = input("left or right?\n").lower()

    if step1 == "left":
        step2 = input("swim or wait?\n").lower()

        if step2 == "wait":
            step3 = input("which door? Red or Blue or Yellow?\n").lower()

            if step3 == "yellow":
                print("You win!")
                flag = True
            elif step3 == "red" or step3 == "blue":
                print("Ahh! Shark!")
                flag = True
            else:
                print("Invalid input. Try again: ")
        else:
            print("You were attacked by a trout. Game over.")
            flag = True
    elif step1 == "right":
        print("You fell in a hole. Game over!")
        flag = True
    else:
        print("Invalid input. Try again: ")
