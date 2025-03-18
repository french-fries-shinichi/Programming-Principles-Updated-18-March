# table.py is both for viewing and editing data sets
# since both view_* functions and edit_* functions
# displays the entire file as a table and then prompts
# user to input choice. it is unique and unambigous enough
# as a file name (idk why im explaining my thought
# process)

import csv

###########
# - table_view(columns, headers, data)
# - view_list(filename)
# - edit_list(data, header, file_name)


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


# def edit_list(data, header, file_name):
#     quit_option = False
#     try:
#         # This segment receives the users input of the row they wish to edit
#         status = True
#         while status:
#             try:
#                 row_index = input("Please enter the row number of the data you wish to edit: ")
#                 if row_index <= 0 or row_index > len(data): # Ensures that the row selected exists
#                     print(
#                         f"Error! Please input a column number between 1 and {len(data)}")
#                     print()
#                 elif row_index.upper == 'QUIT':
#                     print("Are you sure you want to quit?[Y][N]")
#                     confirm = input()
#                     if confirm.upper == 'Y':
#                         print
#                 else:
#                     print(f"Row number selected: {row_index}")  # Prints the row index selected
#                     status = False
#             except ValueError:  # 
#                 print("Invalid input! Please enter an integer")

#         print()
#         count = 1
#         print("Available Columns: ")
#         for i in header:
#             print(f"{count}. {i}")
#             count += 1

#         while status != True:
#             try:
#                 column_index = int(
#                     input("Please enter the column number of the data you wish to edit:"))
#                 if column_index < 0 or column_index > len(header):
#                     print("Error! Please enter a column that exists")
#                 else:
#                     print(f"Column number selected: {column_index}")
#                     status = True
#             except ValueError:
#                 print("Invalid input! Please enter an integer")

#         print(f"You have selected {data[row_index - 1][column_index - 1]}")
#         new_value = input(f"Please enter the new value: ")
#         data[row_index - 1][column_index - 1] = new_value

#         with open(f'{file_name}', 'w') as file:
#             writer = csv.writer(file)
#             writer.writerow(header)
#             writer.writerows(data)

#             print("\nData updated successfully!")
#             print("\nUpdated Data:")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# import csv


def confirm_edit(headers,data,filename):
    
    inputcheck = True
    while inputcheck:
        changes = input("Do you wish to make changes to the data?[Y][N]: ")
        if changes.upper() == 'Y':
            edit_list(headers, data, filename)
            inputcheck = False
        elif changes.upper() == 'N':
            print()
            print("Returning to main menu...")
            inputcheck = False
        else:
            print("Please enter either Y or N")


def edit_list(header, data, file_name):
    # This segment receives the users input of the row they wish to edit
    try:
        status = True
        while status == True:
            try:
                row_input = input(
                    "Please enter the row number of the data you wish to edit (or enter 'Quit' to exit): ")

                # This segment provides user the option to quit
                if row_input.upper() == 'QUIT':
                    confirm = input(
                        "Are you sure you want to quit? [Y/N]: ").upper()
                    if confirm == 'Y':
                        print()
                        print("Returning to main menu...")
                        print()
                        return  # Exit the function
                    else:
                        continue

                row_index = int(row_input)
                # Ensures that the row selected exists
                if row_index <= 0 or row_index > len(data):
                    print(
                        f"Error! Please input a column number between 1 and {len(data)}")
                    print()
                else:
                    # Prints the row index selected
                    print(f"Row number selected: {row_index}")
                    status = False
            except ValueError:  #
                print("Invalid input! Please enter an integer")

        print()
        count = 1
        print("Available Columns: ")
        for i in header:
            print(f"{count}. {i}")
            count += 1
        print()

        status2 = True
        while status2 == True:
            try:
                column_input = input(
                    "Please enter the column number of the data you wish to edit (or enter 'Quit' to exit):")

                if column_input.upper() == "QUIT":
                    confirm = input("Are you sure you want to quit? [Y/N]: ")
                    if confirm.upper() == 'Y':
                        print()
                        print("Returning to main menu...")
                        print()
                        return
                    else:
                        continue

                column_index = int(column_input)
                if column_index <= 0 or column_index > len(header):
                    print("Error! Please enter a column that exists")
                else:
                    print(f"Column selected: {header[column_index - 1]}")
                    status2 = False
            except ValueError:
                print("Invalid input! Please enter an integer")

        print(f"The data selected: {data[row_index - 1][column_index - 1]}")
        new_value = input(f"Please enter the new value: ")
        data[row_index - 1][column_index - 1] = new_value

        with open(f'{file_name}', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

            print("\nData updated successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")