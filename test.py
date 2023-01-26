def find_average(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum                 


print(find_average([1, 2, 3]), 'it is first test')
print(find_average([30, 50, 70, 90]), 'it is second test')
print(find_average([100, 100, 100]), 'it is third test')