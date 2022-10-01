class loanRate :
    interest = 0.9
    def __init__(self,fname,loan):
        self.fname = fname
        self.loan = int(loan)

    def loan_rate_calculation (self):
        x = self.loan * loanRate.interest
        print(f"loan rate : {self.fname} has a rate of interest equal {self.loan * loanRate.interest}")


p1  = loanRate("sarra",40000)
loanRate.interest = 0.2
p1.loan_rate_calculation()