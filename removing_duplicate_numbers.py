
#Removing duplicate numbers
numbers=[92,2,2,4,4,7,7,0,10]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print (unique)



try:
    age=int(input('Age: '))
    print(age)
except ValueError:
    print('invalid value')

