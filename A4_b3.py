def trim_unique_character(statement):
    unique_string = ""
    for i in range(len(statement)):
        if statement[i] not in unique_string:
            unique_string = unique_string+statement[i]
    return unique_string

ch=trim_unique_character('renukeerthana')
print(ch)

def occurances_in_statement(statement,search_string):
    count = 0
    words = statement.split(" ")
    for word in  words:
        if search_string in word:
            count = count + 1
    return count

def occurances_in_word(word,search_string):
    count = 0
    for i in range(len(word)):
        if search_string == (word[i]):
            count = count + 1
    return count

def compress(statement):
    compressed_string=""
    unique_string = trim_unique_character(statement)
    for letters in unique_string:
        counter=occurances_in_word(statement,letters)
        compressed_string= compressed_string+ f"{letters}{counter}"
        #print(compressed_string)
    return compressed_string

statement = "aaabbccdddd"
print(compress(statement))






