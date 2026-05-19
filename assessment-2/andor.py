age = int(input("Enter your age: "))
has_id = input("Do you have an ID card? (yes/no): ").lower()

# Check using 'and' & 'or'
if age >= 18 and (has_id == "yes" or has_id == "y"):
    print("Allowed to Enter!")
else:
    print("Not Allowed!")