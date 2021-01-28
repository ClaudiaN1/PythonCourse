# ask for a name and an age. When both values have been entered,
# check if the person is the right age to go on on an 18-30 holiday.
# They must be over 18 and under 31. If they are, welcome them to the
# holiday, otherwise print a, hopefully, polite message refusing them entry.

name = input("Please enter your name: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome club 18-30 holidays, {0}".format(name))
else:
    print("I'm sorry, our holidays are only for cool people")