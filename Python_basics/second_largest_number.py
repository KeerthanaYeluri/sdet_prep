#finding second-largest number

l = [1, 22, 33, 43, 50]
largest = second_largest = float('-inf')
for num in l:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("second largest", second_largest)

#by using function

def second_largest(l):
    largest = second_largest = float('-inf')
    for num in l:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest
numbers=[22,20,33,90]
result = second_largest(numbers)
print("second largest", result)
