
class PaymentStratgey:
    def pay(self):
        pass
    
    
class CreditCardPayment(PaymentStratgey):
    
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")
    
    
class PayPalPayment(PaymentStratgey):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Paypal.")
    
class UPIPayment(PaymentStratgey):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")
        

class ShoppingCart:
    
    def __init__(self):
        self.amount = 0 
        self.payment_method = None
        
    def add_item(self,amount):
        self.amount += amount
        print(f"Item added. Total amount: ₹{self.amount}")
        
    def set_payment_method(self,method):
        self.payment_method = method
        
    def checkout(self):
        if not self.payment_method:
            print("Please select a payment method.")
        else:
            self.payment_method.pay(self.amount)
            print(f"Order of ${self.amount} is placed successfully!")
            self.ammount = 0
        
        
cart = ShoppingCart()
cart.add_item(500)
cart.add_item(1000)

# Choose payment method at runtime
cart.set_payment_method(CreditCardPayment())
cart.checkout()

# Now pay using PayPal without changing cart logic
cart.set_payment_method(PayPalPayment())
cart.checkout()
