import os
import student, course, enrollment
from table import table_view,view_List, edit_list, confirm_edit
#from editlistfunction import edit_list

should_exit = False
'''
def drop_course_m1():
  delete_row_from_db(seats=50) #just added this to assign a seat variable (can remove this comment later)
'''
def pause():
  os.system("pause")

os.system("clear")
print("\n    French Fries Software Solutions co. unlimited presents:")
print("""
   _____                            _____            _     _             _   _             
  / ____|                          |  __ \\          (_)   | |           | | (_)            
 | |     ___  _   _ _ __ ___  ___  | |__) |___  __ _ _ ___| |_ _ __ __ _| |_ _  ___  _ __  
 | |    / _ \\| | | | '__/ __|/ _ \\ |  _  // _ \\/ _` | / __| __| '__/ _` | __| |/ _ \\| '_ \\ 
 | |___| (_) | |_| | |  \\__ \\  __/ | | \\ \\  __/ (_| | \\__ \\ |_| | | (_| | |_| | (_) | | | |
  \\_____\\___/ \\__,_|_|  |___/\\___| |_|  \\_\\___|\\__, |_|___/\\__|_|  \\__,_|\\__|_|\\___/|_| |_|
  / ____|         | |                           __/ |                                      
 | (___  _   _ ___| |_ ___ _ __ ___            |___/                                       
  \\___ \\| | | / __| __/ _ \\ '_ ` _ \\                                                       
  ____) | |_| \\__ \\ ||  __/ | | | | |                                                      
 |_____/ \\__, |___/\\__\\___|_| |_| |_|                                                      
          __/ |                                                                            
         |___/  
""")
while not should_exit:
  print("""  +-- Main Menu ---------------------+
  |                                  |
  | select one of these options:     |
  |  1 - Add a new student           |
  |  2 - Add a new course            |
  |  3 - Enrol a student in a course |
  |  4 - delete a student            |
  |  5 - delete a course             |
  |  6 - Drop a course               |
  |  7 - View available courses      |
  |  8 - View Student information    |
  |  9 - edit one of the students    |
  | 10 - edit one of the courses     |  
  | 11 - Exit                        |
  +----------------------------------+
  """)
  try:
    c = int(input(">  "))
  except ValueError:
    print("The input wasn't a whole number!\n")
  else:
    match c:
      case 1:
        student.add_student()
        pause()
      case 2:
        course.add_course()
        pause()
      case 3:
        enrollment.enroll()
        pause()
      case 4:
        student.delete_student()
      case 5:
        course.delete_course()
      case 6:
        enrollment.drop_course()
        
      case 7:
        filename = 'courses.csv'
        '''
        columns, headers, data = view_List(filename)
        table_view(columns, headers, data)
        pause() #should_exit = True #instead of exiting and forcing the end-user (ie an admin) to restart the program, just pause to see
      '''
      case 8:
        filename = 'student.csv'
        columns, headers, data = view_List(filename)
        table_view(columns, headers, data)
        pause() #should_exit = True #instead of exiting and forcing the end-user (ie an admin) to restart the program, just pause to see
      case 9:
        columns, headers, data = view_List('student.csv') # Accesses the data from view list function
        table_view(columns, headers, data)   # Runs the view table function
        confirm_edit(headers, data, 'student.csv')  # Runs the edit option function
        edit_list()
      case 10:
        pass
      case 11:
        print("Exiting program...")
        should_exit = True
      case _:
        print(
            "The number given doesn't match any of the actions listed, please type a number between 1-7"
        )
