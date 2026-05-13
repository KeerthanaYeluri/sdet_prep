# palindrome code
s="madam"
print(s==s[::-1])

#by using function
def palindrome(word):
    reversed_word=""
    for ch in word:
        reversed_word=ch+reversed_word
    return word==reversed_word
print(palindrome("madam"))


#by using if statements

def palindrome(text):
    reversed_palindrome=""
    for ch in text:
        reversed_palindrome=ch+reversed_palindrome
    if text==reversed_palindrome:
            return "palindrome"
    else:
            return "not palindrome"
print(palindrome("madam"))