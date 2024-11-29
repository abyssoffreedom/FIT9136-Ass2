"""
This program helps store rabbytes' names and ages, as well as parental relationships.
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
        print("4. Create a Parental Relationship.")
        print("5. List Direct Family of a Rabbit.")
        print("0. Quit.")
        print("=" * 34)

        choice = input()
        if choice == "1":
            input_name()
        elif choice == "2":
            input_age()
        elif choice == "3":
            list_rabbytes()
        elif choice == "4":
            create_relationship()
        elif choice == "5":
            list_family()
        elif choice == "0":
            exit()

def input_name():
    """
    Prompts the users to input rabbit's name.
    """

    #This loop will not terminate until the name is not duplicate.
    while True:
        name = input("Input the new rabbit's name:\n")
        if not name in list(rabbytes_name_age.keys()):
            rabbytes_name_age[name] = "(Unknown)"

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
        if name in list(rabbytes_name_age.keys()):
            age = int(input("Input " + name + "'s age:\n"))
            rabbytes_name_age[name] = "(" + str(age) + ")"
            main_menu()
        #If the name is stored, this line will be skipped due to again the 'main_menu' function.
        print("That name is not in the database.")

def list_rabbytes():
    """
    This function lists rabbits' names along with their ages.
    """

    print("Rabbytes:")
    #Because rabbytes_name_age is a dictionary, we can use 'items' method and two variables to traverse it.
    for key, value in rabbytes_name_age.items():
        print(key, value)
    main_menu()

def create_relationship():
    """
    This function creates parental relationship between 2 rabbits.
    """

    parent_name = input("Input the parent's name:\n")
    kitten_name = input("Input the kitten's name:\n")
    #Add new name to name-age dictionary
    if not parent_name in list(rabbytes_name_age.keys()):
        rabbytes_name_age[parent_name] = "(Unknown)"
    if not kitten_name in list(rabbytes_name_age.keys()):
        rabbytes_name_age[kitten_name] = "(Unknown)"

    if not parent_name in list(rabbytes_family.keys()):
        #initialise this name's corresponding value as an empty list
        rabbytes_family[parent_name] = []
    #Whether the name is stored in the name-age dictionary or not, it have to be added into the family dictionary.
    rabbytes_family[parent_name].append(kitten_name)
    main_menu()
    
def list_family():
    """
    This function lists all parental relationships.
    """
    
    while True:
        #Initialise two empty lists to respectively store names of parents and kittens.
        parents_list = []
        kittens_list = []
        name = input("Input the rabbit's name:\n")
        if name in list(rabbytes_name_age.keys()):
            #Use two variables to traverse the dictionary
            for key, value in rabbytes_family.items():
                #in this case, the name refers to a kitten
                if name in value:
                    parents_list.append(key)
                #in this case, the name refers to a parent
                elif key == name:
                    kittens_list = value
            
            print("Parents of", name + ":")
            parents_list.sort()
            for parent_name in parents_list:
                print(parent_name)
            
            print("Kittens of", name + ":")
            kittens_list.sort()
            for kitten_name in kittens_list:
                print(kitten_name)
            main_menu()
        #Only when the name is not found in the name-age dictionary will the following message be printed out.
        print("That name is not in the database.")
    
#Use a dictionary to store the paired name and age.
rabbytes_name_age = {}
#Use a dictionary to store parental relationships.
rabbytes_family = {}
main_menu()



