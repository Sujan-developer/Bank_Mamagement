def Create_Acc():
    name = input("Enter your name: ").lower()
    while not any(char.isalpha() for char in name):
        print("Name was not valid")
        name = input("Enter your name: ").lower()

    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Not a valid input")


    while True:
        code = input("Enter a bank code: ")
        if code.isdigit():
            code = int(code)
            break
        else:
            print("Not a valid output")

    if age < 18:
        print("Not eligile for making an account")
    else:
        balance = 0
        with open("bank.txt", "r") as f:
            accounts = f.readlines()
        found = False
        for account in accounts:
            account = account.strip()
            acc_data = account.split(",")
            
            if len(acc_data) < 4:
                continue

            if code == int(acc_data[2]):
                print("Code already exists")
                found = True
                break
        if not found:
            with open("bank.txt", "a") as f:
                f.write(f"{name},{age},{code},{balance}\n")
                print("Account successfully created")


def deposit():

    while True:
        Code = input("Enter your code: ")
        if Code.isdigit():
            Code = int(Code)
            break
        else:
            print("Invalid code")

    while True:
        amount = input("Enter your amount to dep: ")
        if amount.isdigit():
            amount = float(amount)
            break
        else:
            print("Invalid amount")



    found = False

    with open("bank.txt", "r") as f:
        accounts = f.readlines()

    updated_accounts = []

    for account in accounts:
        account = account.strip()

        acc_data = account.split(",")

        if len(acc_data) < 4:
            print(f"Insufficient account data: {account}")
            continue

        try:
            if Code == int(acc_data[2]):
                if amount < 0:
                    print("Amount must be positive")
                    updated_accounts.append(account + "\n")
                    continue
                    found = True
                elif amount == 0:
                    print("Amount must be more than 0")
                    found = True
                    updated_accounts.append(account + "\n")
                    continue
                else:
                    current_balance = float(acc_data[3])
                    new_balance = current_balance + amount
                    acc_data[3] = str(new_balance)
                    updated_account = ",".join(acc_data)
                    updated_accounts.append(updated_account + "\n")
                    print(f"Deposit successful. New balance: {new_balance}")
                    found = True
            else:
                updated_accounts.append(account + "\n")

        except Exception as e:
            print(f"Error processing account: {account}")
            print(f"Error details: {e}")

    if not found:
        print("Account not found")

    with open("bank.txt", "w") as f:
        f.writelines(updated_accounts)


def withdraw():
    
    while True:
        code = input("Enter your code: ")
        if code.isdigit():
            code = int(code)
            break
        else:
            print("Not valid")
    while True:
        try:
            Withdraw = float(input("Enter your amount to withdraw: "))
            break
        except ValueError:
            print("Invalid input! Enter a valid number")



        if Withdraw < 0:
            print("You can't withdraw lower than 0")


    found = False
    with open("bank.txt", "r") as f:
        accounts = f.readlines()


    updated_accounts = []
    
    for account in accounts:
        account = account.strip()
        acc_data = account.split(",")
        if len(acc_data) < 4:
            print(f"Insufficient Account data: {data}")
            continue
        
        try:
            current_balance = float(acc_data[3])
            if code == int(acc_data[2]):
                if Withdraw > current_balance:
                    print(f"You only have: {current_balance}")
                    updated_accounts.append(account + "\n")
                    found = True
                    continue
                elif Withdraw == 0:
                    print("Amount must be more than 0")
                    updated_accounts.append(account + "\n")
                    found = True
                    continue
                elif Withdraw < 0:
                    print("Amount must be positive")
                    updated_accounts.append(account + "\n")
                    found = True
                    continue
                else:
                    new_balance = current_balance - Withdraw
                    acc_data[3] = str(new_balance)
                    updated_account = ",".join(acc_data)
                    updated_accounts.append(updated_account + "\n")
                    print(f"Withdraw successful. New balance: {new_balance}")
                    found = True
                    break
            else:
                updated_accounts.append(account + "\n")

        except Exception as e:
            print(f"Error processing account: {account}")
            print(f"Error details: {e}")
    if not found:
        print("Account not found")
    with open("bank.txt", "w") as f:
        f.writelines(updated_accounts)

def Display():
    Code = int(input("Enter your code: "))
    with open("bank.txt", "r") as f:
        lines = f.readlines()
    found = False
    for line in lines:
        account = line.strip()
        display = line.split(",")
        if Code == int(display[2]):
            display = [item.replace("\n", "") for item in display]
            print(display)
            found = True
            break
    if not found:
        print("Code not found")




while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display")
    print("5. Exit")
    choose = input("Enter a choice: ")
    if choose == "1":
        Create_Acc()
    elif choose == "2":
        deposit()
    elif choose == "3":
        withdraw()
    elif choose == "4":
        Display()
    elif choose == "5":
        break
    else:
        print("Not a valid option")
