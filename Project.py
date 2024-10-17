# Create the variable for grade
grade = 0

# All questions go here
# General question
questionsGeneral = [
    {
        "prompt": "What is the capital of Ireland?",
        "options": ["A. Paris", "B. Dublin", "C. Berlin", "D. Brazilia"],
        "answer": "B"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Portuguese", "B. Spanish", "C. Dutch", "D. English"],
        "answer": "A"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"  
    },
    {
        "prompt": "Who wrote 'To kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

# Science questions
questionsScience = [
    {
        "prompt": "What is the chemical symbol for water?",
        "options": ["A. O2", "B. H2O", "C. CO2", "D. H2"],
        "answer": "B"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "prompt": "What gas do plants absorb from the atmosphere during photosynthesis?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "prompt": "What is the hardest natural substance on Earth?",
        "options": ["A. Gold", "B. Iron", "C. Diamond", "D. Silver"],
        "answer": "C"
    },
    {
        "prompt": "What part of the human cell contains genetic material?",
        "options": ["A. Nucleus", "B. Cytoplasm", "C. Cell Membrane", "D. Mitochondria"],
        "answer": "A"
    }
]

# History questions 

questionsHistory = [
    {
        "prompt": "Which country was the first to industrialize during the Industrial Revolution?",
        "options": ["A. Germany", "B. France", "C. Britain", "D. Italy"],
        "answer": "C"
    },
    {
        "prompt": "Who was the ruler of France during the Napoleonic Wars?",
        "options": ["A. Louis XIV", "B. Napoleon Bonaparte", "C. Charles de Gaulle", "D. Maximilien Robespierre"],
        "answer": "B"
    },
    {
        "prompt": "Which treaty ended World War I in 1919?",
        "options": ["A. Treaty of Versailles", "B. Treaty of Paris", "C. Treaty of Vienna", "D. Treaty of Brest-Litovsk"],
        "answer": "A"
    },
    {
        "prompt": "Which of these countries was not part of the Axis Powers in World War II?",
        "options": ["A. Italy", "B. Germany", "C. Japan", "D. Spain"],
        "answer": "D"
    },
    {
        "prompt": "What was the political ideology of the Soviet Union during the Cold War?",
        "options": ["A. Fascism", "B. Capitalism", "C. Communism", "D. Monarchism"],
        "answer": "C"
    }
]

# Maths questions

questionsMaths = [
    {
        "prompt": "What is the value of Pi to two decimal places?",
        "options": ["A. 3.12", "B. 3.14", "C. 3.16", "D. 3.18"],
        "answer": "B"
    },
    {
        "prompt": "What is the square root of 144?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    },
    {
        "prompt": "Solve for x: 2x + 3 = 7",
        "options": ["A. x = 1", "B. x = 2", "C. x = 3", "D. x = 4"],
        "answer": "B"
    },
    {
        "prompt": "What is the result of 15 ÷ 3 + 4 × 2?",
        "options": ["A. 10", "B. 14", "C. 13", "D. 16"],
        "answer": "C"
    },
    {
        "prompt": "What is 25% of 200?",
        "options": ["A. 25", "B. 50", "C. 75", "D. 100"],
        "answer": "B"
    }
]


# ALL QUESTION FUNCTIONS GO HERE
# Define the function for general questions
def general_questions(questionsGeneral):
    global grade    
    score = 0
    total_questions = len(questionsGeneral)

    for question in questionsGeneral:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A , B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct answer!!\n")
            score += 1
            grade +=1
        else:
            print("Wrong!!! The correct answer was:", question["answer"], "\n")

    print(f"Your score is {score} out of {len(questionsGeneral)}")

    return score, total_questions

# Define the funtion for science questions 

def science_questions(questionsScience):
    global grade 
    score = 0
    total_questions = len(questionsScience)
    for question in questionsScience:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A , B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct answer!!\n")
            score += 1
            grade += 1
        else:
            print("Wrong!!! The correct answer was:", question["answer"], "\n")

    print(f"Your score is {score} out of {len(questionsScience)}")
    return score, total_questions

# Define the funtion for history questions 

def history_questions(questionsHistory):
    global grade 
    score = 0
    total_questions = len(questionsHistory)
    for question in questionsHistory:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A , B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct answer!!\n")
            score += 1
            grade += 1
        else:
            print("Wrong!!! The correct answer was:", question["answer"], "\n")

    print(f"Your score is {score} out of {len(questionsHistory)}")
    return score, total_questions

# Define the funtion for Maths questions 

def Maths_questions(questionsMaths):
    global grade 
    score = 0
    total_questions = len(questionsMaths)
    for question in questionsMaths:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A , B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct answer!!\n")
            score += 1
            grade += 1
        else:
            print("Wrong!!! The correct answer was:", question["answer"], "\n")

    print(f"Your score is {score} out of {len(questionsMaths)}")
    return score, total_questions

# Define the function for Grades

def Grade(score, total_question):
    if score > 0 :
        percentage = (score / total_question) * 100
        print(f"Your total score is ({percentage:.2f}%)")
    else :
        print("No questions answered yet")

# Define the menu function
def menu():

    total_score = 0
    total_question = 0


    while True:
        print("\n=== Menu ===")
        print("1. General questions.")
        print("2. Science questions.")
        print("3. History questions.")
        print("4. Maths questions.")
        print("5. Check my grades.")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            score, questions = general_questions(questionsGeneral)
            total_score += score
            total_question += questions
        elif choice == '2':
           score, questions = science_questions(questionsScience)
           total_score += score
           total_question += questions
        elif choice == '3':
           score, questions = history_questions(questionsHistory)  
           total_score += score
           total_question += questions
        elif choice == '4':
            score, questions = Maths_questions(questionsMaths)  
            total_score += score
            total_question += questions
        elif choice == '5':
            Grade(total_score, total_question)        
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
            
# Call the menu
menu()



    