# Purpose: 100 game.
# Description: Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# Author: Esraa Emary Abd Elsalam.
#version: 4.
# ************************************************************************************ #
sum = 0             # Set the base sum equal 0

print('# =============== Welcome to 100 game =============== #')        # Welcome message and display status
print('Sum is equal to 0')
#=====================================THE GAME======================================#
while sum < 100:           #loop until sum equal 100
    if sum < 90:            #firstly: loop until sum greater than or equal 90 and less than 100
        while True:           # check if the move is an integer number
            try:
                move = int(input("First Player: Choose an integer number from 1 to 10: "))
                break
            except ValueError:
                print("Please enter a valid integer number")

        while move > 10 or move < 1:           #check the validity of the integer number
            print("Please enter a valid integer number")
            while True:
                try:
                    move = int(input("First Player: Choose an integer number from 1 to 10: "))
                    break
                except ValueError:
                    print("Please enter a valid integer number")

    sum += move             # Add the first player move to the sum

    print('Sum is equal to', sum)           #display status

    if (sum >= 90) and (sum < 100):              #secondly: loop until sum equal 100

        print('Second Player is closed to win')             #print an encouraging message

        while True:             # check if the move is an integer number
            try:
                move = int(input(f"Second Player: Choose an integer number from 1 to {(100-sum)}: "))
                break
            except ValueError:
                print("Please enter a valid integer number")

        while move > (100-sum) or move < 1:             #check the validity of the integer number
            print("Please enter a valid integer number")
            while True:
                try:
                    move = int(input(f"Second Player: Choose an integer number from 1 to {(100 - sum)}: "))
                    break
                except ValueError:
                    print("Please enter a valid integer number")

        if move == (100-sum):               # Check if the second player won
            print("Sum is equal to 100")
            print('Second Player is the winner')
            break

    if sum < 90:             #firstly: loop until sum greater than or equal 90 and less than 100
        while True:             # check if the move is a valid integer number
            try:
                move = int(input("Second Player: Choose an integer number from 1 to 10: "))
                break
            except ValueError:
                print("Please enter a valid integer number")

        while move > 10 or move < 1:             # check the validity of the integer number
            print("Please enter a valid integer number")
            while True:
                try:
                    move = int(input("Second Player: Choose an integer number from 1 to 10: "))
                    break
                except ValueError:
                    print("Please enter a valid integer number")

    sum += move             # Add the second player move to the sum

    print('Sum is equal to', sum)           # Display status

    if (sum >= 90) and (sum < 100):             #secondly: loop until sum equal 100

        print('First Player is closed to win')              #print an encouraging message

        while True:             # check if the move is an integer number
            try:
                move = int(input(f"First Player: Choose an integer number from 1 to {(100 - sum)}: "))
                break
            except ValueError:
                print("Please enter a valid integer number")

        while move > (100 - sum) or move < 1:           #check if the move is a valid integer number
            print("Please enter a valid integer number")
            while True:
                try:
                    move = int(input(f"First Player: Choose an integer number from 1 to {(100 - sum)}: "))
                    break
                except ValueError:
                    print("Please enter a valid integer number")

        if move == (100 - sum):             # Check if the first player won
            print("Sum is equal to 100")
            print('First Player is the winner')
            break
