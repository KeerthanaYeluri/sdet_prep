# counting no of particular characters in string by using for loop

name="reenu"
count=0
for i in range(len(name)):
    if name[i]=='e':
        count=count+1
print(count)


# keeping this for loop in function

def find_no_of_characters(name):
    count=0
    for i in range(len(name)):
        if name[i]=='r':
            count=count+1
    return count
ch=find_no_of_characters("reenu")
print(ch)


#using while loop

name="keerthana"
count=0
i=0
while i <len(name):
    if name[i]=='e':
        count=count+1
    i=i+1
print(count)


# keeping this while loop in function

def find_no_of_characters_in_while_loop(name):
    count=0
    i=0
    while i < len(name):
        if name[i]=='r':
            count=count+1
        i=i+1
    return count
ch=find_no_of_characters_in_while_loop("keerthana")
print(ch)


#counting no of characters in a string by using for loop
name="keerthana"
count=0
for i in range(len(name)):
    count=count+1
print(count)

#counting no of characters in a string by using for loop keeping this in function

def find_all(name):
    count=0
    for i in range(len(name)):
        count=count+1
    return count
ch=find_all(name)
print(ch)



#counting no of characters in string by using while loop

name='keerthana'
count=0
i=0
while i<len(name):
    count=count+1
    i=i+1
print(count)





