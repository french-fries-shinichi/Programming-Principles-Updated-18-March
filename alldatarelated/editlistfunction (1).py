     
#Code:
import sys #sys --> extra functionality for exit command systems
from csv import writer #import the writer functionality

def input_course_abbreviation_validate():
  course = input('Please enter a course code (e.g. MAT): ')  #input: course code
  if course[0].isupper():
    return course # i will explain this
  else:
    print('Invalid course code! Please try again.') 

def input_course_code():
  course_num = input("Please enter relevant course number (e.g. if MAT, then 1217): ")  #input: course number
  if course_num.isdigit():
    return course_num
  else:
    print("Invalid course number! Please try again.")  #prints when course number input is invalid

def delete_row_from_db(course, course_num):
  try:
    with open('enrolments.csv','w') as fw:  #opens the storage in the database
      ptr = 1  #set pointer = 1
      lines = fw.readlines()
      for line in lines:  #for every line
         if ptr != 5:
           fw.write(line)
         ptr += 1  #increment pointer += 1
    print(f"Removed the course: {course}{course_num}.")

  except FileNotFoundError:
    print("The database 'enrolments.csv' does not exist.")

def drop_course_m():
  course_letters = input_course_abbreviation_validate()
  course_numbers = input_course_code()
  delete_row_from_db(course_letters, course_numbers)