s='aaaabbbccds'
previous=s[0]
output=''
c=1
i=1
while i<len(s):
    if s[i]==previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=s[i]
        c=1
    if i==len(s)-1:
        output=output+str(c)+previous
    i=i+1
print(output)




def trim_characters(word):
    unique_string=''
    for i in range(len(word)):
        if word[i] not in unique_string:
            unique_string=unique_string+word[i]
    return unique_string
ch=trim_characters('aaabbccd')
print(ch)





