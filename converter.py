# This program will convert miles per hour to meters per second and kilometer per hour

# Welcome message
print("Welcome to the mileage converter App")

# Get user input
miles_per_hour = float(input("What is your speed in miles per hour: "))

# Meters Conversion calculation
miles_per_second = miles_per_hour * 0.4474
miles_per_second = round(miles_per_second, 2)

# Kilometer conversion calculation
kilometer_per_hour = miles_per_hour * 1.609344
kilometer_per_hour = round(miles_per_hour, 2)

# Display result to user
print("Your speed in meters per second is " + str(miles_per_second) + ".")
print("Your speed in kilometer per hour is " + str(kilometer_per_hour) + ".")


