# fig03_02.py 9.1 exercise
"""Class average program with sentinel-controlled iteration."""

# initialization phase
total = 0  # sum of grades
grade_counter = 0 # number of grades entered

# processing phase
grade = int(input('Enter grade, -1 to end: '))  # get one grade
# creates grades text file 
grades_file = open('grades.txt', 'w')

while grade != -1:
    total += grade
    grade_counter += 1
    grades_file.write(str(grade) + '\n') # saves grades to text file
    grade = int(input('Enter grade, -1 to end: '))

 # termination phase
if grade_counter != 0:
    average = total / grade_counter
    print(f'Class average is {average:.2f}')
else:
    print('No grades were entered')
grades_file.close() # closes grades text file
