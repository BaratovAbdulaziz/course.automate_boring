# import is used to import different modules build in the python or downloaded manually
# it lets to use different logics that was made using basic functions by different users 
# importing is a good time saving
import random
def main():
    chances = 7


    # randomly picking number from 1 up to 25

    random_integer = random.randint(1,25)

    # printing a statement
    
    print(f"you have {chances} chances the number is >= 1 and number <= 25")

    # making condition checker that continues do the task until the conditions remains True
    
    while chances != 0:

        #example for  assigning value using input:

        user_gees = int(input("write any number"))

        if user_gees == random_integer and chances !=0:

            # printing winning statement

            print(f"congrats you won the number was {random_integer} you had {chances} chances left")
            # f-string (f"{variable name}") is used to add variable values directly inside printing string

        elif user_gees > random_integer and chances != 0:
            
            # elif will be exacted if the if statement will not be True
            
            print("The number is higher than gassed number (choose smaller number!)")
            
            # printing out what is wrong with the number

            chances -= 1
            
            # subtracting one point from  chances if the guess is wrong
            
            print(f"chances lift{chances}")
        elif user_gees < random_integer and chances!=0:
            print("The number is lower than gassed number (choose bigger number!)")
            chances-= 1
            print(f"chances left: {chances}")
        if chances <= 0:
            print("you are out of chances")
            print(f"The correct number was {random_integer}")

if __name__ == "__main__":
    # the line above checks if the file is original or if it is being used as module
    
    main() 
    
    # last line is calling the main function
else:
    print(__name__)