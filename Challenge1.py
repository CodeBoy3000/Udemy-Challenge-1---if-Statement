name = input("Please enter your name! ")
age = int(input("Please enter your age! "))

if age == 17:
    print("Sorry, you ain't old enough {0}.".format(name))
    print("Come back in {0} year.".format(18 - age))
elif age < 17:
    print("Sorry, you ain't old enough {0}.".format(name))
    print("Come back in {0} years.".format(18 - age))
elif age > 30:
    print("Sorry {0} but you are too old to come on holiday!".format(name))
else:
    print("Welcome aboard {0}!".format(name))