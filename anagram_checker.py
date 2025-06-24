
def is_anagram(string_1, string_2):
    cleaning_1 = string_1.replace(" ","").lower()
    cleaning_2 = string_2.replace(" ","").lower()

    return sorted(string_1)==sorted(string_2)
if __name__ == "__main__":
    while True:
        print("🔤 Anagram Checker 🔤")
        word1 = input("Enter first word/phrase (or type 'exit' to quit): ")
        word2 = input("Enter second word/phrase: ")

        if word1.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        if is_anagram(word1,word2):
            if is_anagram(word1, word2):
                print("✅ They are anagrams!")
        else:
            print("❌ They are not anagrams.")