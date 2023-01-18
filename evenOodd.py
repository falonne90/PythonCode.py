
customer_number= int(input("what is your preferred number between 0 and 100?\n\n"))

if customer_number % 2 != 0: 
    print(f"your preferred number {customer_number} is an odd number.\n\n")

else:
    print(f"your preferred number {customer_number}is an even number.")