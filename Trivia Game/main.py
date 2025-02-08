import random

questions = {
    "Creator of Python?": "Guido",
    "Latest Python version?": "3.12",
    "Python file extension?": "py",
    "Mutable built-in type?": "list",
    "Immutable built-in type?": "tuple",
    "Keyword to define a function?": "def",
    "Looping structure in Python?": "for",
    "Keyword to create a class?": "class",
    "Built-in data type for text?": "str",
    "Built-in data type for decimals?": "float",
    "Data type for True/False?": "bool",
    "Keyword to import a module?": "import",
    "Function to get input from user?": "input",
    "Function to display output?": "print",
    "Function to get length of an object?": "len",
    "Function to convert to integer?": "int",
    "Function to convert to string?": "str",
    "Function to check data type?": "type",
    "Operator for exponentiation?": "**",
    "Operator for floor division?": "//",
    "Operator for modulo?": "%",
    "Logical operator for AND?": "and",
    "Logical operator for OR?": "or",
    "Logical operator for NOT?": "not",
    "Keyword to handle exceptions?": "try",
    "Keyword to raise an exception?": "raise",
    "Statement to exit a loop?": "break",
    "Statement to skip iteration?": "continue",
    "Statement to define an empty block?": "pass",
    "Method to add element in a list?": "append",
    "Method to remove element from a list?": "remove",
    "Function to sort a list?": "sorted",
    "Function to get max value?": "max",
    "Function to get min value?": "min",
    "Keyword for inheritance?": "super",
    "Keyword to define a generator?": "yield",
    "Built-in function to map values?": "map",
    "Built-in function to filter values?": "filter",
    "Built-in function to reduce values?": "reduce",
    "Module for regular expressions?": "re",
    "Module for working with time?": "time",
    "Module for working with OS?": "os",
    "Built-in module for JSON?": "json",
    "Keyword to delete a variable?": "del",
    "Function to read a file?": "read",
    "Function to write a file?": "write",
    "Method to get dictionary keys?": "keys",
    "Method to get dictionary values?": "values",
    "Keyword to check membership?": "in",
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list,total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx+1}. {question}")
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!!\n")
            score += 1
        else:
            print(f"Incorrect: Correct answer is "+f"{correct_answer}.\n")

    print(f"Game Over: Your Final Score is {score}/{total_questions}")



python_trivia_game()

