# Pricing & fees (constants)
base_ticket_price = 12.00    # $ per ticket
service_fee       = 1.50     # flat service fee per order

# 1. calculate_subtotal: returns subtotal for given qty of tickets
def calculate_subtotal(qty):
    return base_ticket_price * qty

# 2. determine_age_discount: returns discount amount based on age
def determine_age_discount(subtotal, age_group):
    if age_group == 'child':   # under 12
        return subtotal * 0.50  # 50% off
    elif age_group == 'senior': # 65 and over
        return subtotal * 0.30  # 30% off
    else:
        return 0.00            # no discount

# 3. apply_weekday_discount: $2 off per ticket on weekdays (Mon–Thu)
def apply_weekday_discount(qty, day_of_week):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
    return 2.00 * qty if day_of_week in weekdays else 0.00

# 4. calculate_total: returns (total, subtotal, age_disc, weekday_disc, service_fee)
def calculate_total(qty, age_group, day_of_week):
    subtotal      = calculate_subtotal(qty)
    age_discount  = determine_age_discount(subtotal, age_group)
    weekday_disc  = apply_weekday_discount(qty, day_of_week)
    net           = subtotal - age_discount - weekday_disc
    total         = net + service_fee
    return total, subtotal, age_discount, weekday_disc, service_fee

# 5. process_orders: iterates orders and prints summary
def process_orders(orders):
    for i, order in enumerate(orders, start=1):
        qty, age_group, day = order
        total, subtotal, age_disc, wd_disc, fee = calculate_total(qty, age_group, day)
        print(f"Order {i}: qty={qty}, age={age_group}, day={day} -> \
              subtotal=${subtotal:.2f}, age_disc=${age_disc:.2f}, \
              weekday_disc=${wd_disc:.2f}, fee=${fee:.2f}, total=${total:.2f}")

# Main program
if __name__ == "__main__":
    # orders: (quantity, age_group, day_of_week)
    orders = [
        (4, 'adult', 'Friday'),
        (2, 'child', 'Wednesday'),
        (3, 'senior', 'Monday'),
        (1, 'adult', 'Tuesday'),
        (5, 'child', 'Saturday')
    ]
    process_orders(orders)