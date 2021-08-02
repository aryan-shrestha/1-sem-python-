import utils
import tabulate 

def list_unverified_users():
    user_list = utils.text_to_list('user.txt', 'r')
    unverified_users = []
    for user in user_list:
        if user[9] == "False":
            unverified_users.append(user)
    
    headers = ["Name", "Address", "Email", "Phone No.", "Sex", "DOB", "Username", "Password", "Is Admin", "Is Verified"]
    print(tabulate.tabulate(unverified_users, headers=headers))

def verify_customer(username):
    user_list = utils.text_to_list('user.txt', 'r')

    for user in user_list:
        if user[6] == username:
            user[9] = True
            break

    with open("user.txt", 'w+') as file:
        for user in user_list:
            file.write(f"{user[0]},{user[1]},{user[2]},{user[3]},{user[4]},{user[5]},{user[6]},{user[7]},{user[8]},{user[9]}\n")
    return True

def list_verified_loan(username):
    loan_list = utils.text_to_list('loan.txt', 'r')
    unverified_loans = []
    for loan in loan_list:
        if loan[1] == username:
            unverified_loans.append(loan)
    
    headers = ["Loan ID","username", "Principle", "Time", "Interest", "Rate", "Is verified", "Remain amt"]
    print(tabulate.tabulate(unverified_loans, headers=headers))    

def list_unverified_loan():
    loan_list = utils.text_to_list('loan.txt', 'r')
    unverified_loans = []
    for loan in loan_list:
        if loan[6] == "False":
            unverified_loans.append(loan)
    
    headers = ["Loan ID","username", "Principle", "Time", "Interest", "Rate", "Is verified", "Amount"]
    print(tabulate.tabulate(unverified_loans, headers=headers))    

def verify_loan(loan_id):
    loan_list = utils.text_to_list('loan.txt', 'r')
    
    for loan in loan_list:
        if loan[0] == loan_id:
            loan[6] = True  
            break
    with open("loan.txt", "w+") as file:
        for loan in loan_list:
            file.write(f"{loan[0]},{loan[1]},{loan[2]},{loan[3]},{loan[4]},{loan[5]},{loan[6]},{loan[7]}\n")
    return True

def see_all_transaction():
    loan_list = utils.text_to_list("transactions.txt", "r")

    return loan_list