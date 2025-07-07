# game is called should I go out
import random
def main():
    is_raining=True
    while is_raining != False:
        user_answer=input("is it raining(y/n)?").lower()
        if user_answer=="y":
            print("wait a bit")
            continue
        elif user_answer == "n":
            print("you are allowed to leave")
            is_raining =False
        else:
            print("Unknown Error")

if __name__=="__main__":
    main()