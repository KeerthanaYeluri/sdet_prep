
# finding the smallest number
num=[9,45,3,2,0]
smallest_num=num[0]
for number in num:
    if number < smallest_num:
        smallest_num=number
print(smallest_num)


# second_smallest_number

num=[0,99,67,3,2]
smallest_num=min(num)
second_smallest_num = None
for num in num:
    if num!=smallest_num:
        if second_smallest_num is None or num < second_smallest_num:
            second_smallest_num=num
print(second_smallest_num)


# third_smallest_number
num=[0,88,78,65,4]
smallest_num=min(num)
second_smallest_num=None
for number in num:
    if number!=smallest_num:
        if second_smallest_num is None or number<second_smallest_num:
            second_smallest_num=number
third_smallest_num=None
for number in num:
    if number!=smallest_num and number!=second_smallest_num:
        if third_smallest_num is None or number<third_smallest_num:
            third_smallest_num=number
print(third_smallest_num)


# we can find whatever smallest_number that we can.

numbers = [0, 88, 78, 65, 4]
n = int(input("Enter n value: "))
unique_numbers = sorted(set(numbers))
if n <= len(unique_numbers):
    print(f"{n}th smallest number is:", unique_numbers[n-1])
else:
    print("Not enough numbers")