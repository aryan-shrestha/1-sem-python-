import utils

# admin functions 
def create_admin_user(username, password):
    username = username
    password = password
    is_admin = True

    while utils.validate_admin_username(username):
        print("Username already exist!")
        username = input("Enter another username: ")

    with open('admin_user.txt', 'a+') as file:
        file.write(f"{username},{password},{is_admin}\n")

        print(file.read())

    return True

# customer account creation function
def create_customer_user(**kwargs):
    #return True if account is successfully created 
    is_admin = False                        # setting customer non-admin user by default
    is_active = False                       # setting customer inactive user by default
    
    username_validation = utils.validate_username(kwargs['username'])

    while username_validation == True:      # checking if user already exists. If True asks to reenter other username
        kwargs['username'] = input("Enter another username: ")
        username_validation = utils.validate_username(kwargs['username'])
        
    with open('user.txt', 'a+') as file:    # registering user in user.txt file
        file.write(f"{kwargs['name']},{kwargs['address']},{kwargs['email']},{kwargs['contact_no']},{kwargs['gender']},{kwargs['dob']},{kwargs['username']},{kwargs['password']},{is_admin},{is_active}\n")

        print(f"user created for {kwargs['username']}")

    return True

# Name, Address, Email ID, Contact Number, Gender, Date_Of_Birth, Loan Type, Loan Terms (in years), Instalment 
# Amount, User ID, Password, Rewrite Password,


# customer user login function 
def login(username, password):
    username, password = username, password

    user_list = utils.text_to_list('user.txt', 'r')
    
    for user in user_list:
        if username == user[6] and password == user[7]:     # checking username and password 
            if user[9] == "True":                           # checking if user is verified or not
                return True      

# admin login function
def admin_login(username, password):
    username, password = username, password

    user_list = utils.text_to_list('admin_user.txt', 'r')   # opening admin_text.txt file and arranging data in list
    
    for user in user_list:
        if username == user[0] and password == user[1]:     # validating username and password
            if user[2] == 'True':                           # validating is the user is admin
                return True