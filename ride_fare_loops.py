# Pricing parameters
base_rate_per_mile   = 1.25    # $ per mile
base_rate_per_minute = 0.25    # $ per minute
peak_hours_morning   = range(7, 10)   # 7–9 AM
peak_hours_evening   = range(17, 20)  # 5–7 PM
peak_multiplier      = 1.5     # 50% surge
service_fee          = 2.00    # flat fee per ride

# Sample rides: (distance_mi, duration_min, start_hour)
rides = [
    (3.2, 12, 8),    # morning peak
    (5.0, 20, 14),   # off-peak
    (2.5, 15, 18),   # evening peak
    (10.0, 25, 22),  # late night
    (1.0, 5, 9)      # edge of peak
]

# 1. Calculate total revenue using a while loop
index = 0
total_revenue = 0.0
while index < len(rides):
    dist, dur, hour = rides[index]
    base_fare = dist * base_rate_per_mile + dur * base_rate_per_minute
    multiplier = peak_multiplier if (hour in peak_hours_morning or hour in peak_hours_evening) else 1.0
    fare = base_fare * multiplier + service_fee
    total_revenue += fare
    index += 1
print(f"Total revenue: ${total_revenue:.2f}")

# 2. Compute total distance and average speed using a for loop
total_distance = 0.0
total_time = 0.0
for dist, dur, hour in rides:
    total_distance += dist
    total_time += dur
average_speed = total_distance / (total_time / 60)  # miles per hour
print(f"Total distance: {total_distance:.1f} miles")
print(f"Average speed: {average_speed:.1f} mph")