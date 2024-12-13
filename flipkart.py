import time

class Flipkart:
    url = 'www.flipkart.com'
    items = {'shoes': [10, 2000], 'shirts': [20, 300], 'pants': [10, 500]}
    
    def __init__(self, c_name, c_acc, c_bal, upi_id, upin, dcno, dpin):
        self.c_name = c_name
        self.c_acc = c_acc
        self.c_bal = c_bal
        self.upi_id = upi_id
        self.upin = upin
        self.dcno = dcno
        self.dpin = dpin
        self.cart = []
        self.amt = 0  

    def check_out(self):
        print(list(Flipkart.items.keys()))
        while True:
            item = input('Select your item (or type "exit" to proceed to payment): ')
            if item == 'exit':
                print("Your cart:", self.cart)
                print('1. COD', '2. PhonePe or GPay', '3. Debit card','4. Return','5. Cancel',  sep='\n')
                payment_option = int(input('Enter your payment option: '))
                return self.buy(payment_option)
            if item in Flipkart.items and Flipkart.items[item][0] > 0:
                Flipkart.items[item][0] -= 1
                self.cart.append(item)
                self.amt += Flipkart.items[item][1]
                print(f"{item} added to cart. Total amount: {self.amt}")
                print('Enter "exit" to proceed to payment.')
            else:
                print('Item not available or out of stock.')
                break
        # else:
        #     print('Thank you for shopping 😊')

    def buy(self, pay):
        if pay == 1:
            print(f'Your total amount to be paid is {self.amt}. Payment on delivery selected.')
            return

        attempts = 0
        max_attempts = 3

        if pay == 2:
            print(f'Your UPI ID is {self.upi_id}')
            while attempts < max_attempts:
                pin = input("Enter your UPI PIN: ")
                if pin == str(self.upin):
                    print("Payment done. Thank you 😊")
                    return
                else:
                    attempts += 1
                    print("Incorrect PIN.")
                    if attempts == max_attempts:
                        print("Too many incorrect attempts. Please wait 30 seconds.")
                        time.sleep(30)
                        attempts = 0

        elif pay == 3:
            print(f'Your Debit Card number is {self.dcno}')
            while attempts < max_attempts:
                pin = input("Enter your card PIN: ")
                if pin == str(self.dpin):
                    print("Payment done. Thank you 😊")
                    return
                else:
                    attempts += 1
                    print("Incorrect PIN.")
                    if attempts == max_attempts:
                        print("Too many incorrect attempts. Please wait 30 seconds.")
                        time.sleep(30)
                        attempts = 0
        elif pay==4:
            return self.return_item()
        elif pay==5:
            return self.cancel()
        else:
            print('Invalid payment option.')
        print('Thank you for shopping with us.')

    def return_item(self):
        print('select item to return')
        item_item=input('--')
        self.cart.remove(item_item)
        Flipkart.items[item_item][0]+=1
        print(f'your cart {self.cart}')
    def cancel(self):
        print('You have cancelled your order')
        self.cart.clear()

user= Flipkart('User', 2213213221, 20000, '12345', '1111', '32213221', '321321')
user.check_out()
