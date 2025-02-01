'''
Omar Ahmed (worked with Jessica Draper)
218709923
FINE 3300
February 3, 2025
'''

#Taking in user inputs
principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate as a number, not as a %: "))
ammortization = int(input("Enter the ammortization period (years): "))

#Declaring the denominator for the exponent when calculating the r-amount of different period
#Declaring the list that will contain the different r-values for the payment function,  to be indexed later
den_values = (12,24,26,52)
r_values = []

#Calculating the r-values for each period and appending into list
for value in den_values:
    temp_value = (1+(rate/100)/2)**(2/value)-1
    r_values.append(temp_value)

#This function takes in 3 inputs and calculates 5 calculations of different payments relative to the frequency of the payments
#principal is the borrowed amount, rate is the semi-annual interest rate, and period is the length of the loan. All are going to be user inputs. It will be assumed that the user will enter the correct amounts, so no error checking mechanism has been added
#:.2f part was added to force trailing zeroes, ChatGPT used for this as the typical round() function does not force trailing zeroes
def mortgage_payments(principal, rate, period):
    monthly = f"{(principal * r_values[0]) / (1 - (1 + r_values[0]) ** ((-period) * den_values[0])):.2f}"
    semi_monthly = f"{(principal * r_values[1]) / (1 - (1 + r_values[1]) ** ((-period) * den_values[1])):.2f}"
    biweekly = f"{(principal * r_values[2]) / (1 - (1 + r_values[2]) ** ((-period) * den_values[2])):.2f}"
    weekly = f"{(principal * r_values[3]) / (1 - (1 + r_values[3]) ** ((-period) * den_values[3])):.2f}"
    rapid_biweekly = f"{((principal * r_values[0]) / (1 - (1 + r_values[0]) ** ((-period) * den_values[0]))) / 2:.2f}"
    rapid_weekly = f"{((principal * r_values[0]) / (1 - (1 + r_values[0]) ** ((-period) * den_values[0]))) / 4:.2f}"
    return monthly, semi_monthly, biweekly, weekly, rapid_biweekly, rapid_weekly

# Printing each period's associated cost by indexing the tuple
results = mortgage_payments(principal, rate, ammortization)
print("Monthly Payment: $"+ results[0])
print("Semi-monthly Payment: $"+ results[1])
print("Bi-weekly Payment: $"+ results[2])
print("Weekly Payment: $"+ results[3])
print("Rapid Bi-weekly Payment: $"+ results[4])
print("Rapid Weekly Payment: $"+results[5])
