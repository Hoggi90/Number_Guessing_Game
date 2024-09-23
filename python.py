import random

correct = "Well Done, You got it correct!"
higher = "Higher"
lower = "Lower"

random_number = random.randint(1, 100)

while True:
    prompt = input("Guess the number")
    if prompt < str(random_number):
        print(higher)
        
    elif prompt > str(random_number):
        print(lower)

    elif prompt == str(random_number):
        print(correct)
        break

