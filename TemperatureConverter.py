# This program will convert given temperatures to different measuring units

print("\nWelcome to the Temperature Conversion App")

temp_f = float(input("What is the temperature in Fahrenheit: "))

# Temperature Conversions
temp_c = (5/9) * (temp_f - 32)
temp_k = temp_c + 273.15

# Round Temperatures to 2 decimal places
temp_f = round(temp_f, 2)
temp_c = round(temp_c, 2)
temp_k = round(temp_k, 2)

# Display summary in a table

print("\nDegrees Fahrenheit:\t" + str(temp_f))
print("Degrees Celsius:\t" + str(temp_c))
print("Degrees Kelvin:\t\t" + str(temp_k))


