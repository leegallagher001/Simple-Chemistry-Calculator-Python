# Simple Chemistry Calculator - by Lee Gallagher

# A program containing some basic data on all of the elements of the periodic table (atomic number, mass number, group etc.) as well as
# a facility for performing some basic calculations with them

# (0) Imports

import json
import os

periodic_table_file = "periodic_table.json"

# (1) Functions

def searchElement(): # Main Menu Option 1 - Element Search

    print("How Would You Like To Search?: ")
    print("\n")
    print("1. Name")
    print("2. Atomic Number")
    print("3. Return To Menu")
    print("\n")
    searchChoice = int(input("Enter Selection: "))
    print("\n")

    if searchChoice == 1: # search element by name

        element_name = input("Enter The Name Of The Element: ")

        with open (periodic_table_file, 'r') as f:
            periodic_table = json.load(f)

            for periodic_table["name"] in periodic_table:
                if element_name == periodic_table["name"]:
                    print("Name: ", periodic_table["name"])
                    print("Atomic Number: ", periodic_table["atomic_number"])
                    print("Mass Number: ", periodic_table["mass_number"])

                    

    if searchChoice == 2: # search element by atomic number

        element_atomic_number = int(input("Enter The Atomic Number Of The Element: "))

        with open (periodic_table_file, 'r') as f:
            periodic_table = json.load(f)

            for atomic_number in periodic_table:
                if element_atomic_number == periodic_table["atomic_number"]:
                    print("Name: ", periodic_table["name"])
                    print("Atomic Number: ", periodic_table["atomic_number"])
                    print("Mass Number: ", periodic_table["mass_number"])

def readme(): # Main Menu Option 3 - Readme

    print("-" * 75)
    print("\n")
    print("HELP & README")
    print("\n")
    print("Hello, and welcome to my Basic Chemistry Calculator program!")
    print("\n")
    print("With this program, I hope to build a small database containing some information about each element of the periodic table, including the element name, atomic number, mass number, element group, as well as perhaps some other information eventually.")
    print("\n")
    print("This program can then be used to retrieve information about those elements, as well as perform simple molecular calculations with them, such as finding the mass of a molecule comprised of certain elements, or to balance simple chemical reaction equations.")
    print("\n")
    print("The program is currently under construction, however, here is some basic information about the menu options currently available.")
    print("\n")
    print("MENU OPTION 1 - ELEMENT SEARCH")
    print("\n")
    print("This part of the program allows the user to retrieve information about a specific element, either searching for it by name or atomic number.")
    print("\n")
    print("Which method you would like to use can be chosen in the sub-menu that is displayed after choosing this option. Select '1' to search by element name, or select '2' to search by atomic number.")
    print("\n")
    print("Once you have chosen your method of search, searching is simply a matter of entering your search query, and the program will pull up all of the information on the element that matches that query.")
    print("\n")
    print("MENU OPTION 2 - MOLECULAR MASS CALCULATOR")
    print("\n")
    print("Currently under construction, I hope that I will eventually be able to use the periodic table database that I make to program a simple molecular mass calculator, allowing the user to select elements and a number of atoms to find the total weight of a molecule comprised of those.")
    print("\n")
    print("I might also build a small database of pre-calculated examples of simple molecules in a similar fashion to the element search function.")
    print("\n")
    print("-" * 75)

# (2) Main Menu

def main(): # the main menu screen upon first loading

    print(" -- BASIC CHEMISTRY CALCULATOR - PYTHON -- ")
    print(" ----------- By Lee Gallagher ------------ ")
    print("\n")
    print("Hello, and welcome to the Basic Chemistry Calculator, where you can learn about the different elements that make up the periodic table as well as perform some calculations with those elements.")
    print("\n")
    print("Please choose from the following options: ")
    print("\n")
    print("1. Search Element")
    print("2. Calculate Mass Of Molecule")
    print("3. README")
    print("4. Exit Program")
    print("\n")
    menuChoice = int(input("Enter Selection: "))
    print("\n")

    while menuChoice != 4:
        if menuChoice == 1:
            searchElement()
            print("\n")
            menuChoice = int(input("Ready For Something Else? Choose Another Option: "))
            print("\n")
        elif menuChoice == 2:
            print("Under Construction")
            menuChoice = int(input("Ready For Something Else? Choose Another Option: "))
            print("\n")
        elif menuChoice == 3:
            readme()
            print("\n")
            menuChoice = int(input("Ready For Something Else? Choose Another Option: "))
            print("\n")
        else:
            menuChoice = int(input("Invalid Input. Please Try Again."))
            print("\n")

main()
