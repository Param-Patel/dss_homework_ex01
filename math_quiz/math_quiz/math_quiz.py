import random


def generate_random_integer(minimum_range, maximum_range):
    """
    Returns a random integer specified within the minimum and maximum range
    """
    return random.randint(minimum_range, maximum_range)


def generate_random_operator():
    """
    Generates a random mathematical operator where '+' is addition; '-' is subtraction; '*' is multiplication
    """
    return random.choice(['+', '-', '*'])


def calculation(number_1, number_2, operator):
    """

    :param number_1: Any integer number 1
    :param number_2: Any integer number 2
    :param operator: '+'/ '-'/ '*'
    :return: Result
    """
    operation = f"{number_1} {operator} {number_2}"
    if operator == '+':
        result = number_1+number_2
    elif operator == '-':
        result = number_1-number_2
    else:
        result = number_1*number_2

    return operation, result


def math_quiz():
    """
    Try-Except warning returns an invalid input format if user does not mention integer
    :return: Final score based upon right answers
    """
    score = 0
    total_questions = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for question_number in range(total_questions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 6)
        operator = generate_random_operator()

        operation, result = calculation(number1, number2, operator)
        print(f"\nQuestion: {operation}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input format. The function demands an integer input")

        if user_answer == result:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
