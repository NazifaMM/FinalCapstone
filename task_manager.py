# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        while True:
            new_username = input("New Username: ")
            with open('user.txt','r') as file:
                existing_username = [line.split(';')[0] for line in file.readlines()]
            if new_username in existing_username:
                print("Username exists, please input another.")
            else:
                break

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

    elif menu == 'a':
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")


    elif menu == 'va':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        for t in task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            


    elif menu == 'vm':
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        task_number = 1 # Initialise counter for task number 
        for t in task_list:
            if t['username'] == curr_user:
                disp_str = f"Task {task_number}:\n"
                disp_str = f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n {t['description']}\n"
                print(disp_str)
                task_number += 1  # Increment task number after displaying each task

        # Prompt user to select a task or return back to main menu 
            
        while True:
            user_selection = input("Input which number task would you like to view or enter -1 to return to main menu")
            
            if user_selection == "-1" :  # User selects -1 to return back to main menu
                break
            
            elif int(user_selection) >= 1 : # User selects a task 
                task_index = int(user_selection) - 1  # Convert user input to task index (subtract 1 for zero-based indexing)
                selected_task = task_list[task_index]
                # Display selected task details
                print(f"You selected Task {task_index + 1}:\n")
                print(f"Title: \t\t {selected_task['title']}")
                print(f"Assigned to: \t {selected_task['username']}")
                print(f"Date Assigned: \t {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
                print(f"Due Date: \t {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
                print(f"Task Description: \n {selected_task['description']}")
                
                # Prompt user to either mark the task complete or edit the task
                complete = input(" Would you like to mark this task complete, Yes or No ?")
                if complete == 'yes'.lower():
                    selected_task['Completed'] = True
                    print("Task has been marked completed")
                
                elif complete == 'no'.lower():
                    # Prompt if user would like to edit the task or return back to main menu
                    edit = input(" Enter 'edit' if you want to edit this task or -1 to return to main menu")
                    # If user choses edit 
                    if edit == 'edit'.lower():
                        edit_choice = input(" Enter 'date' to edit due date or 'assign' to edit the assigned user. ")
                        
                        # Editing due date 
                        if edit_choice == 'date'.lower():
                            new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                            try:
                                selected_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                                print("Due date updated successfully.")
                            except ValueError:
                               print("Invalid date format. Please use the format YYYY-MM-DD.")
                        
                        # Editing assigned user
                        elif edit_choice == 'assigned'.lower():
                            new_assigned_person = input("Enter the username of the new assigned person: ")
                            if new_assigned_person in username_password.keys():
                                selected_task['username'] = new_assigned_person
                                print("Assigned person updated successfully.")

                            else: 
                                print("Username does not exit, please enter valid username")
                        
                        elif edit_choice == -1:
                            break # break the loop and return back to main menu
                    
                else:
                    print("Invalid input, please enter the correct corresponding number")

    elif menu == 'gr':

        # # # Generate task overview 
            
        # Function to calculate total tasks
        def total_tasks(tasks):
           return len(tasks)

        # Function to calculate completed tasks
        def completed_tasks(tasks):
            return sum(1 for task in tasks if task['completed'])

        # Function to calculate incomplete tasks
        def incomplete_tasks(tasks):
            return total_tasks(tasks) - completed_tasks(tasks)

       # Function to calculate overdue tasks
        def overdue_tasks(tasks):
            from datetime import datetime
            now = datetime.now()
            return sum(1 for task in tasks if not task['completed'] and task['due_date'] < now)

        # Function to calculate percentage of incomplete tasks
        def percentage_incomplete_tasks(tasks):
            if total_tasks(tasks) == 0:
              return 0
            return (incomplete_tasks(tasks) / total_tasks(tasks)) * 100

        # Function to calculate percentage of overdue tasks
        def percentage_overdue_tasks(tasks):
            if total_tasks(tasks) == 0:
              return 0
            return (overdue_tasks(tasks) / total_tasks(tasks)) * 100
        
    
        # Function to generate task overview report
        def generate_task_overview_report(tasks):
            try:
                with open('task_overview.txt', 'w') as file:
                    file.write("Task Overview\n")
                    file.write("-------------\n")
                    file.write(f"Total Number of Tasks: {total_tasks(tasks)}\n")
                    file.write(f"Total Number of Completed Tasks: {completed_tasks(tasks)}\n")
                    file.write(f"Total Number of Incomplete Tasks: {incomplete_tasks(tasks)}\n")
                    file.write(f"Total Number of Overdue Tasks: {overdue_tasks(tasks)}\n")
                    file.write(f"Percentage of Incomplete Tasks: {percentage_incomplete_tasks(tasks):.2f}%\n")
                    file.write(f"Percentage of Overdue Tasks: {percentage_overdue_tasks(tasks):.2f}%\n")
            except Exception as e:
                print(f"An error has occured whilst generating the Task overview report")
        

        # # # Generating user overview
        
        def generate_user_overview_report(username_password, task_list):
            try:
                with open('user_overview.txt', 'w') as file:
                    file.write("User Overview\n")
                    file.write("-------------\n")
                    file.write(f"Total Number of Users: {len(username_password)}\n")
                    file.write(f"Total Number of Tasks: {len(task_list)}\n")

                    for username in username_password.keys():
                        num_tasks_assigned = sum(1 for task in task_list if task['username'] == username)
                        num_completed_tasks = sum(1 for task in task_list if task['username'] == username and task['completed'])
                        percentage_completed_tasks = (num_completed_tasks / num_tasks_assigned) * 100 if num_tasks_assigned != 0 else 0

                        file.write(f"\nUser: {username}\n")
                        file.write(f"Total Number of Tasks Assigned: {num_tasks_assigned}\n")
                        file.write(f"Total Number of Completed Tasks: {num_completed_tasks}\n")
                        file.write(f"Percentage of Completed Tasks: {percentage_completed_tasks:.2f}%\n")
            except Exception as e:
                print(f"An error has occured whilst generating the report for user overview")
    
           
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)
        
        # Read data from files 
        def read_users_from_file(file_path):
            username_password = {}
            with open(file_path, 'r') as user_file:
                user_data = user_file.read().split("\n")
                
                for user_str in user_data:
                   if user_str:
                      username, password = user_str.split(';')
                      username_password[username] = password  
           
            return username_password
        
        # Generate reports 
        def generate_reports(task_list):
            generate_task_overview_report(task_list)
            generate_user_overview_report(username_password, task_list)
        
        # Display the statistics
        def display_statistics(username_password, task_list):
            num_users = len(username_password)
            num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
