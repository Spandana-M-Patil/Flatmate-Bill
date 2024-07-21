from flat import Bill, Flatmate
from report import GeneratePdf

# Getting the total bill amount and the days for the bill is.
the_bill = float(input('Hey user, Enter the bill amount: '))
period = input('What is the bill period ?(E.g : January 2024) ')
bill_obj = Bill(amount= the_bill, period= period)

# Taking flatmates details 
flatmate1_name = input('What is your name? ')
fl_days = int(input('How many days you spent in the flat during the bill period? '))
flatmate1 = Flatmate(name= flatmate1_name, days_in_flat= fl_days)

flatmate2_name = input('What is the name of the other flatmate? ')
flatmate2_days = int(input(f'How many days {flatmate2_name} spent in the flat during the bill period? '))
flatmate2 = Flatmate(name= flatmate2_name, days_in_flat= flatmate2_days)

# Calculating both flatmates share
flatmate1_pay  = flatmate1.pays(bill= bill_obj, flatmate2= flatmate2)
flatemate2_pay = flatmate2.pays(bill= bill_obj, flatmate2= flatmate1)

# Displaying their share on the screen 
print(f'{flatmate1.name} pays: {flatmate1_pay}')
print(f'{flatmate2.name} pays: {flatemate2_pay}')

# creating the instance for generating pdf
createPdf = GeneratePdf(f'{period}.pdf')
createPdf.generate(flatmate1=flatmate1,flatmate2=flatmate2, bill= bill_obj)