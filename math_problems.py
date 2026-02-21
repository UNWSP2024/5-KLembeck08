import random

def generate_problem():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    return num1, num2

def main():
    num1, num2 = generate_problem()
    print(f"  {num1}")
    print(f"+ {num2}")
    print("------")

    user_answer = int(input("Your answer: "))
    correct_answer = num1 + num2

    if user_answer == correct_answer:
        print("Correct! Great job!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

main()
