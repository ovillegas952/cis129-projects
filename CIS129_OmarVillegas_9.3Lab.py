"""
Author: Omar Villegas

Professor: Troy Adams

Course: CIS129

Description: Program that allows a user to input student names and grades and saves it to a csv text file.
"""
#imports
import csv

import re

# function to prompt user to enter information and to start input validation
def get_student_grades():
    first_name =getValidName('What is the student\'s first name?: ')
    last_name = getValidName('What is the student\'s last name?: ')
    exam_1 = get_valid_int('What grade did the student get for exam 1?: ')
    exam_2 = get_valid_int('What grade did the student get for exam 2?: ')
    exam_3 = get_valid_int('What grade did the student get for exam 3?: ')

    return [first_name, last_name, exam_1, exam_2, exam_3]

# input validation function for user entering first and last name
def getValidName(prompt):
    to_return = input(prompt)
    while not checkValidName(to_return):
        to_return = input('Please enter a name using only letters and with the first letter capitalized: ')
    return to_return
# input validation function that checks if input is all letters
def checkValidName(name_to_check):
    success = False
    try:
        success = True if re.match('^[A-Z][a-zA-Z]*$', name_to_check) else False
    except TypeError:
        print("Please enter a word, not a number: ")
    return success
# input validation function that checks for 
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
def get_valid_int(prompt, min_value=0, max_value=100):
    to_return = get_int(prompt)
    while min_value >= to_return or max_value <= to_return:
        to_return = get_int(f'The value you entered is not included in the grading range, please enter a number between {min_value} and {max_value}: ')
        
    return to_return
# input function that prompts user to enter grades
student_input = input('Would you like to enter a student\'s name and grade? type yes or type -1 if not: ')
with open('grades.csv', 'w') as grades_csv: # opens and stores name and grades into csv file
    while student_input != '-1':
        student_info = get_student_grades()
        writer = csv.writer(grades_csv)
        writer.writerow(student_info)
        student_input = input('Would you like to enter another student\'s name and grade? type yes or type -1 if not: ')
