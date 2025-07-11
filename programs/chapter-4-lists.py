import time,sys
def main():
    cat_name = []
    print(">'q'< to exit the program ")
    print(">>Welcome to a program that collects cat names")
    # making while loop to go on asking user to enter cat name
    while True:
        inputted_data =input("Enter the cat name\nhere:")
# checking user input and adding to the list

        if inputted_data.lower() =="q":
            print(cat_name)
            sys.exit()
        elif inputted_data=="":
            print("Are you serious?")
            continue
        else:
            cat_name.append(inputted_data)
            continue
if __name__ == "__main__":
    main()
# --- END IGNORE ---