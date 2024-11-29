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
    print("0. Quit.")
    print("=" * 34)

    choice = input()
    if choice == "1":
        print_program(program)
    elif choice == "2":
        list_variables(program)
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

def list_variables(program):
    """
    List variables inside the user-entered program.
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
    print("Variables:")
    for variable in variables_list:
        print(variable)
    
    main_menu(program)
    
program = program_input()
main_menu(program)
