import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question text"])
    for index, option in enumerate(question["Options"]):
        print(index + 1, "-", option)
    user_input = int(input("Enter your answer: "))
    question["User Choice"] = user_input
    print("Your answer is: ", user_input)

    if int(user_input) == question["correct answer"]:
        score = score + 1
    else:
        print("Your answer is incorrect")

for question in data:
    message = f"Your answer: {question['User Choice']}, Correct answer: {question['correct answer']}"
    print(message)

print("Your score is: ", score, "/", len(data))
