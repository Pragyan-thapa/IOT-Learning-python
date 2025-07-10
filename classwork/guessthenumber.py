import random
guess_number = int(input("Guess the number: "))
correct_number = random.randint(1,50)
gurss_count = 0
while guess_number != correct_number:
    print("wrong guess")
    if guess_number > correct_number and guess_number < 51:
        print("too high")
        guess_number = int(input("Guess the number: "))
        gurss_count += 1
    elif guess_number < correct_number and guess_number > 0:
        print("too low")
        guess_number = int(input("Guess the number: "))

        gurss_count += 1

    elif guess_number > correct_number:
        print("out of bound")
        guess_number = int(input("Guess the number: "))


if guess_number == correct_number:
    print("correct")
    gurss_count += 1
print("total guess count: ",gurss_count)