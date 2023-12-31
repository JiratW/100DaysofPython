#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
pay_bill = round((bill + (bill * tip / 100))/people, 2)
#Transform format to 2 digits by use format
pay_bill_format = "{:.2f}".format(pay_bill) #Turn pay_bill to string with 2 decimal
print(f"Each person should pay: ${pay_bill_format}")
