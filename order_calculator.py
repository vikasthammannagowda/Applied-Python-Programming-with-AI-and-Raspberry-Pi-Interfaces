# 1. Set up item costs and rates
book_price    = 12.99      # price per book (in $)
quantity      = 3          # how many books you want
shipping_cost = 4.50       # flat shipping fee
tax_rate      = 0.07       # 7% sales tax

# 2. Compute costs using arithmetic and assignment
subtotal = book_price * quantity       # multiplication
tax      = subtotal * tax_rate         # multiplication
total    = subtotal + shipping_cost    # addition
total   += tax                         # augmented assignment

# 3. Define your budget and compare
budget         = 50                    # your maximum spend
within_budget  = total <= budget       # relational comparison

# 4. Show results
print("Subtotal:        ", subtotal)
print("Tax:             ", tax)
print("Shipping:        ", shipping_cost)
print("Total cost:      ", total)
print("Within budget?   ", within_budget)
