"""
This program helps store rabbytes' names and ages.
"""

def main_menu():
    """
    Prompts the user to choose an operation to process information.
    """
    
    #This loop will not terminate until the input conforms to the given choice.
    while True:
        print("=" * 34)
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("0. Quit.")
        print("=" * 34)

        choice = input()
        if choice == "1":
            input_name()
        elif choice == "2":
            input_age()
        elif choice == "3":
            list_rabbytes()
        elif choice == "0":
            exit()

def input_name():
    """
    Prompts the users to input rabbit's name.
    """

    #This loop will not terminate until the name is not duplicate.
    while True:
        name = input("Input the new rabbit's name:\n")
        if not name in rabbytes_info:
            rabbytes_info[name] = "(Unknown)"
            main_menu()
        #If the name is not duplicate, this line will be skipped due to the 'main_menu' function. 
        print("That name is already in the database.")
                
def input_age():
    """
    Prompts the users to input rabbit's age.
    """

    #This loop will not terminate until the input name is already stored.
    while True:
        name = input("Input the rabbit's name:\n")
        if name in list(rabbytes_info.keys()):
            age = int(input("Input " + name + "'s age:\n"))
            rabbytes_info[name] = "(" + str(age) + ")"
            main_menu()
        #If the name is stored, this line will be skipped due to again the 'main_menu' function.
        print("That name is not in the database.")

def list_rabbytes():
    """
    This function list all the rabbits' information.
    """

    print("Rabbytes:")
    #Because rabbytes_info is a dictionary, we can use 'items' method and two variables to traverse it.
    for key, value in rabbytes_info.items():
        print(key, value)
    main_menu()

#Use a dictionary to store the paired name and age.
rabbytes_info = {}
main_menu()
