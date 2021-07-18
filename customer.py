from os import error
import tabulate
import utils

def show_loan_list():
    loan_list = utils.text_to_list('loan_detail.txt', 'r')
    headers = ["loan type", "0-5years", "6-10 years", "11-15 years", "16 years-above"]
    print(tabulate.tabulate(loan_list, headers=headers))

show_loan_list()

def apply_loan(loan_type, p, t, username):
    loan_type = loan_type.lower()

    i, r = utils.calculate_loan(p, t, loan_type)

    loan_detail = [p,t,r,i]
    with open(f"loan.txt", "a") as file:
        is_approved =  False                # this value will be set True when admin approves the loan
        file.write(f"{username},{p},{t},{i},{r},{is_approved}\n")
        return loan_detail

# customer pay loan function 
def pay_loan(username):
    pass