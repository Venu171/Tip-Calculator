print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill?$ "))
tip=int(input("How much tip would you like to give? 10, 12, or 15?  "))
num_of_splits=int(input("How many people to split the bill? "))
final_bill_foreach_person=(total_bill+(tip/100)*total_bill)/num_of_splits
print(f"Each person should pay: ${final_bill_foreach_person:.2f}")
