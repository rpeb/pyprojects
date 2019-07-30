"""This is a command line password authenticator"""
import getpass, sys
user_data={}
def password_check(x):
    if(len(x) < 6):
        return 0
while(True):    
    choice=int(input("Press 1 for sign up or 2 if you're an existing user: "))  
    if choice==1:
        username=input("Set username: ")
        try:
            print("Set password: ")
            password=getpass.getpass()
        except Exception as error:
            print('Error: ', error)
        while password_check(password) == 0:
            print("Password must have atleast 6 characters.")
            try:
                password=getpass.getpass()
            except Exception as error:
                print('Error: ', error)
        user_data[username]=password
        print("Yayy, Succesfully registered!!")
    elif choice==2:
        username=input("Enter your username: ")
        if username in user_data:
            password=getpass.getpass()
            while(user_data[username] != password):
                print("Incorrect password! Try again.")
                password=getpass.getpass()
            print(f"Welcome {username}\n")
        else:
            print(f"No record found for user {username}\n")
        
    else:
        sys.exit(1)
    
