######################################################################################################
# Assignment 0
# Task : Registration and Login system with Python, file handling
# by : Hrishikesh Limaye
######################################################################################################
# re module for regular expressions : email validation
import re
# importing os module : file handling . Get current program directory to store user database file
import os

#variable to store login status
isUserFound = False

# Pattern for email validation
emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
passwordregex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"

# Main Application Entry Point
option = int(input('Select Relevant Option 1.Register 2.Login \r\n'))

# Validate Entered Input
if option == 0:
    # undefined input by user
    print('Invalid Input')
elif option == 1:
    # User has selected New Registration
    print('Welcome to New User Registration')
    email = input('Enter E-mail address as username ')
    password = input('Enter Password ')

    #validate email
    if(re.fullmatch(emailregex, email)):
        # Validate Password
        pswd = re.compile(passwordregex)
        pswdc = re.search(pswd, password)
        if(pswdc):
            #email and password both are correct .
            # New user registration completed
            # Log Data to the file d14_task1_userdb.txt
            # Get current Working Directory to get the path for the user db file
            cwd = os.getcwd()
            try:
                userdb = open(cwd+"/"+"d14_task1_userdb.txt", "a")
                userdb.write("\r\n" + email + " : " + password)
                print(' User Registration Completed Successfully ')
                userdb.close()
            except:
                print('Exception in file handling ')
        # else for if(pswdc):
        else:
            print('password is invalid')
    # else for if (re.fullmatch(emailregex, email)):
    else:
        # Dont Validate Password as email is invalid
        print("Invalid Email . Please retry !")

elif option == 2:
    # Registered User Login
    print('Welcome User ! ')
    task = int(input('Enter Relevant task : 1.Login 2. Forgot Password \r\n'))

    if task == 0:
        print('Invalid Input')
    elif task == 1:
        # Login selected . Check for credentials in db file
        username = input('Enter Username / email ')
        password = input('Enter password')
        try:
            cwd = os.getcwd()
            userdb_read = open(cwd + "/" + "d14_task1_userdb.txt", "r")
            lines = userdb_read.readlines()
            #remove '\n' from the file
            for line in lines:
                line.rstrip('\n')
                if(line != '\n'):
                    data = line.split(':')
                    # Only for debug
                    #print(data[0])
                    if data[0].strip() == username.strip() :
                        if data[1].strip() == password.strip():
                            print('Login Successful !')
                            isUserFound = True
                            break
                        else:
                            print('Incorrect Password . Please try forgot Password option !')
            if isUserFound == False:
                print('User not found / registered . Please use new user registration')
            #close opened file
            userdb_read.close()

        except:
            print('Exception in db file handling ')
    elif task == 2:
        # Forgot Password .Retrieve their original password
        username = input('Enter Username / email ')
        cwd = os.getcwd()
        try:
            userdb_readonly_password = open(cwd + "/" + "d14_task1_userdb.txt", "r")
            lines = userdb_readonly_password.readlines()
            # remove '\n' from the file
            for line in lines:
                line.rstrip('\n')
                if (line != '\n'):
                    data = line.split(':')
                    # Only for debug
                    # print(data[0])
                    if data[0].strip() == username.strip():
                        print('Original Password for username : '+ username +' is  ' +data[1].strip())
                        isUserFound = True
                        break

            if isUserFound == False:
                print('User not found / registered . Please use new user registration')
            #close opened file
            userdb_readonly_password.close()

        except:
            print('Exception in db file handling ')
    else:
        # else for if task == 0:
        print('Invalid Task')
# else for if option == 0:
else :
    print('Invalid User Input ')