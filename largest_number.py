# finding maximum value
#from practice2 import count

numbers=[4,1,0,2,88,60]
max_value=numbers[0]
for number in numbers:
    if number > max_value:
        max_value=number
print (max_value)

#finding minimum value
numbers=[0,20,11,10]
min_value=numbers[0]
for number in numbers:
    if number<min_value:
        min_value=number
print (min_value)


#finding largest even number
numbers=[0,22,44,11]
largest_even_numbers=numbers[0]
for number in numbers:
    if number % 2 == 0 and number > largest_even_numbers:
        largest_even_numbers=number
print (largest_even_numbers)

#finding largest odd number
numbers=[0,11,31,44,55]
largest_odd_numbers=numbers[0]
for number in numbers:
    if number%2!=0 and number > largest_odd_numbers:
        largest_odd_numbers=number
print (largest_odd_numbers)


#finding smallest number
numners=[33,2,12,90]
smallest_number=numners[0]
for number in numners:
    if number < smallest_number:
        smallest_number=number
print (smallest_number)
#finding second smallest number
second_smallest_number=None
for number in numners:
    if number!=smallest_number:
        if second_smallest_number is None or number < second_smallest_number:
            second_smallest_number=number
print (second_smallest_number)

#finding third smallest number
Third_smallest_number=None
for number in numners:
    if number!=smallest_number and number!=second_smallest_number:
        if Third_smallest_number is None or number < Third_smallest_number:
            Third_smallest_number=number
print(Third_smallest_number)

#counting the numbers which were greater than 10
numbers=[90,2,3,44,52]
count=0
for number in numbers:
    if number>10:
        count+=1
print (count)






