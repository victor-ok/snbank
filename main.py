import os
import json
from random import randint

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STAFF_FILE = os.path.join(BASE_DIR, 'staff.txt')
CUSTOMER_FILE = os.path.join(BASE_DIR, 'customer.txt')

staff_file = open(STAFF_FILE, "r")
customer_file = open(CUSTOMER_FILE, "r")

operation = input("Welcome to snbank \n Select an option below\n1. Staff login (S)\n2. Close App (C) \n")

while (operation == "S"):
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open("staff.txt") as f_obj:
        staff_details = f_obj.read()
        if username in staff_details and password in staff_details:
            print("welcome " + username)
            session = open("session.txt", "w")
            session.write(username)
            session.close()
        

            staff_operation = input("A. Create new bank account \nB. Check Account Details\nC. Logout\n")

            if staff_operation == "A":
                
                acc_name = input("Enter account name: ")
                opening_bal = input("Enter your opening balance: ")
                acc_type = input("Enter your preferred account type: ")
                acc_email = input("Enter a valid email: ")
                n = 10
                acc_number = ''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
                print(acc_number)
                
                data = {}
                data[acc_number] = []
                data[acc_number].append({
                    'account_name': acc_name,
                    'opening_balance': opening_bal,
                    'account_type': acc_type,
                    'account_number': acc_number
                })
                with open("customer.txt", "w") as f:
                    json.dump(data, f)
                    # f.write(acc_name+" "+opening_bal+" "+acc_type+" "+acc_type+" "+acc_email+" "+" "+acc_number+""+""+"")
                    # f.close()
                    staff_operation = input("A. Create new bank account \nB. Check Account Details\nC.Logout\n")

            elif staff_operation == "B":
                cus_acc_number = input("Enter account number of the account you want to fetch its details: ")
                with open("customer.txt") as f_obj:
                    customer_details = f_obj.read()
                    if cus_acc_number in customer_details:
                        f_obj.seek(_from)
                        print (f_obj.readlines())
                        staff_operation = input("A. Create new bank account \nB. Check Account Details\nC. Logout\n")

            # elif staff_operation == "C":
                

        else:
            print("You are not a staff")


while (operation == "C"):
    print("Thank you for banking with us")
    break