# fig03_02.py
"""Class average program with sentinel-controlled iteration."""

# function to ensure proper integer input validation
def get_int(prompt):
    to_return = input(prompt)
    is_number = False
    while not is_number:
        try:
            to_return = int(to_return)
            is_number = True
        except ValueError:
            to_return = input('Please enter a number, not a word or letter: ')
            is_number = False
    return to_return
# input validation function to ensure number entered is in a valid range 
def get_valid_int(prompt, min_value, max_value, sentinel_value):
    to_return = get_int(prompt)
    while min_value >= to_return or max_value <= to_return:
        if to_return == sentinel_value:
            break
        to_return = get_int(f'The value you entered is not included in the grading range, please enter a number between {min_value} and {max_value}: ')
        
    return to_return

# initialize variables
total = 0  # sum of grades
grade_counter = 0 # number of grades entered

# processing phase
grade = get_valid_int('Enter grade, -1 to end: ', 0, 100, -1)  # get one grade

grades_file = open('grades.txt', 'w')

while grade != -1:
    total += grade
    grade_counter += 1
    grades_file.write(str(grade) + '\n')
    grade = int(input('Enter grade, -1 to end: '))

 # termination phase
if grade_counter != 0:
    average = total / grade_counter
    print(f'Class average is {average:.2f}')
else:
    print('No grades were entered')
grades_file.close()
