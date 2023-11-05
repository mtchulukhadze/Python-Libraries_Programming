import pyodbc
import pandas as pd

user = 'DESKTOP-3QJN7S3'+"\)" + "user" 

user_rep = user.replace(")" , "")

conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=DESKTOP-3QJN7S3;" 
                      f"uid={user_rep};"
                      "Database = BANK_MANAGEMENT_SYSTEM;" 
                      "Trusted_Connection=yes;")

def openaccount():
    name = input('enter name')
    acc_no = input('enter account number')
    dob = input('enter dob')
    address = input('enter address')
    contactn = input('contact number')
    opening_bal = int(input('enter opening balance'))
    data1 = (name, acc_no, dob, address, contactn, opening_bal)
    sql1 = ('insert into BANK_MANAGEMENT_SYSTEM.dbo.accoount_table values (?, ?, ?, ?, ?, ?)')
    conn.execute(sql1, data1)
    conn.commit()
    print('Data eneterd successfully.')


def customerdetails():
   acc_no = str(input('eneter account number:'))
   sql1 = """SELECT * FROM BANK_MANAGEMENT_SYSTEM.dbo.accoount_table WHERE acc_no = ?"""
   cursor = conn.cursor()
   cursor.execute(sql1, acc_no)
   out = cursor.fetchall()
   if not out:
      print('account not fount')
   else:
      print(out)


def depositeamount():
   amount = int(input('enter amount  to deposit'))
   acc_no = input('which account tou want to deposit')
   acc_add_amount = """select opening_bla from BANK_MANAGEMENT_SYSTEM.dbo.accoount_table where acc_no = ?"""
   cursor = conn.cursor()
   cursor.execute(acc_add_amount, acc_no)
   result = cursor.fetchone()
   opening_bla = int(result.opening_bla)

   new_balance = opening_bla + int(amount)

   update = ('update BANK_MANAGEMENT_SYSTEM.dbo.accoount_table set opening_bla = ? where acc_no = ?')
   cursor.execute(update, (new_balance, acc_no))
   conn.commit()

   print(f'new balance is {new_balance}')


def payment():
   groccery = input('you want to buy (y/n)')
   acc_no = input('enter your account_no')
   if groccery == 'y':
      print('''
            please take a item:
               1. item1: price 50$
               2. item2: price 100$
            ''')
      choice = input('enter choice')
      paied = 0

      if choice == '1':
         paied = 50
      elif choice == '2':
         paied = 100
   else:
      print('no item')

   acc_amount = 'select opening_bla from BANK_MANAGEMENT_SYSTEM.dbo.accoount_table where acc_no =?'
   cursor = conn.cursor()
   cursor.execute(acc_amount, (acc_no,))
   result = cursor.fetchone()

   current_balance = result.opening_bla
   available_balance = current_balance - paied

   update = 'update BANK_MANAGEMENT_SYSTEM.dbo.accoount_table set opening_bla = ? where acc_no = ?'
   cursor.execute(update, (available_balance, acc_no))
   cursor.commit()

   print(f'your available balance is {available_balance}')


def balance():
   print(pd.read_sql_query('SELECT * FROM BANK_MANAGEMENT_SYSTEM.dbo.accoount_table', conn))
   

def main():
    print('''
        1. open account
        2. deposite amount
        3. payment
        4. balance 
        5. customer details
        6. close account
    ''')
    choice  = input('enter the task')
    if choice == '1':
       openaccount()
    elif choice == '2':
       depositeamount()
    elif choice == '3':
       payment()
    elif choice == '4':
       balance()
    elif choice == '5':
       customerdetails()
    else:
       print('error')
if __name__ == '__main__':
   main()
