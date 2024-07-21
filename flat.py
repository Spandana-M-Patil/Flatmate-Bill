class Bill:
    """
    Object that contains data, such as amount and period
    """
    def __init__(self, amount, period) -> None:
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates flatmate object for each who shares the flat and contain the details such as
    days spent in the flat and their name 
    """
    def __init__(self, name, days_in_flat) -> None:
        self.name = name
        self.days_in_flat = days_in_flat
    
    """
    Method that going to calculate each person bill based on how many days they spent
    """
    def pays(self, bill, flatmate2):
        person_share = (bill.amount / (self.days_in_flat + flatmate2.days_in_flat)) * self.days_in_flat
        return round(person_share, 2)