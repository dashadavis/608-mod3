<<<<<<< HEAD
##Python Object representing a purchase for a given amount
#Dasha Davis

class Purchase(object):
    def __init__(self, amount):
       self.amount = amount

    def calculateTax(self, taxPercent):
       return self.amount * taxPercent/100.0

    def calculateTip(self, tipPercent):
       return self.amount * tipPercent/100.0

    def calculateTotal(self, taxPercent, tipPercent):
       return self.amount * (1 + taxPercent/100.00 + tipPercent/100.0)

#Create Purchase object given amount
purchase = Purchase(100.0)

#Set the tax and tip percentages
taxPercent = 7.5
tipPercent = 20.0

#Use the object to calculate tax and tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

#Display some useful information
print('Tax: ',tax)
print('Tip: ',tip)
print('Total: ',purchase.calculateTotal(taxPercent, tipPercent)) 







=======
>>>>>>> 524b6baf480efbbb47f365e1c466bab85fcb2367

