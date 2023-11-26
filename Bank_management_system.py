# by default admin
# username : admin
# pass : 123

class Bank:
    def __init__(self, name) -> None:
        self.name = name


class Account:
    accounts = []
    isloan = True
    bankrupt = False

    def __init__(self, name, password, email, address, type) -> None:
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.type = type
        self.__balance = 0

        self.loan = 0
        self.loan_total = 0
        self.transaction_history = []
        self.accNo = f'{len(Account.accounts)}-{name[:3]}'
        Account.accounts.append(self)

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print(f"\n--> Deposited {amount}. New balance: ${self.__balance}")
            self.transaction_history.append(
                {'Type': 'deposit', 'amount': amount})
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        if Account.bankrupt == False:
            if amount >= 0 and amount <= self.__balance:
                self.__balance -= amount
                print(f"\nWithdrew ${amount}. New balance: ${self.__balance}")
                self.transaction_history.append(
                    {'Type': 'withdraw', 'amount': -amount})
            else:
                print("\nWithdrawal amount exceeded")
        else:
            print("!!!! Bank is Bankcrupt !!!!")

    def check_balance(self):
        print(f"Your account balance is : {self.__balance}")

    def transfer_money(self, amount, accNo):
        flag = False
        if self.bankrupt == False:
            if amount >= 0 and amount <= self.__balance:
                for account in Account.accounts:
                    if accNo == account.accNo:
                        self.__balance -= amount
                        self.transaction_history.append(
                            {'Type': 'send', 'amount': -amount})
                        account.__balance += amount
                        account.transaction_history.append(
                            {'Type': 'recieve', 'amount': amount})
                        flag = True
                if flag == False:
                    print("Account does not exist")
            else:
                print("Insufficient Money")
        else:
            print("Bank is bankrupt!!!")

    def history(self):
        for item in self.transaction_history:
            print(' '.join(f'{key}: {value}' for key, value in item.items()))

    def take_loan(self, amount):
        if self.loan >= 0 and self.loan < 2 and Account.isloan == True:
            self.__balance += amount
            self.loan_total += amount
            self.loan += 1
            self.transaction_history.append(
                {'Type': 'loan', 'amount': amount})
        else:
            print("Loan can not be granted")

    def delete_account(self, accNo):

        flag = False
        for i, item in enumerate(Account.accounts):
            if item.accNo == accNo:
                del Account.accounts[i]
                flag = True
                break
        if flag == False:
            print("No account found")

    def all_user(self):
        for item in Account.accounts:
            print(f"Name : {item.name}    AccNO : {item.accNo}")

    def total_balance(self):
        sum = 0
        for item in Account.accounts:
            sum += item.__balance
        print('Total balance of bank : ', sum)

    def total_loan(self):
        sum = 0
        for item in Account.accounts:
            sum += item.loan_total
        print('Total Loan of bank : ', sum)

    def turn_off_loan(self):
        if Account.isloan == True:
            Account.isloan = False
            print("Loan feature turn off")
        else:
            Account.isloan = True
            print("Loan feature turn on")


admin = Account('admin', '123', 'admin@gmail.com', 'dhaka', 'admin')

currentUser = None
while True:
    if currentUser == None:
        print("\n--->Welcome to Ar's Bank\n")
        ch = input("\nLogin/Register (L/R): \n")
        if ch == 'r' or ch == 'R':
            type = input("savings account or Current account (sv/cu)")
            name = input("Name: ")
            email = input("Enter email : ")
            address = input("Enter Address : ")
            password = input("Password: ")
            if type == 'sv':
                currentUser = Account(name, password, email, address, type)
            elif type == 'cu':
                currentUser = Account(name, password, email, address, type)
            else:
                print("Entered Wrong Option.")

        elif ch == 'l' or ch == 'L':
            acc = input("Admin / Acount Holder (ad / ac) : ")
            if acc == 'ad':
                username = input("Enter username : ")
                password = input("Password : ")
                if username == 'admin' and password == '123':
                    currentUser = 'admin'
                    # print('hi')
                else:
                    print("You have entered wrong username or password")
            elif acc == 'ac':
                email = input("Email : ")
                password = input("Password : ")
                flag = False
                for account in Account.accounts:
                    if account.email == email and account.password == password:
                        currentUser = account
                        flag = True
                        break
                if flag == False:
                    print("Wrong email or password!!!")
            else:
                print("\nEntered wrong option")

        else:
            print("\nYou have entered Wrong Option!!!Please try again\n")
    else:
        if currentUser == 'admin':
            print("----------------------")
            print("1. Create an account")
            print("2. Delete an account")
            print("3. All user accounts list")
            print("4. Total available balance")
            print("5. Total loan amount")
            print("6. Loan feature")
            print("7. Bankrupt")
            print("8. Logout\n")

            op = int(input("Chhose Option:"))

            if op == 1:
                type = input("savings account or Current account (sv/cu)")
                name = input("Name: ")
                email = input("Enter email : ")
                address = input("Enter Address : ")
                password = input("Password: ")
                if type == 'sv':
                    Account(name, password, email, address, type)
                elif type == 'cu':
                    Account(name, password, email, address, type)
                else:
                    print("Entered wrong option")

            elif op == 2:
                accNO = input("Enter account number : ")
                admin.delete_account(accNO)

            elif op == 3:
                admin.all_user()

            elif op == 4:
                admin.total_balance()

            elif op == 5:
                admin.total_loan()

            elif op == 6:
                admin.turn_off_loan()

            elif op == 7:
                Account.bankrupt = True
                print("Bankrupt")

            elif op == 8:
                currentUser = None
            else:
                print('Entered wrong option')
        else:
            print("----------------------")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. take loan")
            print("6. Transfer Money")
            print("7. Logout\n")

            op = int(input("Chhose Option:"))

            if op == 1:
                amount = int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)

            elif op == 2:
                amount = int(input("Enter deposit amount:"))
                currentUser.deposit(amount)

            elif op == 3:
                currentUser.check_balance()

            elif op == 4:
                currentUser.history()

            elif op == 5:
                ama = int(input("Enter amount : "))
                currentUser.take_loan(ama)

            elif op == 6:
                amount = int(input("Enter amount : "))
                accnum = input("Enter Account number : ")
                currentUser.transfer_money(amount, accnum)

            elif op == 7:
                currentUser = None
            else:
                print('Entered wrong option')
