#tip calcultor

print("Welcome to the tip calculator!")
bill=float(input("Enter your bill:"))
tip= int(input("Enter your tip percent: 10 , 12 ,15?"))/100
print(tip)
persons_numbers=int(input("Enter how many people:"))
total_tip=bill*tip
total_bill = bill+ total_tip
total_bill_per_person= total_bill/persons_numbers
print(total_bill_per_person)