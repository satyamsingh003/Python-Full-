from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCard(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using credit card")


class UPI(Payment):
    def pay(self,amount):
        print(f"Paid {amount}  using UPI")

class Paypal(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using paypal")


payments={
    CreditCard(),
    UPI(),
    Paypal()
}

for payment in payments:
    payment.pay(500)


# hERE THE CALLER KNOWS ONLY PAY(). it doesn't know how each  payment method work internally. , this is termaed as abstraction


""" 
What if any class does not implement method pay() then it will throws an array as type error



Imagine you have 100 developers.

One developer creates:

class GooglePay(Payment):

Another creates:

class PhonePe(Payment):

Another creates:

class AmazonPay(Payment):

Even if different people build them, every class must implement:

pay()

Your application stays consistent.
"""


