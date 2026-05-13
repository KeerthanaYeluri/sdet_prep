string='anand'
search_string='a'
count=0
for i in range(len(string)):
    if search_string == (string[i]):
        count=count+1
print('search string found',count,'times')
print(f"search string found {count} times")



statement="this is how the things work there"
search_string="th"
count=0
words=statement.split(" ")
for word in words:
    if search_string in word:
        count=count+1
print(f"search string found {count} times")



def occurances_in_statement(statement,search_string):
    count = 0
    words = statement.split(" ")
    for word in  words:
        if search_string in word:
            count = count + 1
    return count

statement="this is how the things work there in the corporate"
search_string="th"
count=occurances_in_statement(statement,search_string)
print(f"search string found {count} times")
















