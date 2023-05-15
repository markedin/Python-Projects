
#import abc and abstractmethod
from abc import ABC, abstractmethod

#create abstract class called store
class store(ABC):
    #create method that outputs a string and takes in an amount
    def getTotal(self, amount):
        print("Your total for todays purchases: ", amount)
    #create abstract method called getInvoice
    @abstractmethod
    def getInvoice(self, amount):
            pass

#create another class to define implementation of its parents abstract method
class paymentOperation(store):
    #define how to implement getInvoice from store class
    def getInvoice(self, amount):
        print("Your invoice for todays transaction totals {} without tax.".format(amount))

#create an object that uses both parent and child methods
obj = paymentOperation()
obj.getTotal(200)
obj.getInvoice(200)
