
import random

# checking even or odd for multiple numbers.
def even_or_odd(number):
    for n in number:
        if n % 2 == 0:
            print (f"{n} is even")
        else:
            print (f"{n} is odd")
even_or_odd([12,10,5])

# checking even or odd with single number.
def even_or_odd(number):
    if number % 2 == 0:
        print (f"{number} is even")
    else:
        print (f"{number} is odd")
even_or_odd(6)


# Adding two numbers
def add(a,b,c):
    result = a + b + c
    print (f"sum is {result}")
add(10,20,30)


def add(a,b):
    return  a + b
print(add(10,20))


#rock paper
def get_choices():
    player_choice="rock"
    computer_choice="paper"
    return player_choice,computer_choice
choices,player=get_choices()
print (choices,player)


def get_choices():
    player_choice=input("Enter your choice:(rock,paper,scissor) ")
    options=["rock","paper","scissor"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices
choices=get_choices()
print(choices)
