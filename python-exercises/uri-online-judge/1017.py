consumption = 12

time_spent = input("Type the time spent in the trip")
average_speed = input("Type the average speed")

time_spent = int(time_spent)
average_speed = int(average_speed)

liters = time_spent*average_speed/consumption

print("%.3f" %liters)