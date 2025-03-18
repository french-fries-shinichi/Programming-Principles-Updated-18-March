from csv import writer, reader
from os import system, name

status = True

#################
# - clear
# - add_course
# - delete_course


def clear(): #defines out clear function
  # for windows
  if name == 'nt':
    _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
  else:
    _ = system('clear')


def add_course(): #Function for adding a course
  clear() #Clears the screen
  while True:
    try:
      
      while status:
        course_code = input("Insert the course code: ") #Takes the course code as an input
        if course_code[0].isupper() and len(course_code) != 3:
             print("Invalid input! Please try again.") #Loops until the input is valid
        else:
          break #Exits the loop
        
      while status:
        course_num = int(input("Insert the course number: ")) #Takes the course number as the input
        if str(course_num).isdigit() and len(str(course_num)) != 4:
          print("Invalid input! Please try again.") #Loops until the input is valid
        else:
          break #Exits the loop

      while status:    
        course_name = input("Insert the full course name ") #Takes the course name as the input from the user 
        if course_name.isalpha() and course_name[0].isupper(): #Checks the input to see if it only contains alphabets and the first letter is in uppercase
          break #Exits the loop
        else:
          print("Invalid input! Please try again.") #Loops again until the input is valid
    
    except ValueError:
      print("Invalid input! Please try again.") #Loops until the input is valid
    else:
      mix = [course_code, course_num, course_name, 30] #Variable that combines the course name, course number and seats available into a list
      with open('courses.csv', 'a') as object: #Opens the courses.csv file in append mode
        writer_object = writer(object) #Defines the file that will be written to
        writer_object.writerow(mix) #Writes mix into the file
      print("Added!") #Statement that shows the user the course is added
      break #Exits the loop


def delete_course():
  id = input("Input Course ID to be deleted")
  line_to_delete = 0 # at which line is the data located

  with open('courses.csv', newline='') as data:
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
  with open("courses.csv", "r") as f:
    lines = f.readlines()
  with open("courses.csv", "w") as f:
    for number, line in enumerate(lines):
      if number != line_to_delete:
        f.write(line)