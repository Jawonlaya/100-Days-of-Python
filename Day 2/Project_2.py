
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!\n")
total_Bill = float(input("What was the total bill? $")) #take bill input as a float
tip = float(input("What percentage of tip would you like to give? 10, 12, or 15? ")) #take tip input as a float
bill_Split = int(input("How many people to split the bill? ")) #take bill share input as an integer

#Calculate total bill to include intended tip
total_With_Tip = tip / 100 * total_Bill

# Add all bill
total = total_Bill + total_With_Tip

# Split bill between customers
div_Bill = total/bill_Split

# Round total bill to two decimal places
final_Total = round(div_Bill, 2)
final_Total = "{:.2f}".format(div_Bill)

#output total bills
print(f"Each person should pay ${final_Total}")
