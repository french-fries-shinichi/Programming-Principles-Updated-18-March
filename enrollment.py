from csv import writer, DictWriter, DictReader
import csv #so redundant
import datetime
namelist = []
courselist = []

#######
# notice: i removed 'csv.' from 'csv.reader()' to make the code
#   nicer to read
###############
# - enroll
# - drop_course

def enroll():
  status = True
  findname = False
  print("Enroll Students")

  while status is True:
    while True:
      name = input("Insert student's name: ")
      if name[0].isupper():
        break
      else:
        print("Invalid input! Please try again.")

    while True:
      student_id = input("Insert student ID: ")
      if len(student_id) == 5:
        break
      else:
        print("Invalid input! Please try again.")

    with open('students.csv', "r") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if name == row[2] and student_id == row[1]:
          status = False
          break
        line_count += 1
      
    if status is True:
      print("Invalid name and student ID! Please try again.")
  
  print()
  with open("courses.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      if line_count == 0:
        courselist.append([row[1], row[2], row[3]])
        line_count += 1
      else:
        courselist.append([row[1], row[2], row[3]])
        print(str(line_count) + '. ' + row[3])
        line_count += 1
  
  with open('enrollments.csv') as index_obj:
    csv_reader = csv.reader(index_obj, delimiter=',')
    count = 0
    for row in csv_reader:
      count += 1

  choice = int(input("Select a course (Insert a number only): "))
  print("Name:", name, "\nCourse selected:", courselist[choice][2], "\nCourse code: ", courselist[choice][0], "\nCourse ID: ", courselist[choice][1])
  x = datetime.datetime.now()
  mix = [int(count), student_id, courselist[choice][0], courselist[choice][1], x.strftime("%x")]
  with open('enrolments.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(mix)


def drop_course():  #define function for reusability
  status = True #assign a statement for True/False value jumps
  try:
    while status:
      print('\n+------Dropping a course-------+')
      course_code = input('Insert the course code (e.g. MAT): ')  #input: course code
      if len(course_code) == 3:
        
        course_num = input("Insert the course number (e.g. 1217): ")  #input: course number
        if course_num.isdigit() and len(course_num) == 4:
          course_name = input('Insert the full course name: ') #input: course name
          if course_name[0].isupper() and course_name.isalpha():
            
            available_seats = 30 #default seats: 30

            #calls back the function for seat incrementation stored in a local variable
            course_drop = increment_seats(course_code, course_num, course_name, available_seats) #returns the function for reusability
            if course_drop is True:
              print("\nCourse dropped successfully!") # when course_drop was a success
              print("+----------------------------+")
              break
            else: #if not, leave an error and exit the looping process
              print("Course is not found or does not exist. Please try again.")
          else:
            print("Invalid input! Please try again") #exits current loop once course subject is validated and function was executed without any errors
            return False #return False and exit current loop
        else:
          print("Invalid input! Please enter a valid 4-digit number")
          return False #return False and exit current loop
      
      
  except TypeError or FileNotFoundError as e: #Error: inappropriate object type or unknown file error
    print(f"Unknown error. File not found or object type undefined for {e}")

# Local Variable to store seats
def increment_seats(course_code, course_num, course_name):
    course_drop = True  # Assuming True means we are dropping a course
    if course_drop:
        increment = 1  # Set increment variable to add +1 seat condition
        try:
            # Open the CSV file in read mode
            with open('courses.csv', 'r', newline='') as csvfile:
                csvreader = DictReader(csvfile)  # Read CSV into a dictionary
                rows = list(csvreader)  # Convert the CSV rows into a list for modification
                course_found = False #set a new condition for if course found is False
                
                for row in rows: #Open up the rows for iteration editing
                    if row['course_code'] == course_code and row['course_num'] == course_num and row['course_name'] == course_name:
                        # If a match is found, increment the available seats
                        row['available_seats'] = str(int(row['available_seats']) + increment)
                        course_found = True
                        break  # Exit the loop and jump to course_found is True
                    else:
                      print('Invalid input! Course not found')
                      return False     
                if not course_found:
                    # If course is not found, print an error message
                    print(f"An error has occurred. The course {course_code}{course_num} cannot be found.")
                    return False  # Exit the function if course is not found

            # If the seats were updated, write the changes back to the file
            if course_found:
                with open('courses.csv', 'w', newline='') as csvfile:
                    fieldnames = ['course_code', 'course_num', 'course_name', 'available_seats']
                    csvwriter = DictWriter(csvfile, fieldnames=fieldnames)
                    csvwriter.writeheader()  # Write the header to the file
                    csvwriter.writerows(rows)  # Write the modified rows back to the CSV file
                    print("Dropping the selected course...")  # Output buffer

        except ValueError as e:
            print(f"Error for: {e}")
            return False  # If there was an error with reading/writing the file, return False

    return course_drop  # True --> if the course was successfully dropped