"""
- Must include 1 class
- Must have some sort of main menu and accept user input to route logic flow
- Needs to have the following functionality:
   - Check Balance
   - Deposit
   - Withdrawal
   - Exit
- Must manage balance accurately (balance should reflect transactions).
"""
class Wallet():

   def squiggly(self):
      print('\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.\n')

   def main_menu(self):
      Wallet.squiggly(self)
      menu_select = input('What would you like to do?\n\n (1) Check Balance | (2) Deposit | (3) Withdrawal | (4) Exit | >>> ').lower()
      #print(menu_select) # for debugging - remove before submission

      if menu_select == '4' or menu_select == 'exit':
         Wallet.leave_menu(self) # important to self reference

      elif menu_select == '1' or menu_select == 'check balance' or menu_select == 'balance':
         Wallet.check_balance(self)

      elif menu_select == '2' or menu_select == 'deposit':
         Wallet.deposit(self) 

      elif menu_select == '3' or menu_select == 'withdraw' or menu_select == 'withdrawal':
         Wallet.withdrawal(self) 

      else:
         print('Something else happened...')
         exit()

   def balance_query(self):
      balance_object = open('wallet_data.py', 'r+')
      data = balance_object.read()
      data = float(data)
      print_data = str(format(data, '.2f'))
      deposit_question = '\nYour balance: $' + print_data
      balance_object.close()
      return deposit_question

   def balance_data(self):
      balance_object = open('wallet_data.py', 'r+')
      data = float(balance_object.read())
      balance_object.close()
      return data

   def check_balance(self):
      data = Wallet.balance_data(self)

      if data == 0:
         print('\nDude, you\'re just broke.')
         Wallet.main_menu(self)

      if data > 0 and data < .01:
         print('\nYou are close to broke: $' + str(format(data, '.2f')))
         Wallet.main_menu(self)

      elif data > 1e+46:
         print('\nYou have a grossly large amount of money: $' + str(format(data, '.2f')))
         Wallet.main_menu(self)

      else:
         print(self.balance_query())
         Wallet.main_menu(self)

      Wallet.squiggly(self)

      print(result)
      balance_object.close()
      print('\n*\n*\n*\n')
      Wallet.main_menu(self)


   def deposit(self): # oh no I broke my deposit
      print(self.balance_query())
      data = Wallet.balance_data(self)
      deposit_request = input('\nHow much would you like to deposit? | >>> $')

      try:
         val = round(float(deposit_request), 2)

         if val < 0:
            print('\nThis is not a valid deposit amount, my dude.')
            Wallet.squiggly(self)
            Wallet.deposit(self)

         elif val >= 0:
            new_balance = data + val
            file = open('wallet_data.py', 'r+')
            file.write(str(new_balance))

            print('\nYou deposited: $' + str(format(val, '.2f')))
            file.close()
            print(self.balance_query() + '\n')
            Wallet.main_menu(self)
         
         else:
            print(self.balance_query())
            Wallet.main_menu(self)

      except ValueError:
         print("Input was not a valid number.")
         Wallet.deposit(self)

      balance_object.close()

   def withdrawal(self):
      print(self.balance_query())
      data = Wallet.balance_data(self)
      deposit_request = input('\nHow much would you like to withdraw? | >>> $')

      try:
         val = round(float(deposit_request), 2)

         if val > data:
            print('\nYou don\'t have enough money to withdraw that much!')
            Wallet.withdrawal(self)

         elif val < 0:
            print('\nThis is not a valid withdrawal amount, my dude.')
            Wallet.squiggly(self)
            Wallet.deposit(self)

         elif val >= 0:
            new_balance = data - val
            file = open('wallet_data.py', 'r+')
            file.write(str(new_balance))

            print('\nYou withdrew: $' + str(format(val, '.2f')))
            file.close()
            print(self.balance_query() + '\n')
            Wallet.main_menu(self)
         
         else:
            print(self.balance_query())
            Wallet.main_menu(self)

      except ValueError:
         print("Input was not a valid number.")
         Wallet.deposit(self)

      balance_object.close()
   

   def leave_menu(self):
      print('\n*closes wallet*\n')
      exit()
   

   def __str__(self):
        heredoc = f'''
        A simple Python-powered wallet.
        '''.strip()

   def __init__(self):
      print('\nHello, PyWallet here.')
      Wallet.main_menu(self)
   

Wallet()