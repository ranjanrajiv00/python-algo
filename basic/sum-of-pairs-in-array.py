def findPairs(numbers, value):
    hashMap = {}
    result = []

    for num in numbers:
        if value-num in hashMap:
            result.append([num, value-num])
        hashMap[num] = num
    return result
    
print(findPairs([9, 2, 4, 7, 5, 1, 3, 3, 6, 0], 6))