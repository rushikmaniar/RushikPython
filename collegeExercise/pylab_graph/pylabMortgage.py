import pylab

def findPayment(loan,r,m):
    return loan * (((r)*(1+r)**m)/((1+r)**m-1))

class Mortgage(object):
    def __init__(self,loan,r,months):
        self.loan = loan
        self.rate = r/12.0
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan,self.rate,months)
        self.legend = None

    def makePayment(self):
        self.paid.append(self.payment)
        redustion = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - redustion)