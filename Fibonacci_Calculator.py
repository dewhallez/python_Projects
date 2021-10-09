# Fibonacci calculator

print("Welcome to the Fibonacci Calculator App")

number = int(input("\nHow many digits of the Fibonacci Sequence would you like to calculate: "))

# Fibonacci Algorithm
fibonacci = [1, 1]
for i in range(number - 2):
    temp = fibonacci[i] + fibonacci[i+1]
    fibonacci.append(temp)

# Display the sequence of numbers
print("\nThe first " + str(number) + " numbers of the Fibonacci Sequence are: ")
for numbers in fibonacci:
    print(numbers)

# Calculate the golden ratio
golden = []
for i in range(len(fibonacci) - 1):
    ratio = fibonacci[i+1] / fibonacci[i]
    golden.append(ratio)

# Display Golden ratio values
print("\nThe corresponding Golden Ratio values are: ")
for ratio in golden:
    print(ratio)


print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618.........")