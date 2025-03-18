import csv
 
def table_view(columns, headers, data):
  formated_headers = []
  formated_data = []

#This segment calculates the max width of each column
  max_width_of_column = []
  for column in columns:  # Iterates between columns
      max_value = 0
      for i in column:  # Iterates between data within the columns
          if len(i) > max_value:  # Tests if the data is larger than max value
              max_value = len(i)  # Updates the max width of data
      max_width_of_column.append(max_value) # Adds the max data width of each column into a list

# This segment produces the formatted header of the table
  header_with_width = zip(headers, max_width_of_column) # Combines the header with its respective max width
  for header, width in header_with_width:  # Iterates between headers
      formated_headers.append(header.ljust(width))  # Produces the format and adds it into the list
  header_row = " | ".join(formated_headers) # Combines columns
  print(header_row)
  print("-" * len(header_row))

# This segment produces the formatted data of the table
  for row in data:  # Iterates between each row of data
    formated_row = [] # Reset the formatted_row list for each row
    for item,width in zip(row, max_width_of_column):  # Combines the row with its respective max width
        formated_row.append(item.ljust(width))  # Iterates between the two elements into item[] and width[]
    data_row = " | ".join(formated_row)   # Produces the format and adds it into the list
    print(data_row)
  print("-" * len(data_row)) 

#This segment reads the file and segregates it into headers,data and columns
def view_List(filename):
    try:
        with open(f'{filename}', 'r') as file: 
            fileReader = csv.reader(file)
            headers = next(fileReader)  # Reads the first row of values into headers
            data_in_file = list(fileReader)  # Read the remaining row
            columns = list(zip(headers, *data_in_file))  # Combine each element into a column instead of a row
            return columns, headers, data_in_file
    except FileNotFoundError:  # Handles if File Not Found Error
        print("Error! File not found")