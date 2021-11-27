import random


Secrete_num = random.randint(1, 50)
guess = int(input("Guess a number between 1 to 50: "))
count = 1
while Secrete_num != guess:
    if Secrete_num > guess:
        print("Sorry wrong number too Low, try again")
        count += 1
    else:
        print("Sorry wrong number too High, try again")
        count += 1
    guess = int(input("Enter a guess number: "))
if Secrete_num == guess:
    print("You got it right!", "\n" "you answered it in " +
          str(count) + " tries")
