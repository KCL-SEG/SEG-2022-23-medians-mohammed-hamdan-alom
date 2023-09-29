"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(list1):

    list1.sort()

    n = len(list1)

    if n % 2 != 0:
        return list1[n // 2]
    else:
        return (list1[n // 2] + list[n // 2 - 1]) / 2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

#print(numbers)
print(median(numbers))