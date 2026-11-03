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
