
import random as rd

v = 30 # upper limit of range of possible answers
half_v = int(v/2)  # used for providing a hint
x = 10 # NUMBER OF GUESSES WE CAN DO

number = rd.randint(0, v)  # generate random integer
hints = {"hint1": False, "hint2": False}  # dictionary to limit loop iterations

while x > 0:
    
    n = input("Enter Integer: ")
    n = int(n)
    # print("N", n)
    # print("Number", number)
    if n == number:
        print("\nYou got it right! Winner Winner Chicken Dinner!")
        print("Number is {}".format(number))
        print("*"*40)
        break
        
    elif x > 5 and x < 9 and hints["hint1"] == False:
        if number < half_v:
            print("Number is < {}".format(half_v))
        else:
            print("Number is > {}".format(half_v))
        x -= 1
        print("-"*40)
        hints["hint1"] = True
        
    elif x < 5 and hints["hint2"] == False:
        if number%2 == 0:
            print("Number is even")
        else:
            print("Number is odd")
        x -= 1
        print("-"*40)
        hints["hint2"] = True
        
    elif x == 1 and n != number:
        print("Game Over!")
        print("="*40)
        x -= 1
    else:
        print("Incorrect")
        print("_"*40)
        x -= 1
