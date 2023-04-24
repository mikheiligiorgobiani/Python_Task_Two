import random
number_random = random.randint(1,99)
user_number = int(input("please enter number:"))
while user_number != number_random:
    user_number = int(input("please enter number:"))
    if user_number == number_random:
        print("Congratulations! ")