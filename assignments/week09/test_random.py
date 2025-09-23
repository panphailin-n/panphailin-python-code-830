import random

def test_random():
    random_number = random.randint(1,10)

    guess_number =int(input("Enter guess number is 1-10:"))
    guess_number =int(guess_number)

    if random_number == guess_number:
        return print("You can do it")
    if random_number < guess_number :
        print("Too much")
    if random_number > guess_number :
        print("Too law")
    else :
        print("Fasle") 

    print(random_number)
                  
test_random()