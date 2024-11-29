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
    print("4. Create table.")
    print("5. Delete table.")
    print("6. Delete column.")
    print("7. Restore table.")
    print("0. Quit.")
    print("=" * 34)

    choice = input()
    if choice == "1":
        list_tables()
    elif choice == "2":
        display_table()
    elif choice == "3":
        duplicate_table()
    elif choice == "4":
        create_table()
    elif choice == "5":
        delete_table()
    elif choice == "6":
        delete_column()
    elif choice == "7":
        restore_table()
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
            #The index of deleted table is reserved,
            #and the outter max() is used to prevent the deleted table's index being assigned to the new table.
            index_allocated = max(max(tables_dictionary.keys()), max(deleted_tables.keys())) + 1
            #Use deepcopy so that modification of one table will not affect its duplicate.
            tables_dictionary[index_allocated] = copy.deepcopy(tables_dictionary[index_chosen])
            break
        print("Incorrect table index. Try again.")
    main_menu()

def create_table():
    """
    Create a table via selecting some columns from an existing table.
    """

    while True:
        index_chosen = int(input("Choose a table index (to create from):\n"))
        if index_chosen in tables_dictionary:
            index_allocated = max(max(tables_dictionary.keys()), max(deleted_tables.keys())) + 1
            columns_chosen = input("Enter the comma-separated indices of the columns to keep:\n")
            #The new table which is about to create
            table = []
            #Each line is a list in a table.
            for line in tables_dictionary[index_chosen]:
                #Use an empty list to store a line of the new table.
                row = []
                #Column_index is a string, with which we can find the wanted value in a specific column,
                #and add this value into a line of the new table.
                for column_index in columns_chosen.split(","):
                    row.append(line[int(column_index)])
                table.append(row)
            tables_dictionary[index_allocated] = table
            break
        print("Incorrect table index. Try again.")
    main_menu()

def delete_table():
    """
    Delete an exsiting table.
    """

    while True:
        index_chosen = int(input("Choose a table index (for table deletion):\n"))
        if index_chosen in tables_dictionary:
            deleted_tables[index_chosen] = copy.deepcopy(tables_dictionary[index_chosen])
            del tables_dictionary[index_chosen]
            break
        print("Incorrect table index. Try again.")
    main_menu()

def delete_column():
    """
    Delete a column in an exsiting table.
    """

    while True:
        index_table = int(input("Choose a table index (for column deletion):\n"))
        if index_table in tables_dictionary:
            index_column = int(input("Enter the index of the column to delete:\n"))
            for row in tables_dictionary[index_table]:
                del row[index_column]
            break
        print("Incorrect table index. Try again.")
    main_menu()

def restore_table():
    """
    Restore the table has been deleted.
    """

    while True:
        index_chosen = int(input("Choose a table index (for restoration):\n"))
        if index_chosen in deleted_tables and index_chosen != -1:
            #deleted_tables is a dictionary that stores the data of tables being deleted.
            tables_dictionary[index_chosen] = copy.deepcopy(deleted_tables[index_chosen])
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
        #Tables_dictionary's key is an index, and value is a table, i.e. a list of lists.
        tables_dictionary[index] = table


tables_dictionary = {}
csvs_list = ["grades.csv", "class_students.csv", "rabbytes_club_students.csv", "rabbytes_data.csv"]
#"-1: []" is added here to prevent max() in line 90 and 104 from comparing a null value,
#which results in a runtime error.
deleted_tables = {-1: []}

for index, file_name in enumerate(csvs_list):
    read_csv(index, file_name)

main_menu()
