def largest(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num

    return max

print(largest([9,2,3,100,20,190,60]))