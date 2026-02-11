a="listen"
b="silent"
print(sorted(a)==sorted(b))


#by using if statement
a="listen"
b="silent"
if sorted(a)==sorted(b):
    print("anagram")
else:
    print("not anagram")


#by using function
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram("listen", "silent"))


#using function with if condition
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return "Not an anagram (different lengths)"
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
        return "Yes, it is an anagram!"
    else:
        return "No, it is not an anagram."
print(is_anagram("listen", "silent"))
