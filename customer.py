import tabulate
import utils
import uuid

def show_loan_list():
    loan_list = utils.text_to_list('loan_detail.txt', 'r')
    headers = ["loan type", "0-5years", "6-10 years", "11-15 years", "16 years-above"]
    print(tabulate.tabulate(loan_list, headers=headers))

def apply_loan(loan_type, p, t, username):
    loan_type = loan_type.lower()

    i, r = utils.calculate_loan(p, t, loan_type)

    loan_detail = [p,t,r,i]
    with open(f"loan.txt", "a") as file:
        is_approved =  False                # this value will be set True when admin approves the loan
        loan_id = uuid.uuid4()
        amount = float(i) + float(p)
        file.write(f"{loan_id},{username},{p},{t},{i},{r},{is_approved},{amount}\n")
        return loan_detail

# customer pay loan function 
def see_all_loan(username):
    loan_list = utils.text_to_list('loan.txt', 'r')
    user_loans = []
    for loan in loan_list:
        if loan[1] == username:
            if loan[-2] == "True":
                user_loans.append(loan)   
    return user_loans

def see_loan_detail(username, loan_id):
    user_loans = see_all_loan(username)
    for loan in user_loans:
        if loan[0] == loan_id:
            selected_loan = loan
    p = float(selected_loan[2])
    i = float(selected_loan[4])
    a = p + i
    return p,i,a

def pay_loan(username, loan_id, installment_amount):
    p,i,a = see_loan_detail(username, loan_id)
    a = a - installment_amount
    
    loan_list = utils.text_to_list('loan.txt', 'r')
    
    for loan in loan_list:
        if loan[0] == loan_id:
            loan[-1] = a
            break
    
    with open("loan.txt", 'w+') as file:
        for loan in loan_list:
            file.write(f"{loan[0]},{loan[1]},{loan[2]},{loan[3]},{loan[4]},{loan[5]},{loan[6]},{loan[7]}\n")
    return a


