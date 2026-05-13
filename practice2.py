numbers=[5,2,5,2,2]
for x_count in numbers:
    print ('x' * x_count)


numbers=[2,4,6,8]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output += chr(ord("A") + count)
    print (output)



numbers=[3,5,7]
for x_count in numbers:
    output =''
    for count in range(x_count):
        output += 'x'
    print (output)