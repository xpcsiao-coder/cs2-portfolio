# **GUIDE QUESTIONS⋆⭒˚.⋆**

## 1. What does each function do?
> calculate_total() multiplies the price by the quantity to get the total, while calculate_change() subtracts the payment and total or vice versa for the change or shortage.

## 2. What is the difference between the parameters price and quantity and the actual arguments passed
to the function? 
> Parameters are the variables inside the function, while arguments are the actual values passed to the function, for example; price and quantity are parameters, while 35 and 3 are arguments when calling calculate_total(35, 3).

## 3. Where is the returned total stored, and how is it reused?
> The returned total is stored in the variable 'total', then, it is reused in calculate_change() and when displaying the cost.

## 4. Why is it useful to separate total calculation from change calculation? 
> Separating the calculations makes the program easier to read, test, and fix.
