"""
This program helps to retrieve variables in a program.
"""

import keyword

def program_input():
    """
    Prompts the user to enter a program.
    """

    program = []
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    while True:
        line = input()
        if line.strip().lower() == "end":
            return program
        program.append(line)

def main_menu(program):
    """
    Prompts the user to choose the next step.
    """

    print("=" * 34)
    print("Enter your choice:")
    print("1. Print program.")
    print("2. List.")
    print("3. Format.")
    print("0. Quit.")
    print("=" * 34)

    choice = input()
    if choice == "1":
        print_program(program)
    elif choice == "2":
        list_variables(program)
    elif choice == "3":
        format_variable(program)
    elif choice == "0":
        exit()

def print_program(program):
    """
    Print out the user-entered program.
    """

    print("Program:")
    for line in program:
        print(line)
    main_menu(program)

def collect_variables(program):
    """
    Collect variables inside the user-entered program.
    """

    valid_signs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    variables_list = []
    #Each line in the program is a string.
    for line in program:
        #split() actually deletes all whitespaces in the string and turn it into a list of words.
        words_list = line.split()
        for word in words_list:
            # Check the validation and uniqueness of the variable name
            if word[0] in valid_signs and word not in keyword.kwlist and word not in variables_list:
                variables_list.append(word)
    variables_list.sort()
    return variables_list

def list_variables(program):
    """
    List variables inside the user-entered program.
    """

    print("Variables:")
    for variable in collect_variables(program):
        print(variable)
    main_menu(program)

def format_variable(program):
    """
    Change variable's name into snake_case. 
    """
    
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Use an empty list to store the new program after being formatted.
    formatted_program = []
    while True:
        variable_picked = input("Pick a variable:\n")
        if variable_picked in collect_variables(program):
            #Use an empty string to store variable name after being formatted.
            variable_formatted = ""
            for index, char in enumerate(variable_picked):
                #Capitals which are not initial separate an independent word in the name
                #That's why a "_" needs to be added before the capital
                if index != 0 and char in capitals:
                    variable_formatted += "_" + char.lower()
                else:
                    variable_formatted += char.lower()

            for line in program:
                #This list contains words and whitespaces of a line in the program.
                words_list = line.split(" ")
                for index, word in enumerate(words_list):
                    if word == variable_picked:
                        #Replace the old name with the formatted name.
                        words_list[index] = variable_formatted
                    #Recover the list back into the string in its original length.
                    line = " ".join(words_list)
                formatted_program.append(line)
            break
        print("This is not a variable name.")
    main_menu(formatted_program)

program = program_input()
main_menu(program)
