def calculate_score(correct_count, total_questions):
    percentage_score = (correct_count / total_questions) * 100
    return percentage_score

def get_grade(percentage):
    if percentage < 50:
        return "D - Better luck next time!"
    elif percentage <= 69:
        return "C - Not bad, keep practicing!"
    elif percentage <= 89:
        return "B - Good Job!"
    else:
        return "A - Trivia Master!"


questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is 5 + 5 * 2?"
]
correct_answers = ["paris", "mars", "15"]

print("=== Welcome to the Python Trivia Quiz! ===")
print()

correct_count = 0

for i in range(len(questions)):
    # Print the individual question using index [i]
    print(f"Question {i+1}: {questions[i]}")
    user_answer = input("Your answer: ").strip().lower()
    print()
    
 
    if user_answer == correct_answers[i]:
        correct_count += 1


total_questions = len(questions)
final_percentage = calculate_score(correct_count, total_questions)
final_grade = get_grade(final_percentage)


print("--- QUIZ RESULTS ---")
print(f"You got {correct_count} out of {total_questions} correct!")
print(f"Score: {final_percentage}%")
print(f"Grade: {final_grade}")
print("-" * 20)