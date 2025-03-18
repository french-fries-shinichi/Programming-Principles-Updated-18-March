import csv
from csv import writer

namelist = []
courselist = []

def enroll():
  status = True
  print("Enroll Students")
  while status is True:
    name = input("Insert student's name: ")
    with open('student.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if name == row[0]:
          status = False
          break
        line_count += 1
    if status is True:
      print("Invalid student's name! Please try again.")
    
  with open('courses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      courselist.append(row[2])
      print(str(line_count + 1) + '. ' + row[2])
      line_count += 1
    
  choice = int(input("Select a course (Insert a number only): "))
  print("Name:", name, "\nCourse selected:", courselist[choice - 1], "\nCourse ID", )
  mix = [name, courselist[choice - 1]]
  with open('enrolments.csv', 'a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(mix)