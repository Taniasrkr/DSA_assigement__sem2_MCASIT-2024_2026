
# Write a function thant takes a list of integers as a parameters andd
# returns third smallest number from the list. For example,
# input:[34,89,54,20,50,76,10,45,90] output: 34

def third_smallest(numbers):
    numbers = sorted(numbers)
    return numbers[2]

nums = [34,89,54,20,50,76,10,45,90]
print(third_smallest(nums))