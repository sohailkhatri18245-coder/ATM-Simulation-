import random

Name = ['Aarav Sharma', 'Isha Verma', 'Rohan Gupta', 'Neha Patel', 'Karan Mehta',
        'Ananya Iyer', 'Vikram Singh', 'Priya Nair', 'Rahul Das', 'Sneha Reddy']
Pin = [4821, 1593, 7642, 2308, 9175, 6459, 3814, 7026, 5582, 8963]
account_number = [739251, 482906, 915374, 608421, 347862, 829517, 564903, 193845, 672104, 405728]
Complete_detail = []
Balance = {}
Amount_in_account = []

def New_Amount():
    for i in range(len(Name)):
        A = random.randint(1000, 10000)
        Amount_in_account.append(A)
        Complete_detail.append([Name[i], Pin[i], account_number[i], "Initial Balance :", A])
        Balance[account_number[i]] = {Name[i]: A}


New_Amount()


def balance():
    P = int(input("Enter Your Account Number: "))
    if P in account_number:
       
        print("Your Name           Your Balance")
        print(Balance[P])
    else:
        print("Account number not found.")


def Withdraw():
    P = int(input("Enter Your Account Number: "))
    
    Withdraw_amount = int(input("Enter The Amount To Withdraw: "))
    PiN = int(input("Enter Your Pin: "))

    if P in account_number:
        acc_idx = account_number.index(P)
        if PiN in Pin and Pin.index(PiN) == acc_idx:
            if Withdraw_amount > Amount_in_account[acc_idx]:
                print("Insufficient balance.")
            else:
                Amount_in_account[acc_idx] -= Withdraw_amount
                print("Withdrawal successful! Remaining Balance:", Amount_in_account[acc_idx])
        else:
            print("Invalid Pin.")
    else:
        print("Invalid Account Number.")


def deposit():
    P = int(input("Enter Your Account Number: "))
    Deposit_amount = int(input("Enter Your Amount: "))
    PiN = int(input("Enter Your Pin: "))

    if P in account_number:
        acc_idx = account_number.index(P)
        if PiN in Pin and Pin.index(PiN) == acc_idx:
            Amount_in_account[acc_idx] += Deposit_amount
            print("Deposit successful! New Balance:", Amount_in_account[acc_idx])
        else:
            print("Invalid Pin.")
    else:
        print("Invalid Account Number.")


def Pin_change():
    P = int(input("Enter Your Account Number: "))
    PiN = int(input("Enter Your Current Pin: "))

    if P in account_number:
        acc_idx = account_number.index(P)
        if PiN in Pin and Pin.index(PiN) == acc_idx:
            New_pin = int(input("Enter Your New Pin: "))
            Pin[acc_idx] = New_pin
            print("Your Account Number:", P)
            print("Your Previous Pin   :", PiN)
            print("Your New Pin        :", Pin[acc_idx])
            print("Congrats! You have successfully changed your PIN.")
        else:
            print("Invalid Pin.")
    else:
        print("Invalid Account Number.")


print("\n_______OPTIONS________\n")
print("Press 1 for Withdraw")
print("Press 2 for Deposit")
print("Press 3 for Check Balance")
print("Press 4 for PIN change")
choose = input("Enter Your Choice: ")

#New_Amount()

if choose == "1":
    Withdraw()
elif choose == "2":
    deposit()
elif choose == "3":
    balance()
elif choose == "4":
    Pin_change()
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")