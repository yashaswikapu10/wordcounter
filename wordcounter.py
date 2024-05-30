def count_words(text):
    """
    This function takes a string input and returns the number of words in it.
    A word is defined as a sequence of characters separated by spaces.
    """
    # Split the text by spaces to get a list of words
    words = text.split()
    # Return the length of the list which represents the number of words
    return len(words)

def main():
    """
    Main function to handle user input, word counting, and displaying the output.
    """
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")

    # Error handling for empty input
    if not user_input.strip():
        print("Error: No input provided. Please enter some text.")
        return

    # Call the count_words function to get the number of words
    word_count = count_words(user_input)

    # Display the word count to the user
    print(f"The number of words in the entered text is: {word_count}")

# Entry point of the program
if _name_ == "_main_":
    main()