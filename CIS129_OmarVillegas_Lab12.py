"""
Author: Omar Villegas

Professor: Troy Adams

Course: CIS129

Description: Program based on OOP that creates a pet class, stores and recieves information entered, then displays it to the user upon input.
"""

# imports for input validation
import re

# main
def main():
    pet_name = getValidName('What is the name of your pet?: ')
    pet_type = getValidName('What is the type of pet you have?: ')
    pet_age = get_valid_int('What is the age of your pet?: ')


    Animal = Pet(pet_name, pet_type, pet_age)

    print("Your pet's name is:" , Animal.get_name())
    print("Your pet's type is:" , Animal.get_type())
    print("Your pet's age is:" , Animal.get_age())

    Animal.set_age("")

    print(Animal.get_age())

# Class creation
class Pet:
    def __init__(self,name,type,age):
        self.__name = name
        self.__type = type
        self.__age = age

    def set_name(self,new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name
    
    def set_type(self,new_type):
        self.__name = new_type

    def get_type(self):
        return self.__type
    
    def set_age(self,new_age):
        self.__age = new_age

    def get_age(self):
        return self.__age

 #input validation for word prompts   
def getValidName(prompt):
    to_return = input(prompt)
    while not checkValidName(to_return):
        to_return = input('Please enter a word using only letters: ')
    return to_return
# Input validation in case a number is entered instead of word
def checkValidName(name_to_check):
    success = False
    try:
        success = True if re.match('^[a-zA-Z]*$', name_to_check) and len(name_to_check) != 0 else False
    except TypeError:
        print("Please enter a word, not a number: ")
    return success

# input validation function that checks for an integer input
def get_int(prompt):
    to_return = input(prompt)
    is_number = False
    while not is_number:
        try:
            to_return = int(to_return)
            is_number = True
        except ValueError:
            to_return = input('Please enter a whole number, not a word, letter, or number with a decimal: ')
            is_number = False
    return to_return

# input validation function to ensure number entered is in a valid range 
def get_valid_int(prompt, min_value=0, max_value=200):
    to_return = get_int(prompt)
    while min_value >= to_return or max_value <= to_return:
        to_return = get_int(f'The value you entered is not in the age range, please enter a number between {min_value} and {max_value}: ')
    return to_return
# main function call
main()
