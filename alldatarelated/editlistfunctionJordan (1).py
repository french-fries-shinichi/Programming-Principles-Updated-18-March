import csv

def edit_list(data, header, file_name):
    quit_option = False
    try:
        # This segment receives the users input of the row they wish to edit
        status = True
        while status:
            try:
                row_index = input("Please enter the row number of the data you wish to edit: ")
                if row_index <= 0 or row_index > len(data): # Ensures that the row selected exists
                    print(
                        f"Error! Please input a column number between 1 and {len(data)}")
                    print()
                elif row_index.upper == 'QUIT':
                    print("Are you sure you want to quit?[Y][N]")
                    confirm = input()
                    if confirm.upper == 'Y':
                        print
                else:
                    print(f"Row number selected: {row_index}")  # Prints the row index selected
                    status = False
            except ValueError:  # 
                print("Invalid input! Please enter an integer")

        print()
        count = 1
        print("Available Columns: ")
        for i in header:
            print(f"{count}. {i}")
            count += 1

        while status != True:
            try:
                column_index = int(
                    input("Please enter the column number of the data you wish to edit:"))
                if column_index < 0 or column_index > len(header):
                    print("Error! Please enter a column that exists")
                else:
                    print(f"Column number selected: {column_index}")
                    status = True
            except ValueError:
                print("Invalid input! Please enter an integer")

        print(f"You have selected {data[row_index - 1][column_index - 1]}")
        new_value = input(f"Please enter the new value: ")
        data[row_index - 1][column_index - 1] = new_value

        with open(f'{file_name}', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

            print("\nData updated successfully!")
            print("\nUpdated Data:")

    except Exception as e:
        print(f"An error occurred: {e}")