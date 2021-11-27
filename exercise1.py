
answer3 = "UNIX"
answer4 = "Hardware"
answer5 = "DVD drive"
answer6 = "Brain"
answer7 = "PC"
answer8 = "Central processing unit"

count = 0


question1 = input("CPU is the _____ of computer. ")
if question1 == answer6:
    print(answer6, " is the correct answer")

    count += 1
else:
    print("Wrong! the correct answer is ", answer6)
    count -= 1
question2 = input("A desktop computer is also known as: ")
if question2 == answer7:
    print(answer7, "is the correct answer")
    count += 1
else:
    print("Wrong! the correct answer is ", answer7)
    count -= 1

question3 = input("CPU is an abbreviation for?")
if question3 == answer8:
    print(answer8, "is a correct answer")
    count += 1
else:
    print("Wrong, the correct answer is ", answer8)

question4 = input("Where is the DVD disk put in a computer?: ")
if question4 == answer5:
    print(answer5, " is correct")
    count += 1
else:
    print("Wrong! the correct answer is ", answer5)

question5 = input("Moderm is a: ")
if question5 == answer4:
    print(answer4, " is correct")
    count += 1
else:
    print("Wrong! the correct answer is", answer4)
    count -= 1

question6 = input("Shell is the exclusive feature of?: ")
if question6 == answer3:
    print(answer3, " is the correct answer")
    count += 1
else:
    print("Wrong! the correct answer is ", answer3)
    count -= 1

print("You got", count, "out of 6 correct!")
