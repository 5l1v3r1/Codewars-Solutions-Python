'''
challenge URL : https://www.codewars.com/kata/558fc85d8fd1938afb000014
'''
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    sum = 0 
    for i in range(len(numbers)):
        if numbers[i] != numbers[i+1]:
           sum = numbers[i] + numbers[i+1]
           break
    return sum
    