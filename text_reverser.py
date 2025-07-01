# text reverser

def text_reverser():
    user_input = input("Enter the sentance (or type 'exit' to quit):: ")

    if user_input.lower() == "exit":
        print("Exiting the program. Goodbye!")
        return False

    #Reverse entire sentence (character by character)
    char_reverse = user_input[::-1]
    print("Reversed (by characters):",char_reverse)

    #Reverse sentence word by word
    words = user_input.split()
    reversed_words = "".join(reversed(words))
    print(print("Reversed (by words):", reversed_words))

    return True

if __name__=="__main__":
    while True:
        if not text_reverser():
             break