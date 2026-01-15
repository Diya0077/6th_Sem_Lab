name = input("Enter your name: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Hello,", name)

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1-num2}")
print(f"Multiplication: {num1*num2}")
print(f"Division: {num1/num2}")
print(f"Integer Division: {num1//num2}")
print(f"Modulo: {num1%num2}")
print(f"Exponentiation: {num1**num2}")


import statistics

def compute_summary_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)

    try:
        mode = statistics.mode(data)

    except statistics.StatisticsError:
        mode = "No unique mode found"

    std_dev = statistics.stdev(data)
    variance = statistics.variance(data)
    return mean, median, mode, std_dev, variance


n = int(input("Enter the count of numbers: "))

numbers = []
for i in range(n):
    a = int(input("Enter the number: "))
    numbers.append(a)

print("Numbers:", numbers)

mean, median, mode, std_dev, variance = compute_summary_statistics(numbers)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std_dev)
print("Variance:", variance)