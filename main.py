import random


class CardAnatomy:

    list_of_card = {}

    def __init__(self):
        self.MII = '4'
        self.IIN = '00000'
        self.BIN = self.MII + self.IIN

    def create_account(self):
        account_identifier = str(random.randrange(0, 999999999)).zfill(9)
        # acc = int(account_identifier)
        # print(type(acc))
        # print((account_identifier))
        multiple_odd = account_identifier[0:9:2] # you have to multiply this plus 8
        # print(multiple_odd)
        y = 0
        for i in multiple_odd:
            if int(i)*2 < 10:
                y = y + int(i)*2
            else:
                y = y + (int(i) * 2 - 9)
        # print(y)

        even_numbers = account_identifier[1:9:2]
        # print(even_numbers) # just add this number, these are even numbers
        x = 0
        for i in even_numbers:
            x = x +int(i)
        # print(x) # here you add even number
        checksum1 = 10 - (x + y + 8) % 10 #here you have number of checksum without checking if its  10
        # print(checksum1)
        if checksum1 == 10:
            checksum = '0'
        else:
            checksum = str(checksum1)


        card_pin = str(random.randrange(0, 9999)).zfill(4)
        card_num = self.BIN + account_identifier + checksum
        CardAnatomy.list_of_card[card_num] = {'solde': 0, 'code': card_pin}

        print("Your card has been created")
        print("Your card number:")
        print(card_num)
        print("Your card number:")
        print(card_pin)

    def log_into_account(self, num_card, code_pin):
        if num_card in CardAnatomy.list_of_card and CardAnatomy.list_of_card[num_card]['code'] == code_pin:
            print("You have successfully logged in!")
            return True
        else:
            print("Wrong card number or PIN!")
            return False

    def manage_account(self, num_card):
        while True:
            print("1. Balance")
            print("2. Log out")
            print("0. Exit")
            mng_choice = input()
            if mng_choice == '1':
                print("Balance: ", CardAnatomy.list_of_card[num_card]['solde'])
            elif mng_choice == '2':
                print("You have successfully logged out!")
                break
            elif mng_choice == '0':
                exit(1)

    def transaction(self):
        while True:
            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit")
            trans_choice = input()
            if trans_choice == '1':
                self.create_account()
            elif trans_choice == '2':
                num_card = input("Enter your card number: ")
                code_pin = input("Enter your PIN: ")
                if self.log_into_account(num_card, code_pin):
                    self.manage_account(num_card)
            elif trans_choice == '0':
                break


my_card = CardAnatomy()
my_card.transaction()
