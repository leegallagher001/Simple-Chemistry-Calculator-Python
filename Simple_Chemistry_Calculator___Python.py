# Simple Chemistry Calculator - by Lee Gallagher

# A program containing some basic data on all of the elements of the periodic table (atomic number, mass number, group etc.) as well as
# a facility for performing some basic calculations with them

# (0) Imports

import csv
import pandas as pd
import os

# (0.1) Test Data

# I started off by manually entering the first few elements, then used AI to create the rest of the list in that format
# as I thought that doing it all manually would have been laborious and more prone to error, although I did end up adding the symbols manually
# later on as I decided that would be a cool feature

periodic_table = {} # our database of periodic table info

periodic_table["Hydrogen"] = {"name": "Hydrogen", "symbol": "H", "atomic_number": 1,"mass_number": 1.008}
periodic_table["Helium"] = {"name": "Helium", "symbol": "He", "atomic_number": 2,"mass_number": 4.003}
periodic_table["Lithium"] = {"name": "Lithium", "symbol": "Li", "atomic_number": 3,"mass_number": 6.940}
periodic_table["Beryllium"] = {"name": "Beryllium", "symbol": "Be", "atomic_number": 4, "mass_number": 9.012}
periodic_table["Boron"] = {"name": "Boron", "symbol": "B", "atomic_number": 5, "mass_number": 10.81}
periodic_table["Carbon"] = {"name": "Carbon", "symbol": "C", "atomic_number": 6, "mass_number": 12.011}
periodic_table["Nitrogen"] = {"name": "Nitrogen", "symbol": "N", "atomic_number": 7, "mass_number": 14.007}
periodic_table["Oxygen"] = {"name": "Oxygen", "symbol": "O", "atomic_number": 8, "mass_number": 15.999}
periodic_table["Fluorine"] = {"name": "Fluorine", "symbol": "F", "atomic_number": 9, "mass_number": 18.998}
periodic_table["Neon"] = {"name": "Neon", "symbol": "Ne", "atomic_number": 10, "mass_number": 20.180}
periodic_table["Sodium"] = {"name": "Sodium", "symbol": "Na", "atomic_number": 11, "mass_number": 22.990}
periodic_table["Magnesium"] = {"name": "Magnesium", "symbol": "Mg", "atomic_number": 12, "mass_number": 24.305}
periodic_table["Aluminium"] = {"name": "Aluminium", "symbol": "Al", "atomic_number": 13, "mass_number": 26.982}
periodic_table["Silicon"] = {"name": "Silicon", "symbol": "Si", "atomic_number": 14, "mass_number": 28.085}
periodic_table["Phosphorus"] = {"name": "Phosphorus", "symbol": "P", "atomic_number": 15, "mass_number": 30.974} 
periodic_table["Sulfur"] = {"name": "Sulfur", "symbol": "S", "atomic_number": 16, "mass_number": 32.06}
periodic_table["Chlorine"] = {"name": "Chlorine", "symbol": "Cl", "atomic_number": 17, "mass_number": 35.45}
periodic_table["Argon"] = {"name": "Argon", "symbol": "Ar", "atomic_number": 18, "mass_number": 39.948}
periodic_table["Potassium"] = {"name": "Potassium", "symbol": "K", "atomic_number": 19, "mass_number": 39.098}
periodic_table["Calcium"] = {"name": "Calcium", "symbol": "Ca", "atomic_number": 20, "mass_number": 40.078}
periodic_table["Scandium"] = {"name": "Scandium", "symbol": "Sc", "atomic_number": 21, "mass_number": 44.956}
periodic_table["Titanium"] = {"name": "Titanium", "symbol": "Ti", "atomic_number": 22, "mass_number": 47.867}
periodic_table["Vanadium"] = {"name": "Vanadium", "symbol": "V", "atomic_number": 23, "mass_number": 50.942}
periodic_table["Chromium"] = {"name": "Chromium", "symbol": "Cr", "atomic_number": 24, "mass_number": 51.996}
periodic_table["Manganese"] = {"name": "Manganese", "symbol": "Mn", "atomic_number": 25, "mass_number": 54.938}
periodic_table["Iron"] = {"name": "Iron", "symbol": "Fe", "atomic_number": 26, "mass_number": 55.845}
periodic_table["Cobalt"] = {"name": "Cobalt", "symbol": "Co", "atomic_number": 27, "mass_number": 58.933}
periodic_table["Nickel"] = {"name": "Nickel", "symbol": "Ni", "atomic_number": 28, "mass_number": 58.693}
periodic_table["Copper"] = {"name": "Copper", "symbol": "Cu", "atomic_number": 29, "mass_number": 63.546}
periodic_table["Zinc"] = {"name": "Zinc", "symbol": "Zn", "atomic_number": 30, "mass_number": 65.38} 
periodic_table["Gallium"] = {"name": "Gallium", "symbol": "Ga", "atomic_number": 31, "mass_number": 69.723}
periodic_table["Germanium"] = {"name": "Germanium", "symbol": "Ge", "atomic_number": 32, "mass_number": 72.630}
periodic_table["Arsenic"] = {"name": "Arsenic", "symbol": "As", "atomic_number": 33, "mass_number": 74.922}
periodic_table["Selenium"] = {"name": "Selenium", "symbol": "Se", "atomic_number": 34, "mass_number": 78.971}
periodic_table["Bromine"] = {"name": "Bromine", "symbol": "Br", "atomic_number": 35, "mass_number": 79.904}
periodic_table["Krypton"] = {"name": "Krypton", "symbol": "Kr", "atomic_number": 36, "mass_number": 83.798}
periodic_table["Rubidium"] = {"name": "Rubidium", "symbol": "Rb", "atomic_number": 37, "mass_number": 85.468}
periodic_table["Strontium"] = {"name": "Strontium", "symbol": "Sr", "atomic_number": 38, "mass_number": 87.62}
periodic_table["Yttrium"] = {"name": "Yttrium", "symbol": "Y", "atomic_number": 39, "mass_number": 88.906}
periodic_table["Zirconium"] = {"name": "Zirconium", "symbol": "Zr", "atomic_number": 40, "mass_number": 91.224}
periodic_table["Niobium"] = {"name": "Niobium", "symbol": "Nb", "atomic_number": 41, "mass_number": 92.906}
periodic_table["Molybdenum"] = {"name": "Molybdenum", "symbol": "Mo", "atomic_number": 42, "mass_number": 95.95}
periodic_table["Technetium"] = {"name": "Technetium", "symbol": "Tc", "atomic_number": 43, "mass_number": 98}
periodic_table["Ruthenium"] = {"name": "Ruthenium", "symbol": "Ru", "atomic_number": 44, "mass_number": 101.07}
periodic_table["Rhodium"] = {"name": "Rhodium", "symbol": "Rh", "atomic_number": 45, "mass_number": 102.91} 
periodic_table["Palladium"] = {"name": "Palladium", "symbol": "Pd", "atomic_number": 46, "mass_number": 106.42}
periodic_table["Silver"] = {"name": "Silver", "symbol": "Ag", "atomic_number": 47, "mass_number": 107.87}
periodic_table["Cadmium"] = {"name": "Cadmium", "symbol": "Cd", "atomic_number": 48, "mass_number": 112.41}
periodic_table["Indium"] = {"name": "Indium", "symbol": "In", "atomic_number": 49, "mass_number": 114.82}
periodic_table["Tin"] = {"name": "Tin", "symbol": "Sn", "atomic_number": 50, "mass_number": 118.71}
periodic_table["Antimony"] = {"name": "Antimony", "symbol": "Sb", "atomic_number": 51, "mass_number": 121.76}
periodic_table["Tellurium"] = {"name": "Tellurium", "symbol": "Te", "atomic_number": 52, "mass_number": 127.60}
periodic_table["Iodine"] = {"name": "Iodine", "symbol": "I", "atomic_number": 53, "mass_number": 126.90}
periodic_table["Xenon"] = {"name": "Xenon", "symbol": "X", "atomic_number": 54, "mass_number": 131.29}
periodic_table["Cesium"] = {"name": "Cesium", "symbol": "Cs", "atomic_number": 55, "mass_number": 132.91}
periodic_table["Barium"] = {"name": "Barium", "symbol": "Ba", "atomic_number": 56, "mass_number": 137.33}
periodic_table["Lanthanum"] = {"name": "Lanthanum", "symbol": "La", "atomic_number": 57, "mass_number": 138.91}
periodic_table["Cerium"] = {"name": "Cerium", "symbol": "Ce", "atomic_number": 58, "mass_number": 140.12}
periodic_table["Praseodymium"] = {"name": "Praseodymium", "symbol": "Pr", "atomic_number": 59, "mass_number": 140.91}
periodic_table["Neodymium"] = {"name": "Neodymium", "symbol": "Nd", "atomic_number": 60, "mass_number": 144.24}
periodic_table["Promethium"] = {"name": "Promethium", "symbol": "Pm", "atomic_number": 61, "mass_number": 145}
periodic_table["Samarium"] = {"name": "Samarium", "symbol": "Sm", "atomic_number": 62, "mass_number": 150.36}
periodic_table["Europium"] = {"name": "Europium", "symbol": "Eu", "atomic_number": 63, "mass_number": 151.96}
periodic_table["Gadolinium"] = {"name": "Gadolinium", "symbol": "Gd", "atomic_number": 64, "mass_number": 157.25}
periodic_table["Terbium"] = {"name": "Terbium", "symbol": "Tb", "atomic_number": 65, "mass_number": 158.93}
periodic_table["Dysprosium"] = {"name": "Dysprosium", "symbol": "Dy", "atomic_number": 66, "mass_number": 162.50}
periodic_table["Holmium"] = {"name": "Holmium", "symbol": "Ho", "atomic_number": 67, "mass_number": 164.93}
periodic_table["Erbium"] = {"name": "Erbium", "symbol": "Er", "atomic_number": 68, "mass_number": 167.26}
periodic_table["Thulium"] = {"name": "Thulium", "symbol": "Tm", "atomic_number": 69, "mass_number": 168.93}
periodic_table["Ytterbium"] = {"name": "Ytterbium", "symbol": "Yb", "atomic_number": 70, "mass_number": 173.05}
periodic_table["Lutetium"] = {"name": "Lutetium", "symbol": "Lu", "atomic_number": 71, "mass_number": 174.97}
periodic_table["Hafnium"] = {"name": "Hafnium", "symbol": "Hf", "atomic_number": 72, "mass_number": 178.49}
periodic_table["Tantalum"] = {"name": "Tantalum", "symbol": "Ta", "atomic_number": 73, "mass_number": 180.95}
periodic_table["Tungsten"] = {"name": "Tungsten", "symbol": "W", "atomic_number": 74, "mass_number": 183.84}
periodic_table["Rhenium"] = {"name": "Rhenium", "symbol": "Re", "atomic_number": 75, "mass_number": 186.21}
periodic_table["Osmium"] = {"name": "Osmium", "symbol": "Os", "atomic_number": 76, "mass_number": 190.23}
periodic_table["Iridium"] = {"name": "Iridium", "symbol": "Ir", "atomic_number": 77, "mass_number": 192.22}
periodic_table["Platinum"] = {"name": "Platinum", "symbol": "Pt", "atomic_number": 78, "mass_number": 195.08}
periodic_table["Gold"] = {"name": "Gold", "symbol": "Au", "atomic_number": 79, "mass_number": 196.97}
periodic_table["Mercury"] = {"name": "Mercury", "symbol": "Hg", "atomic_number": 80, "mass_number": 200.59}
periodic_table["Thallium"] = {"name": "Thallium", "symbol": "Tl", "atomic_number": 81, "mass_number": 204.38}
periodic_table["Lead"] = {"name": "Lead", "symbol": "Pb", "atomic_number": 82, "mass_number": 207.2}
periodic_table["Bismuth"] = {"name": "Bismuth", "symbol": "Bi", "atomic_number": 83, "mass_number": 208.98}
periodic_table["Polonium"] = {"name": "Polonium", "symbol": "Po", "atomic_number": 84, "mass_number": 209}
periodic_table["Astatine"] = {"name": "Astatine", "symbol": "At", "atomic_number": 85, "mass_number": 210}
periodic_table["Radon"] = {"name": "Radon", "symbol": "Rn", "atomic_number": 86, "mass_number": 222}
periodic_table["Francium"] = {"name": "Francium", "symbol": "Fr", "atomic_number": 87, "mass_number": 223}
periodic_table["Radium"] = {"name": "Radium", "symbol": "Ra", "atomic_number": 88, "mass_number": 226}
periodic_table["Actinium"] = {"name": "Actinium", "symbol": "Ac", "atomic_number": 89, "mass_number": 227}
periodic_table["Thorium"] = {"name": "Thorium", "symbol": "Th", "atomic_number": 90, "mass_number": 232.04}
periodic_table["Protactinium"] = {"name": "Protactinium", "symbol": "Pa", "atomic_number": 91, "mass_number": 231.04}
periodic_table["Uranium"] = {"name": "Uranium", "symbol": "U", "atomic_number": 92, "mass_number": 238.03}
periodic_table["Neptunium"] = {"name": "Neptunium", "symbol": "Np", "atomic_number": 93, "mass_number": 237}
periodic_table["Plutonium"] = {"name": "Plutonium", "symbol": "Pu", "atomic_number": 94, "mass_number": 244}
periodic_table["Americium"] = {"name": "Americium", "symbol": "Am", "atomic_number": 95, "mass_number": 243}
periodic_table["Curium"] = {"name": "Curium", "symbol": "Cm", "atomic_number": 96, "mass_number": 247}
periodic_table["Berkelium"] = {"name": "Berkelium", "symbol": "Bk", "atomic_number": 97, "mass_number": 247}
periodic_table["Californium"] = {"name": "Californium", "symbol": "Cf", "atomic_number": 98, "mass_number": 251}
periodic_table["Einsteinium"] = {"name": "Einsteinium", "symbol": "Es", "atomic_number": 99, "mass_number": 252}
periodic_table["Fermium"] = {"name": "Fermium", "symbol": "Fm", "atomic_number": 100, "mass_number": 257} ##
periodic_table["Mendelevium"] = {"name": "Mendelevium", "symbol": "Md", "atomic_number": 101, "mass_number": 258}
periodic_table["Nobelium"] = {"name": "Nobelium", "symbol": "No", "atomic_number": 102, "mass_number": 259}
periodic_table["Lawrencium"] = {"name": "Lawrencium", "symbol": "Lr", "atomic_number": 103, "mass_number": 262}
periodic_table["Rutherfordium"] = {"name": "Rutherfordium", "symbol": "Rf", "atomic_number": 104, "mass_number": 267}
periodic_table["Dubnium"] = {"name": "Dubnium", "symbol": "Db", "atomic_number": 105, "mass_number": 270}
periodic_table["Seaborgium"] = {"name": "Seaborgium", "symbol": "Sg", "atomic_number": 106, "mass_number": 271}
periodic_table["Bohrium"] = {"name": "Bohrium", "symbol": "Bh", "atomic_number": 107, "mass_number": 270}
periodic_table["Hassium"] = {"name": "Hassium", "symbol": "Hs", "atomic_number": 108, "mass_number": 277}
periodic_table["Meitnerium"] = {"name": "Meitnerium", "symbol": "Mt", "atomic_number": 109, "mass_number": 278}
periodic_table["Darmstadtium"] = {"name": "Darmstadtium", "symbol": "Ds", "atomic_number": 110, "mass_number": 281}
periodic_table["Roentgenium"] = {"name": "Roentgenium", "symbol": "Rg", "atomic_number": 111, "mass_number": 282}
periodic_table["Copernicium"] = {"name": "Copernicium", "symbol": "Cn", "atomic_number": 112, "mass_number": 285}
periodic_table["Nihonium"] = {"name": "Nihonium", "symbol": "Nh", "atomic_number": 113, "mass_number": 286}
periodic_table["Flerovium"] = {"name": "Flerovium", "symbol": "Fl", "atomic_number": 114, "mass_number": 289}
periodic_table["Moscovium"] = {"name": "Moscovium", "symbol": "Mc", "atomic_number": 115, "mass_number": 290}
periodic_table["Livermorium"] = {"name": "Livermorium", "symbol": "Lv", "atomic_number": 116, "mass_number": 293}
periodic_table["Tennessine"] = {"name": "Tennessine", "symbol": "Ts", "atomic_number": 117, "mass_number": 294}
periodic_table["Oganesson"] = {"name": "Oganesson", "symbol": "Og", "atomic_number": 118, "mass_number": 294}

