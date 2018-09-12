#!/usr/bin/env python3

while True:
    value = input("How old are you? [q to quit]: ")
    if value == 'q': 
        break
    number = int(value)
    if number >= 35:
        print("Have another drink, you're old")
    elif number == 34:
        print("Meh, What's another year?")
    elif number == 33:
        print("Still time to learn Sumerian!")
    elif number == 32:
        print("Time to learn Sumerian!")
    elif number == 31:
        print("You are old enough to drink now....for ten years")
    elif number == 30:
        print("Three Decades. That's something")
    elif number <= 29:
        print("You are really young")
    print("HAPPY BIRTHDAY!")

