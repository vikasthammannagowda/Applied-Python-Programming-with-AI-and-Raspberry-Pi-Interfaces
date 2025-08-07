# 1. Get user inputs
book_price    = float(input("Enter the price per book ($): "))
quantity      = int(input("Enter the quantity of books: "))
shipping_cost = float(input("Enter the flat shipping cost ($): "))
tax_rate      = float(input("Enter the tax rate as a decimal: "))

# 2. Compute subtotal
subtotal        = book_price * quantity

# 3. Apply discount based on subtotal
if subtotal >= 100:
    discount_rate = 0.10   # 10% discount
elif subtotal >= 50:
    discount_rate = 0.05   # 5% discount
else:
    discount_rate = 0.0    # no discount
discount        = subtotal * discount_rate

# 4. Compute tax and total
taxable_amount  = subtotal - discount
tax             = taxable_amount * tax_rate
total           = taxable_amount + tax + shipping_cost

# 5. Show results
print("Subtotal:", subtotal)
print("Discount rate used:", discount_rate)
print("Discount applied:", discount)
print("Total cost:", total)