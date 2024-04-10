import avg_speed_calculator

user_distance = float(input("Distance: "))
user_time = float(input("Time: "))
user_avg_speed = avg_speed_calculator.calculate_avg_speed(user_distance, user_time)

print(f"Your average speed: {user_avg_speed:.2f} km/h.")
