def reverse_string(text):
    reversed_string=""
    for ch in text:
        reversed_string=ch+reversed_string
    return reversed_string
print(reverse_string("toll"))


#without using function

s="renu"
print(s[::-1])

#by using if statements
def reverse(text):
    if text=="":
        return "string is empty"
    reversed_string = ""
    for ch in text:
        reversed_string=ch+reversed_string
    return reversed_string
print(reverse("toll"))