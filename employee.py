"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, is_monthly, hours, salary, commission_number, contract_worth):
        self.name = name
        self.is_monthly = is_monthly
        self.hours = hours
        self.salary = salary
        self.commission_number = commission_number
        self.contract_worth = contract_worth

    def get_pay(self):
        if self.is_monthly == True:
            if self.commission_number > 0:
                return ((self.salary)+(self.commission_number*self.contract_worth))
            else:
                return (self.salary)
        else:
            if self.commission_number > 0:
                return ((self.salary*self.hours)+(self.commission_number*self.contract_worth))
            else:
                return (self.salary*self.hours)

    def __str__(self):
        if self.is_monthly == True:
            if self.commission_number > 1:
                return (self.name + " works on a monthly salary of " + str(self.salary) + " and receives a commission for " + str(self.commission_number) + " contract(s) at " + str(self.contract_worth) + "/contract.  Their total pay is " + str(self.get_pay()) + ".")
            elif self.commission_number == 1:
                return (self.name + " works on a monthly salary of " + str(self.salary) + " and receives a bonus commission of " + str(self.contract_worth) + ".  Their total pay is " + str(self.get_pay()) + ".")
            else:
                return (self.name + " works on a monthly salary of " + str(self.salary) + ". Their total pay is "+ str(self.get_pay()) + ".")
        else:
            if self.commission_number > 1:
                return (self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.salary) + "/hour and receives a commission for " + str(self.commission_number) + " contract(s) at " + str(self.contract_worth) + "/contract.  Their total pay is "+str(self.get_pay()) + ".")
            elif self.commission_number == 1:
                return (self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.salary) + "/hour and receives a bonus commission of " + str(self.contract_worth) + ".  Their total pay is "+str(self.get_pay()) + ".")
            else:
                return (self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.salary) + "/hour.  Their total pay is " + str(self.get_pay()) + ".")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 0, 4000, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 100, 25, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 0, 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 0, 2000, 1, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 120, 30, 1, 600)
