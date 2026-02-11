def trim_unique_character(statement):
    unique_string=""
    for i in range(len(statement)):
        if statement[i] not in unique_string:
            unique_string=unique_string+statement[i]
    return unique_string
# ch=trim_unique_character("reeeeenu")
# print(ch)

def occurances_in_word(word,search_string):
    count=0
    for i in range(len(word)):
        if word[i]==search_string:
            count=count+1
    return count
# ch=occurances_in_word('this is renu',"k")
# print(ch)

def compress(statement):
    compressed_string=""
    unique_string=trim_unique_character(statement)
    for letter in unique_string:
        counter=occurances_in_word(statement,letter)
        compressed_string=compressed_string+f"{letter}{counter}"
    return compressed_string
statement="aaabbbcccdd"
print(compress(statement))




#by using dictionary

def copress(s):
    compressed_string={}
    for ch in s:
        if ch in compressed_string:
            compressed_string[ch]=compressed_string[ch]+1
        else:
            compressed_string[ch]=1
    return compressed_string
print(copress("ppplll"))





