import json

def ask_question():
    question = input("enter the question:")
    choices = []
    for i in range(4):
        var = input(f"enter choice[{i+1}]:")
        choices.append(var)
    
    correct_ans = input("enter correct choice number(int):")
    data = {"question":question, "choices": choices, "correct_ans":correct_ans}
    print("="*25)
    return data

def question_data_dict(number_of_questions):
    question_data = []
    for j in range(number_of_questions):
        #ask questions and store them in the varible called dat
        data = ask_question()
        #append data to question_data
        question_data.append(data)
    
    return question_data

def save2json(data):
    data = json.dumps(data)
    with open("questions.json","w") as f:
        f.write(data)
        
    return 

#quiz data python objects
data = question_data_dict(5)
#save them to json in the system
save2json(data)
    
        
