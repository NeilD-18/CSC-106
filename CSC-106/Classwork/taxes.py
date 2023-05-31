meal_price = 44
tax_rate  = 0.08 
tip_rate = .20  
tax = 0.08 * meal_price
tip = 0.20 * meal_price

total = float(meal_price + (meal_price * tax_rate) + (meal_price * tip_rate))
total = round(total, 2)

print("Meal: $", meal_price)
print("Tax: $" , tax)
print("Tip: $" , tip)
print("Total: $" , total)