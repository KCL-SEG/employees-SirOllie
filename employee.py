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
                print(self.name + "'s salary is " + str((self.salary)+(self.commission_number*self.contract_worth)))
            else:
                print(self.name + "'s salary is " + (str(self.salary)))
        else:
            if self.commission_number > 0:
                print(self.name + "'s salary is " + str((self.salary*self.hours)+(self.commission_number*self.contract_worth)))
            else:
                print(self.name + "'s salary is " + str((self.salary*self.hours)))

    def __str__(self):
        if self.is_monthly == True:
            if self.commission_number > 0:
                exit
            else:
                print(self.name + " works on a monthly salary of " + str(get_pay()))
        else:
            if self.commission_number > 0:
                exit
            else:
                print(self.name + "works on a contract of " + str(self.hours) + " at " + str(self.salary) + "/hour. Their total pay is " + self.get_pay())


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

billie.get_pay()
charlie.get_pay()
renee.get_pay()
jan.get_pay()
robbie.get_pay()
ariel.get_pay()
billie.__str__()
