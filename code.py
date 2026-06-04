import random

score = 0
attempted = 0

with open("dataset.txt", "r") as file:
    questions = file.readlines()

random.shuffle(questions)

for line in questions:
    data = line.strip().split("|")

    print("\n" + data[0])
    print("A.", data[1])
    print("B.", data[2])
    print("C.", data[3])
    print("D.", data[4])

    answer = data[5]

    user = input("Enter option (A/B/C/D) or Q to quit: ").upper()

    if user == "Q":
        print("\nQuiz Ended by User.")
        break

    attempted += 1

    if user == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n===== QUIZ RESULT =====")
print("Questions Attempted:", attempted)
print("Correct Answers:", score)
print("Wrong Answers:", attempted - score)

if attempted > 0:
    percentage = (score / attempted) * 100
    print("Percentage: {:.2f}%".format(percentage))
else:
    print("Percentage: 0%")