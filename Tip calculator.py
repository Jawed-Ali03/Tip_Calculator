print("Welcome to the tip calculator!")
total_Bill=float(input("What was the total bill?"))
tip_Given=float(input("How much tip would you like to give? 10, 12 or 15?"))
bill_Split=float(input("How many people to split the bill?"))
new_Total_Bill= total_Bill *(1+(tip_Given/100))
final_Value = new_Total_Bill / bill_Split
print(f"Each person should pay: {round(final_Value,2)}")
