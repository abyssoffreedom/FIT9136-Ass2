"""
This program converts csv files into visible tables and allows several operations on tables.
"""

from tabulate import tabulate
import copy

def main_menu():
    """
    Prompts the user to choose an operation.
    """

    print("=" * 34)
    print("Enter your choice:")
    print("1. List tables.")
    print("2. Display table.")
    print("3. Duplicate table.")
    print("0. Quit.")
    print("=" * 34)

    choice = input()
    if choice == "1":
        list_tables()
    elif choice == "2":
        display_table()
    elif choice == "3":
        duplicate_table()
    elif choice == "0":
        exit()

def list_tables():
    """
    List all tables with their indexes stored in the tables_dictionary.
    """

    header = ["Index", "Columns", "Rows"]
    data = []
    #Dictionary's items must be sorted before being traversed, because dictionary is unordered.
    for key, value in sorted(tables_dictionary.items()):
        #The key represents the index; the value represents a table, 
        #so the length of the value represents the number of rows,
        #and the length of the first line represents the number of columns.
        data.append([key, len(value[0]), len(value)])
    print(tabulate(data, headers = header))
    main_menu()

def display_table():
    """
    Display the chosen table.
    """
    
    while True:
        index = int(input("Choose a table index (to display):\n"))
        if index in tables_dictionary:
            #The value of the dictionary with this index is a table,
            #and the first line in the table represents headers.
            header = tables_dictionary[index][0]
            data = []
            #Exclude the first line that is the header, and the remnants are all table's content.
            for line in tables_dictionary[index][1:]:
                data.append(line)
            print(tabulate(data, headers = header))
            break
        print("Incorrect table index. Try again.")
    main_menu()

def duplicate_table():
    """
    Duplicate the chosen table and allocate it a new index.
    """

    while True:
        index_chosen = int(input("Choose a table index (to duplicate):\n"))
        if index_chosen in tables_dictionary:
            #The new index should be the smallest that has not been used.
            index_allocated = max(tables_dictionary.keys()) + 1
            tables_dictionary[index_allocated] = copy.deepcopy(tables_dictionary[index_chosen])
            break
        print("Incorrect table index. Try again.")
    main_menu()

def read_csv(index, file_name):
    """
    Read csv files into the tables_dictionary with a specific index.
    """

    table = []
    with open(file_name, "r") as fileref:
        for line in fileref:
            #Line is a string, so it needs to be split into a list.
            table.append(line.strip().split(","))
        #Tables_dictionary's key is an index, value is a list of lists.
        tables_dictionary[index] = table


tables_dictionary = {}
csvs_list = ["grades.csv", "class_students.csv", "rabbytes_club_students.csv", "rabbytes_data.csv"]

for index, file_name in enumerate(csvs_list):
    read_csv(index, file_name)

main_menu()
