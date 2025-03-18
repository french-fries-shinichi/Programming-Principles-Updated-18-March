import csv

# Start of Main Function (Global Variable)
def drop_course():  #define function for reusability
  status = True #assign a statement for True/False value jumps
  try:
    while status:
      print('\n+------Dropping a course-------+')
      course = input('Course code (e.g. MAT): ')  #input: course code
      if course[0].isupper() and len(course) == 3:
        break #exit current loop when course input is validated
      else:
        print('Invalid course code! Please try again.')

    while status:
      coursenum = input("Course number (e.g. 1217): ")  #input: course number
      available_seats = 30 #default seats: 30
      if coursenum.isdigit() and len(coursenum) == 4:
        break #exit current loop when number input is validated
      else:
        print("Invalid input! Please enter a valid 4-digit number")
    
    while status:
      course_subject = input('Input the full subject name: ')
      if course_subject.isalpha() and course_subject[0].isupper(): #Checks the input to see if it only contains alphabets and the first letter is in uppercase
        break
      else:
        print("Invalid subject input! Please try again.")
        #calls back the function for seat incrementation stored in a local variable
    if (course, coursenum, course_subject):
      course_drop = increment_seats(course, coursenum, course_subject, available_seats) #returns the function for reusability
      print("\nCourse dropped successfully!")
      print("+----------------------------+")
      
    else:
      print("Invalid input! Please try again") #exits current loop once course subject is validated and function was executed without any errors
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