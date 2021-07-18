from os import name


def validate_username(username):

    # return True if username already exists else returns False

    user_list = text_to_list('user.txt', 'r')
   
    for user in user_list:
        if username == user[6]:
            already_exist = True
            break
        else:
            already_exist = False

    try:
        return already_exist
    except UnboundLocalError: # handling error caused due to empty user_list
        return False

def validate_admin_username(username):

    # return True if username already exists else returns False

    user_list = text_to_list('admin_user.txt', 'r')
    
    for user in user_list:
        if username == user[0]:
            already_exist = True
            break
        else:
            already_exist = False

    try:
        return already_exist
    except UnboundLocalError:   # handling error caused due to empty user_list
        return False

def text_to_list(file_name, mode):
    
    # returns a list from the text file

    with open(file_name, mode) as file:
        data = file.read().split('\n')
        user_list = []
        for ele in data:
            user_list.append(ele.split(','))

        user_list.pop(-1)   # removing the last empty string character from the user_list which is created by \n 
                            # while writing data on file
    return user_list

def calculate_loan(p, t, loan_type):
    loan_list = text_to_list('loan_detail.txt', 'r')

    for loan in loan_list:
        if loan_type == loan[0]:
            if t <= 5:
                if loan[1] == '-':
                    raise ValueError("Loan not available for the given year") 
                else:
                    r = float(loan[1])

            elif t>=6 and t<=10:
                if loan[2] == '-':
                    raise ValueError("Loan not available for the given year")    
                else:
                    r = float(loan[2])

            elif t>=11 and t<=15:
                if loan[3] == '-':
                    raise ValueError("Loan not available for the given year")    
                else:
                    r = float(loan[2])
            elif t>=16:
                if loan[4] == '-':
                    raise ValueError("Loan not available for the given year")    
                else:
                    r = float(loan[2])
            else:
                raise ValueError("Invalid input")
    
    i = (p*t*r)/100
    return i,r
   