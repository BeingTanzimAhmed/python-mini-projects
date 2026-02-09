def run_quiz(): # This function runs a simple quiz game
    questions = [ # List of quiz questions, options, and answers
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C) Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B) 4"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B) Jupiter"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
            "answer": "C) William Shakespeare"
        }
    ]

    score = 0 # Initialize score to keep track of correct answers
 
 # enumerate function is used to loop through the questions list and get both the index and the question itself. This allows us to display the question number (Q1, Q2, etc.) when printing the question to the user.
    for index,q in enumerate(questions):   # Loop through each question and display it to the user
        print(f"Q{index + 1}: {q['question']}")
        for option in q['options']: # Loop through the options for the current question and print them
            print(option)
        
        user_answer = input("Your answer(A/B/C/D): ") # Prompt the user to input their answer
        if user_answer.strip().upper() == q['answer'][0]: # Check if the user's answer matches the correct answer (ignoring case and whitespace)
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer is {q['answer']}\n")

    print(f"Your final score is {score}/{len(questions)}") # After all questions have been answered, print the user's final score out of the total number of questions

run_quiz() # Call the function to start the quiz game