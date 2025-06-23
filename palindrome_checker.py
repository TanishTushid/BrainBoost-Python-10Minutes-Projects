def is_palindrome(text):
    cleaned = text.replace(" ","").lower()
    return cleaned ==cleaned[::-1]
def main():
    while True:
        user_input = input("Enter a word or sentence (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        if is_palindrome (user_input):
            print("✅ It's a palindrome!")
        else :
            print("❌ Not a palindrome.")

if __name__ == "__main__":
    print("Running the program........")
    main()