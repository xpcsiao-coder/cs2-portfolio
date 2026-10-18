price = float(input("Enter item price: "))

quantity = int(input("Enter quantity: "))

payment = float(input("Enter amount paid: "))

def calculate_total(price, quantity):
  return price * quantity

total = calculate_total(price, quantity)

def calculate_change(payment, total):
  if payment >= total:
    return payment - total
  else:
    return total - payment

change = calculate_change(payment, total)

print("Total Cost: PHP", total)

if payment >= total:
    print("Change: PHP", change)
else:
    print("Additional Amount Needed: PHP", change)

# 1. calculate_total() multiplies the price by the quantity to get the total, while calculate_change() subtracts the payment and total or vice versa for the change or shortage.

# 2. Parameters are the variables inside the function, while arguments are the actual values passed to the function, for example; price and quantity are parameters, while 35 and 3 are arguments when calling calculate_total(35, 3).

# 3. The returned total is stored in the variable 'total', then, it is reused in calculate_change() and when displaying the cost.

# 4. Separating the calculations makes the program easier to read, test, and fix.
