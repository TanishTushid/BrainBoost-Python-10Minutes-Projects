import string
from collections import Counter

user_input = input(" Enter your paragraph:\n ")      # take the input from user's

characters_count = len(user_input)    # count the characters of the paragraph

words_split = user_input.split()      #split the paragraph
words_length = len(words_split)       #give the length of the words split

sentence_count = user_input.count('.')+user_input.count('!')+user_input.count('?')    # count the sentences

#remove puntuation

cleaned_text = user_input.translate(str.maketrans('','',string.punctuation))          # cleaning the paragraph
words_frequency = Counter(cleaned_text.lower().split())                               # count the words
most_common_words = words_frequency.most_common(1)[0]                                 # count the common words 

#print for output

print("\nAnalysing.....")                                                                   
print(f"Characters: {characters_count}")                                                        #give characters
print(f"Words: {words_length}")                                                                 #give word length
print(f"Sentences: {sentence_count}")                                                           #give sentences in paragraph
print(f"Most common word: '{most_common_words[0]}'({most_common_words[1]} times)")              #give most common words


