from data import quiz_dict

score = 0

for quiz in quiz_dict:
    print(quiz_dict[quiz]['question'])
    answer = input("Answer: ")
    
    if answer.lower() == quiz_dict[quiz]['answer'].lower():
        print("Your answer is correct")
        score += 10
    else:
        print("Your answer is wrong")
        print(f"Correct answer is: {quiz_dict[quiz]['answer']}")
    print(f"Your score: {score}")
    print("-----------------------")
print(f"Total score is: {score}")

