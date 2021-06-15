import json
#load questions from json file
data_json = open("questions.json","r").read()
questions_list = json.loads(data_json)


#iterate through question
total_number_of_questions = len(questions_list)
submitted_answers = []

for i in range(total_number_of_questions):
    print(f"question{[i+1]}")
    question = questions_list[i]
    print(question["question"])
    for j in range(4):
        choices = question["choices"]
        print(f"{[j+1]} {question['choices'][j]}")
    correct_ans = int(input("answer(int):"))
    submitted_answers.append(correct_ans)

print(submitted_answers)
number_of_correct_answers = 0
number_of_wrong_answers = 0
for answer in questions_list:
    
    if int(answer["correct_ans"]) == int()


    
"""
command line quiz app exampe
question[1]
pick the odd one out:
[1] python3 
[2] java
[3] css
[4] kotlin
answer:3
============================

   ..........
   
"""

