"""
Pre coding steps for Typing Speed Tester:
1. Import necessary modules: time for measuring time taken, random for selecting random sentences.
2. Create a list of sentences for the typing test.
3. Define a function to measure accuracy by comparing user input with the test sentence.
4. Define the main function to conduct the typing test:
   - Select a random sentence from the list.
    - Prompt the user to type the sentence and record the start time.
    - Capture the user input and record the end time. 
    - Calculate time taken, words typed, typing speed (words per minute), and accuracy.

5. Call the main function to start the typing test.

"""
# time module is used for time related functions
import time # For measuring time taken 
import random # For selecting random sentences

# # List of sentences for typing test
sentences = [ 
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "This is the way for us to reference the object of the class."
]

# Function to measure accuracy
def measure_accuracy(user_input, test_sentence): # user_input is what user typed, test_sentence is the original sentence
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b) # explanation: zip pairs characters from both strings, sum counts matches
    accuracy = (correct_chars / len(test_sentence)) * 100 if test_sentence else 0 # Calculate accuracy percentage
    return accuracy

def typing_test(): # Main function to conduct typing test
    test_sentence = random.choice(sentences) # Select a random sentence
    print("Type the following sentence as fast as you can:") # Prompt user
    print(test_sentence) # Display the sentence to type
    input("Press Enter when you are ready...")
    start_time = time.time() # Record start time
    user_input = input("\nStart typing:\n") 
    end_time = time.time() # Record end time
    time_taken = round(end_time - start_time, 2)   # Calculate time taken # round to 2 decimal places for better readability
    word_count = len(test_sentence.split(" ")) # Count words in the test sentence
    if time_taken == 0:
        print("Typing too fast to measure!")
        return


    print("Results:")
    print(f"Time taken: {time_taken} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing speed: {word_count / (time_taken / 60):.2f} words per minute") # Calculate typing speed in WPM
    accuracy = measure_accuracy(user_input, test_sentence) # Measure accuracy
    print(f"Accuracy: {accuracy:.2f}%") # Display accuracy

typing_test()