# importing the needed libraries
from csv import writer, reader
from os import system, name
import re

# variables declared
# ...

######################
# table of content
# - clear
# - add_student
# - delete_student

def clear(): #defines out clear function
  # for windows
    if name == 'nt':
      _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
      _ = system('clear')  
## this function is just so that the below works, should move somewhere more sensible


def add_student():
  clear() #Clears the screen
  status = True
  print("\nAdding a new student") # Title
  while True:
    try:
      while status:
        name = input("Name: ") # Takes the name as the input
        if name[0].isupper(): # If the first character is in upper case, the program will not loop
          status = False #Exits the while loop
        else:
          print("Invalid name! Please try again.") # If the first character is in lower case, the program will prompt the user to input the name again
      age = int(input("Age: ")) # Takes the age as the input
      while status is False: 
        email = input("Email: ") # Takes the email address as the input
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if valid:
          status = True #If the email address is valid, the program will not loop.
        else:
          print("Invalid email address! Please try again.") # If the email address is invalid, the program will prompt the user to type it again
    except ValueError:
      print("Invalid input! Please try again.") # If the age is not an integer, the user has to type it in again
    else:
      mix = [name, age, email] # Creates a variable that puts the name, age and email address into a list
      with open('student.csv', 'a') as f_object: # Opens a file named student.csv in append mode
        writer_object = writer(f_object) # Defines the file that would be written to
        writer_object.writerow(mix) # Writes the student's information to the file
      print("Added successfully!\n") # Message that indicates that the information is added successfully
      break # Exits the loop


def delete_student():
  id = input("Input ID of student to be deleted")
  line_to_delete = 0 # at which line is the data located

  with open('students.csv', newline='') as data:
    # parse file
    table = reader(data, delimiter=',')

    # iterate until the right entry is found
    for row in table:
      if row[1] == id:
        print("we found the student!")
        break
      line_to_delete += 1
    else:
      print("student ID as inputted has not been found...")
  
  # now we delete the data
  lines = []
  with open("students.csv", "r") as f:
    lines = f.readlines()
  with open("students.csv", "w") as f:
    for number, line in enumerate(lines):
      if number != line_to_delete:
        f.write(line)

      
    
