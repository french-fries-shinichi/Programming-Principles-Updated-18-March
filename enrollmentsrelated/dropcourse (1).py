'''
import csv
import sys

# Start of Main Function (Global Variable)
def drop_course():  # Define function for reusability
    status = True
    try:
        while status:
            print('\n+------Dropping a course-------+')
            course = input('Course code (e.g. MAT): ')  # input: course code
            if course.isalpha() and len(course) == 3:
                  # set status default: False
                  coursenum = input("Course number (e.g. 1217): ")  # input: course number
                  available_seats = 30
                  if coursenum.isdigit() and len(coursenum) == 4 and course.isalpha() and len(course) == 3:
                    status = True  # set status to True
                    # Now calling increment_seats function
                    course_drop = increment_seats(course, coursenum, available_seats)
                    if course_drop:
                      print('\nYour course has been dropped successfully!')  # drops the course if successful
                      print('+-----------------------------+')
                    else:
                      print(f"Error: Course {course}{coursenum} not found in the system.")
                  else:
                    print('\nInvalid course code! Please try again.')

        
            
            else:
              print("\nInvalid input. Please enter a valid 4-digit number: ")
    except (TypeError, FileNotFoundError) as e:  # Error: inappropriate object type or unknown file error
        print("\nInvalid input! Please enter a valid course code with number and try again.")


# Local Variable to store seats
def increment_seats(course, coursenum, available_seats):
    course_drop = True
    if course_drop:
        increment = 1  # Increment the available seats (drop the course logic)
        try:
            with open('courses.csv', 'r', newline='') as csvfile:  # Opens the csv file in read-mode
                csvreader = csv.DictReader(csvfile)  # Read the CSV content
                rows = list(csvreader)  # Forms a list to store rows that are modifiable

            course_found = False
            # Debugging: print course and coursenum before checking
            print(f"Looking for course {course} with course number {coursenum}...")
            
            for row in rows:
                if row['course'] == course and row['coursenum'] == coursenum:  # Checks course name and number match
                    print(f"Found matching course: {row}")  # Debugging: print matching course
                    row['available_seats'] = str(int(row['available_seats']) + increment)  # Increment seats
                    course_found = True
                    break  # Exits the loop (course was found)

            if course_found:
                with open('courses.csv', 'w', newline='') as csvfile:
                    fieldnames = ['course', 'coursenum', 'available_seats']
                    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames) 
                    csvwriter.writeheader()  # Write the header
                    csvwriter.writerows(rows)  # Write the updated rows
                print("Dropping the selected course...")  # output buffer
            else:
                print(f"\nAn error has occurred. Course {course},{coursenum} cannot be found.")
                return False  # Return False if course is not found

        except Exception as e:
            print(f"Error: {e}")
            return False  # Return False if there's any error with reading/writing the file

   
    return course_drop  # Return True if the course is successfully processed
    '''


import csv

# Start of Main Function (Global Variable)
def addcourse():  #define function for reusability
  status = True #assign a statement for True/False value jumps
  try:
    while status:
      print('\n+------Dropping a course-------+')
      course = input('Inset the course code (e.g. MAT): ')  #input: course code
      if course[0].isupper() and len(course) == 3:
        #exit current loop when course input is validated
        coursenum = input("Insert the course number (e.g. 1217): ")  #input: course number
        if coursenum.isdigit() and len(coursenum) == 4:
          course_subject = input('Insert the full course name: ')
          if course_subject[0].isupper() and course_subject.isalpha(): #Checks the input to see if it only contains alphabets and the first letter is in uppercase
            #calls back the function for seat incrementation stored in a local variable
            available_seats = 30 #default seats: 30
            course_drop = increment_seats(course, coursenum, course_subject, available_seats) #returns the function for reusability
            print("\nCourse dropped successfully!")
            print("+----------------------------+")
            break
          else:
            print("Invalid input! Please try again") #exits current loop once course subject is validated and function was executed without any errors
            return False
         #exit current loop when number input is validated
        else:
          print("Invalid input! Please enter a valid 4-digit number")
          return False
      
      
  except TypeError or FileNotFoundError: #Error: inappropriate object type or unknown file error
    print("Unknown error. File not found or object type undefined.")


# Local Variable to store seats
def increment_seats(course, coursenum, course_subject, available_seats):
    course_drop = True  # Assuming True means we are dropping a course
    if course_drop:
        increment = 1  # Set increment variable to add +1 seat condition
        try:
            # Open the CSV file in read mode
            with open('courses.csv', 'r', newline='') as csvfile:
                csvreader = csv.DictReader(csvfile)  # Read CSV into a dictionary
                rows = list(csvreader)  # Convert the CSV rows into a list for modification
                course_found = False  # Track whether the course was found
                
                # Iterate through the rows to find the matching course
                for row in rows:
                    if row['course'] == course and row['coursenum'] == coursenum and row['course_subject'] == course_subject:
                        # If a match is found, increment the available seats
                        row['available_seats'] = str(int(row['available_seats']) + increment)
                        course_found = True
                        break  # Exit the loop as we found the course
                    else:
                      print('Invalid input! Course not found')
                      return False    
                if not course_found:
                    # If course is not found, print an error message
                    print(f"An error has occurred. The course {course} {coursenum} cannot be found.")
                    return False  # Exit the function if course is not found

            # If the course was found and the seats updated, write the changes back to the file
            if course_found:
                with open('courses.csv', 'w', newline='') as csvfile:
                    # Assuming that 'coursenum', 'course_subject', and 'available_seats' are the columns in your CSV
                    fieldnames = ['course', 'coursenum', 'course_subject', 'available_seats']
                    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    csvwriter.writeheader()  # Write the header to the file
                    csvwriter.writerows(rows)  # Write the modified rows back to the CSV file
                    print("Dropping the selected course...")  # Output buffer after updating

        except ValueError as e:
            print(f"Error for: {e}")
            return False  # If there was an error with reading/writing the file, return False

    return course_drop  # True --> if the course is successfully processed