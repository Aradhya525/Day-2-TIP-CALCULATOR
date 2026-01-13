print("Welcome to TIP Calculator")
bill_amt = float(input("Enter the bill amount $"))
tip = int(input("What percentage tip would you like to give? 10% 15% 25%: %"))
people_number = int(input("Enter number of people paying the bill: "))
total_bill = bill_amt + bill_amt * (tip/100)  
bill_split = total_bill/people_number

print(f"Each person should pay {bill_split}")
