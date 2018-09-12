#!/usr/bin/env python3

wake = { "5": "45",
        "6": "60",}
# Add fifteen minutes

age = input("How old is your child? ")
wakeTime = input("When does your child need to wake? [H:MM] ")
wakeTime = wakeTime.split(':')
age = int(age)

if age == 5:
    min = int(wakeTime[1]) + 45
elif age >= 5:
    min = int(wakeTime[1]) + 45 + (( int(age) - 5 ) * 15) 
# elif age <= 5:
#    print("You should find a different chart")

bedTime = divmod(min, 60) 
print("A child of " + str(age) + " should go to bed at " + str((int(bedTime[0] + int(wakeTime[0])))) + ':' + str(bedTime[1])  )
