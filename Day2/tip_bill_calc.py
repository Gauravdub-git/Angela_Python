print("Welcome to the tip bil calculator")

bill = float(input("What was the Total bil :- "))

tip = int(input("What percentage would you lie to give :- "))

people = int(input("How many people to split the bill? "))

bill_with_tip = bill + bill * tip / 100
bill_per_person = bill_with_tip / people 
final_amount = round(bill_per_person, 3)
final_amount= "{:.2f}".format(bill_per_person)

print(f"Each person should pay {final_amount}")

