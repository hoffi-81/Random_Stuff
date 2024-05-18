import random 


my_number = input("Gues Number from 1 to 10: ")
random_number = random.randint(1, 10)


if int(my_number) == random_number:
     print("You are right, {} is the right number".format(my_number))
else:
     print("You guesed the number {} but it is {}".format(my_number, random_number))