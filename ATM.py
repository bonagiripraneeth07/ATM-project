import datetime
import csv
import random as rd

from _csv import writer

dt = datetime.datetime.now()
time = str(dt.strftime('%X'))
date = str(dt.date())
balance = rd.randint(1000, 9999)


def create_account():
    account_number = input("Enter your 10 digit account number : ")
    account_pin = input('Enter your 4 digit PIN to continue...: ')
    account_name = input("Please Enter Your Name : ")
    new_acc_balance = 1000
    search_data = account_number

    if len(account_number) == 10 and len(account_pin) == 4:
        with open("existing accounts.csv", 'r') as file:
            contents = file.read()
            if search_data in contents:
                print("account already exists")
            else:
                print("Account creation successful")
                new_account = [account_number, account_name,f'{date}/{time}']
                with open("existing accounts.csv", 'a') as file:
                    writer_obj = writer(file)
                    writer_obj.writerow(new_account)

        print("1. Login 2.Exit")
        userput = int(input('~'))
        if userput == 1:
            login()
        elif userput == 2:
            print("Thank you ,please visit again")
        else:
            print("invalid input")

    else:
        print("please check the account number and PIN")


def deposit(acc_num):
    account_number = acc_num
    #print(account_number)
    print("Enter amount to deposit")
    account_balance = balance
    initial_amount = balance
    deposit_amount = int(input('~'))
    random = rd.randint(1000, 9999)
    # random_balanace= rd.randint(1000,9999)

    print("""
             --HUMAN VERIFICATION--     
     """)
    print(random)
    userput = int(input("Please Enter the PIN you see on Screen : "))
    account_balance = account_balance + deposit_amount
    if userput == random:
        with open("transactions.csv", 'a') as file:
            fill = [account_number, initial_amount, "Deposit", deposit_amount, account_balance, f'{date}/{time}']
            writer_obj = writer(file)
            writer_obj.writerow(fill)
        print("verification successful ")

        print(f'amount {deposit_amount} deposited  successfully ')
        userput = int(input("~ Press 1 to show available balance  2 . Exit "))
        if userput == 1:
            print(f'the available balance in you account is :₹{account_balance}')
        elif userput == 2:
            print("Thank you,visit again ")
        else:
            print("Invalid Input")

    else:
        print("veriffication faild please try again later")


def withdrawal(acc_num):
    account_number = acc_num
    #print(account_number)
    account_balance = balance
    initial_amount = balance
    # random_balanace =  rd.randint(1000,9999)
    print("Enter amount to withdrawal")
    withdrawal_amount = int(input('~'))
    if withdrawal_amount > initial_amount:
        print("insufficient balance  ")
        pass
    else:
        random = rd.randint(1000, 9999)
        print("""
                --HUMAN VERIFICATION--     
         """)
        print(random)
        userput = int(input("Please Enter the PIN you see on Screen : "))
        if userput == random:
            print("verification successful ")
            account_balance = account_balance - withdrawal_amount
            with open("transactions.csv", 'a') as file:
                fill = [account_number, initial_amount, "withdraw", withdrawal_amount, account_balance,
                        f'{date}/{time}']
                writer_obj = writer(file)
                writer_obj.writerow(fill)
            print(f'amount ₹{withdrawal_amount} withdrawn  successfully ')
            print("""
           Press 1 to show available balance 
           Press 2 to  Exit
           """)
            userput = int(input('~'))
            if userput == 1:
                print(f'the available balance in you account is : ₹{account_balance}')
            elif userput == 2:
                print("Thank you,visit again ")
            else:
                print("Invalid Input ")
        else:
            print("veriffication faild please try again  ")
            continue_browsing(account_number)


def checkbalance():
    account_balance = balance
    print(f' the balance available in your account is : ₹{account_balance}')

def fundtransfer(acc_num):
    #acc_num=acc_num
    print(f' Your Account number : {acc_num}')
    account_balance=balance
    print('Enter Account number to Transfer Funds')
    transfer_account_number=int(input('~'))
    account_balance = balance
    initial_amount = balance
    # random_balanace =  rd.randint(1000,9999)
    print("Enter amount to Transfer")
    transfer_amount = int(input('~'))
    if transfer_amount > initial_amount:
        print("insufficient balance  ")
        pass
    else:
        random = rd.randint(1000, 9999)
        print("""
                    --HUMAN VERIFICATION--     
             """)
        print(random)
        userput = int(input("Please Enter the PIN you see on Screen : "))
        if userput == random:
            print("verification successful ")
            account_balance = account_balance - transfer_amount
            with open("transactions.csv", 'a') as file:
                fill = [acc_num, initial_amount, f'Fund Transfer to {transfer_account_number}',transfer_amount , account_balance,
                        f'{date}/{time}']
                writer_obj = writer(file)
                writer_obj.writerow(fill)
            print(f'amount ₹{transfer_amount} Fund Transfer  successful ')
            print("""
               Press 1 to show available balance 
               Press 2 to  Exit
               """)
            userput = int(input('~'))
            if userput == 1:
                print(f'the available balance in you account is : ₹{account_balance}')
            elif userput == 2:
                print("Thank you,visit again ")
            else:
                print("Invalid Input ")
        else:
            print("veriffication faild please try again  ")
            continue_browsing(acc_num)






def services(acc_num):
    account_num = acc_num
    print('------------------------------------------------------------------------------------')
    print("welcome to YourBankOfIndia ATM services ")

    print("""           
                        Servies

 1.Money withdrawal  2.Check Balance  3.Money Deposit 4.Funds Transfer                
      """)
    userput = int(input('~'))
    if userput == 1:
        print("Money withdrawal")
        withdrawal(account_num)



    elif userput == 2:
        print("check balance")
        checkbalance()



    elif userput == 3:
        print("money deposit")
        deposit(account_num)
    elif userput==4:
        print('Funds transfer')
        fundtransfer(acc_num)


    else:
        print("Invalid Input")
    continue_browsing(account_num)


def continue_browsing(acc_numb):
    account_number = acc_numb
    print("""            


         1.Money withdrawal  2.Check Balance  3.Money Deposit 4. Logout               
              """)
    userput = int(input('~'))
    if userput == 1:
        print("Money withdrawal")
        withdrawal(account_number)
    elif userput == 2:
        print("check balance")
        checkbalance()

    elif userput == 3:
        print("money deposit")
        deposit(account_number)
    elif userput == 4:
        print("Loging out!")

    else:
        print("Invalid Input")


def login():
    account_number = input("Enter the 10 Digit account number to Login :  ")
    account_pin = input('Enter your 4 digit PIN to continue... : ')
    search_data = account_number
    if len(account_number) == 10 and len(account_pin) == 4:
        with open("existing accounts.csv", 'r') as file:
            contents = file.read()
            if search_data in contents:
                print("Login successful")
                services(account_number)
    else:
        print("please check the account number and PIN")
        print("Account not found ")




print("----------------------------------------------------------------------------------------------------------")
print("""Press 1 to create a new YourBankOfIndia ATM Account 
      2 to Login existing Account  
      """)
userput = int(input("~"))
if userput == 1:
    create_account()
elif userput == 2:
    login()
else:
    print("Invalid Input")


