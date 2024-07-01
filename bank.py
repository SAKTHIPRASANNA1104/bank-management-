import pyodbc

class Bank:
    def __init__(self):
        self.conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=bank_database.accdb;')
        self.cursor = self.conn.cursor()

    def func(self):
        self.n = int(input('Enter number (1: New Account, 2: Print Details, 3: Deposit, 4: Withdraw, 5: Quit): '))
        while self.n <= 5:
            if self.n == 1:
                self.newac()
            elif self.n == 2:
                self.out()
            elif self.n == 3:
                self.deposit()
            elif self.n == 4:
                self.withdraw()
            elif self.n == 5:
                self.quit()
                break
            self.n = int(input('Enter number (1: New Account, 2: Print Details, 3: Deposit, 4: Withdraw, 5: Quit): '))

    def newac(self):
        self.no = int(input('Enter account number: '))
        self.na = input('Enter name: ')
        self.opbal = int(input('Enter opening balance: '))
        self.am = self.opbal  # Initialize total amount with opening balance

        self.cursor.execute("INSERT INTO Accounts (AccountNumber, Name, OpeningBalance, CurrentBalance) VALUES (?, ?, ?, ?)",
                            (self.no, self.na, self.opbal, self.am))
        self.conn.commit()
        print('New account created successfully.')

    def out(self):
        self.no = int(input('Enter account number to display details: '))
        self.cursor.execute("SELECT * FROM Accounts WHERE AccountNumber = ?", (self.no,))
        row = self.cursor.fetchone()
        if row:
            print('Account number:', row.AccountNumber)
            print('Name:', row.Name)
            print('Opening balance:', row.OpeningBalance)
            print('Current balance:', row.CurrentBalance)
        else:
            print('Account not found.')

    def deposit(self):
        self.no = int(input('Enter account number for deposit: '))
        self.cursor.execute("SELECT CurrentBalance FROM Accounts WHERE AccountNumber = ?", (self.no,))
        row = self.cursor.fetchone()
        if row:
            self.am = row.CurrentBalance
            deposit_amount = int(input('Enter deposit amount: '))
            self.am += deposit_amount
            self.cursor.execute("UPDATE Accounts SET CurrentBalance = ? WHERE AccountNumber = ?", (self.am, self.no))
            self.conn.commit()
            print('Deposit successful.')
            self.out()
        else:
            print('Account not found.')

    def withdraw(self):
        self.no = int(input('Enter account number for withdrawal: '))
        self.cursor.execute("SELECT CurrentBalance FROM Accounts WHERE AccountNumber = ?", (self.no,))
        row = self.cursor.fetchone()
        if row:
            self.am = row.CurrentBalance
            self.wam = int(input('Enter withdrawal amount: '))
            if self.am >= self.wam:
                self.am -= self.wam
                self.cursor.execute("UPDATE Accounts SET CurrentBalance = ? WHERE AccountNumber = ?", (self.am, self.no))
                self.conn.commit()
                print('Withdrawal successful.')
                self.out()
            else:
                print('Insufficient funds')
        else:
            print('Account not found.')

    def quit(self):
        self.conn.close()
        print('Thank you for using our banking service.')

# Run the program
bank = Bank()
bank.func()
