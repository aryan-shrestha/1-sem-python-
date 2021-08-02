import auth
import customer
import admin
import tabulate

# fuction to create user. by default registered user is neither active user not admin user
def create_user_view():
    name = input("Full name: ")
    address = input("Address: ")
    email = input("Email: ")
    contact_no = input("Contact No.: ")
    gender = input("Gender: ")
    dob = input("Enter date of birth: ")
    username = input("Username: ")
    password = input("Password: ")
    
    username = auth.create_customer_user(
        name= name,
        address= address,
        email=email,
        contact_no=contact_no,
        gender=gender,
        dob=dob,
        username=username,
        password=password,
    )
    print(f"Account Successfully created for {username}.")

# function to handle login 
def customer_login_view():
    username = input("Username: ")
    password = input("Password: ")

    if auth.login(username, password) == True:  # calling login function defined in auth module 
        customer_view(username)
    else:
        print("Invalid Username or password")
        customer_login_view()

# function to handle admin login
def admin_login_view():
    username = input("Username: ")
    password = input("Password: ")

    if auth.admin_login(username, password) == True:
        print("Admin User successfully Logged in !!")
        admin_view()
    else:
        print("Invalid Username or passord. Please Try again. ")
        admin_login_view()

def admin_view():
    user_input = int(input("""
    1) Verify New users
    2) Verify Loan request
    3) See all verified Loan
    4) See all transactions
    """))
    try:
        if user_input == 1:
            # function to verify the customer user
            def admin_func_1():
                print("Below is the list of the unverified users: \n")
                admin.list_unverified_users()
                user_input = input("Do you want to verify user?(y/n)")
                while user_input == 'y':
                    username = input("Enter username of customer you want to verify: ")
                    if admin.verify_customer(username):
                        print(f"\n{username} verified!\n")
                        admin_func_1()
                admin_view()
            admin_func_1()

        elif user_input == 2:
            # function to verify the customer loan
            def admin_func_2():
                print("Below is the list of the unverified users: \n")
                admin.list_unverified_loan()
                user_input = input("Do you want to  verify loan?(y/n)\n")
                while user_input == 'y':
                    loan_id = input("Enter loan ID you want to verify: ")
                    if admin.verify_loan(loan_id):
                        print(f"loan for the customer with {loan_id} has been verified\n")
                        admin_func_2()
                admin_view()
            admin_func_2()
        
        elif user_input == 3:
            def admin_func_3():
                print("Below are the loans that are verified: \n")
                admin.list_verified_loan()
                input("Press any key to go back..")
                admin_view()
            admin_func_3()

        elif user_input == 4:
            def admin_func_4():
                print("All the trasactions are listed below: \n")
                transaction_list = admin.see_all_transaction()
                headers = ["Loan ID", "Username", "Principle", "Time", "Interest", "Rate", "Is Verified", "Amount"]
                print(tabulate.tabulate(transaction_list, headers))
                input("Press any enter to go back..")
                admin_view()
            admin_func_4()

    except:
        print("Invalid Input!")
        admin_view()

# customer view after login
def customer_view(username):
    username = username
    try:
        user_choice = int(input("""
        Enter Corresponding integer value to select the options
        -------------------------------------------------------\n
        1) See available loans
        2) Pay loan instalment
        3) View transactions
        4) Check loan status
        5) go back
        """))
    except ValueError:
        print("Invalid input")
        customer_view()
    else:
        if user_choice == 1:
            def customer_func_1(username):
                print("Below is the list of all the available loan")
                customer.show_loan_list()

                loan_type = input("Input loan type to apply for loan: ")
                p = float(input("Amount: "))
                t = float(input("Time: "))
                
                try:
                    loan_detail = customer.apply_loan(loan_type,p,t,username)
                except:
                    print("Invalid Information")
                    customer_func_1(username)
                else:
                    print("Your request for the loan with following details has been submited..\n")
                    print("Loan details:")
                    print(f"principle = {loan_detail[0]}, time = {loan_detail[1]}, rate = {loan_detail[2]}, loan_detail = {loan_detail[3]}\n")
                    customer_view(username)
            customer_func_1(username)

        elif user_choice == 2:
            # Function to pay installment on loan
            def customer_func_2(username):
                print("Below are the loans you have to pay: \n")
                headers = ["Loan ID", "Username", "Principle", "Time", "Interest", "Rate", "Is Verified", "Amount"]
                loan_list = customer.see_all_loan(username)
                print(tabulate.tabulate(loan_list, headers=headers))

                user_input = input("\nDo you want to pay installment(y/n)? ")
                while user_input == "y":
                    loan_id = input("Enter loan ID: ")
                    p,i,a = customer.see_loan_detail(username, loan_id)
                    loan_detail = [[p,i,a]]
                    header = ["Principle", "Interest", "Amount"]
                    print(tabulate.tabulate(loan_detail, headers=header))
                    installment_amount = float(input("Enter Installment amount: "))
                    remaining_amount = customer.pay_loan(username, loan_id, installment_amount)
                    print(f"""
                    {installment_amount} successfully deducted from the total payable amount.
                    Your remaining payable amount is {remaining_amount}
                    """)
                    customer_func_2(username)
                customer_view(username)
            customer_func_2(username)

        elif user_choice == 3:
            def user_choice_3(username):
                print("Below are your transactions:\n")
                customer.view_transactions(username)
                input("\nPress any key to go back..")
                customer_view(username)
            user_choice_3(username)
        
        elif user_choice == 4:
            def user_choice_4(username):
                print("Below are your loans and their current status: \n")
                headers = ["Loan ID", "Username", "Principle", "Time", "Interest", "Rate", "Is Verified", "Amount"]
                loan_list = customer.see_loan_status(username)
                print(tabulate.tabulate(loan_list, headers=headers))
                input("\n Press any key to go back..")
                customer_view(username)    
            user_choice_4(username)
        
        elif user_choice == 5:
            print("Logged Out from the system.")
            home_view()

def home_view():
    try:
        user_choice = int(input("""
        1) Admin Login
        2) Customer Login
        3) Register Customer
        """))
    except ValueError:
        print("Invalid input. Please input integer input.")
        home_view()
    else:
        if user_choice == 1:
            admin_login_view()
        elif user_choice == 2:
            customer_login_view()
        elif user_choice == 3:
            create_user_view()

home_view()