# (1) Functions

def searchElement(): # Main Menu Option 1 - Element Search

    print("How Would You Like To Search?: ")
    print("\n")
    print("1. Name")
    print("2. Atomic Symbol")
    print("3. Atomic Number")
    print("4. Return To Menu")
    print("\n")
    searchChoice = int(input("Enter Selection: "))

    while searchChoice != 4:

        if searchChoice == 1: # search element by name

            print("\n")
            element_name = input("Enter The Name Of The Element: ")

            for item in periodic_table: # loops through periodic_table dictionary
                if periodic_table[element_name] == periodic_table[item]: # finds specific item with name being searched for
                    print("\n")
                    print("Element Name: ", periodic_table[element_name]["name"])
                    print("Element Symbol: ", periodic_table[element_name]["symbol"])
                    print("Atomic Number: ", periodic_table[element_name]["atomic_number"])
                    print("Mass Number: ", periodic_table[element_name]["mass_number"])
                    print("\n")
                    searchChoice = int(input("Would You Like To Search Another Element, Or Return To The Main Menu? Please Enter Selection: "))

        elif searchChoice == 2: # search element by element symbol

            print("\n")
            element_symbol = input("Enter The Symbol Of The Element: ")

            for item in periodic_table: # loops through periodic_table dictionary
                if element_symbol == periodic_table[item]["symbol"]: # finds specific item with name being searched for
                    print("\n")
                    print("Element Name: ", periodic_table[item]["name"])
                    print("Element Symbol: ", periodic_table[item]["symbol"])
                    print("Atomic Number: ", periodic_table[item]["atomic_number"])
                    print("Mass Number: ", periodic_table[item]["mass_number"])
                    print("\n")
                    searchChoice = int(input("Would You Like To Search Another Element, Or Return To The Main Menu? Please Enter Selection: "))
                    
        elif searchChoice == 3: # search element by atomic number

            print("\n")
            element_atomic_number = int(input("Enter The Atomic Number Of The Element: "))

            for item in periodic_table: # loops through periodic_table dictionary
                if element_atomic_number == periodic_table[item]["atomic_number"]: # finds specific item with name being searched for
                    print("\n")
                    print("Element Name: ", periodic_table[item]["name"])
                    print("Element Symbol: ", periodic_table[item]["symbol"])
                    print("Atomic Number: ", periodic_table[item]["atomic_number"])
                    print("Mass Number: ", periodic_table[item]["mass_number"])
                    print("\n")
                    searchChoice = int(input("Would You Like To Search Another Element, Or Return To The Main Menu? Please Enter Selection: "))

        else:
            searchChoice = int(input("Invalid Selection. Please Try Again."))
             

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
