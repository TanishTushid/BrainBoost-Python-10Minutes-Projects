import tkinter as tk
from collections import Counter
import string

def analyze_text():
    text = input_text.get("1.0", tk.END)
    char_count = len(text)
    word_list = text.split()
    word_count = len(word_list)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Clean and find most common word
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = cleaned_text.split()
    if words:
        most_common = Counter(words).most_common(1)[0]
        common_word = f"{most_common[0]} ({most_common[1]} times)"
    else:
        common_word = "N/A"
    
    # Display results
    char_label.config(text=f"Characters: {char_count}")
    word_label.config(text=f"Words: {word_count}")
    sentence_label.config(text=f"Sentences: {sentence_count}")
    common_label.config(text=f"Most Common Word: {common_word}")

# GUI setup
root = tk.Tk()
root.title("Word Counter")

tk.Label(root, text="Enter text below:", font=('Arial', 12)).pack()

input_text = tk.Text(root, height=10, width=50)
input_text.pack(pady=10)

tk.Button(root, text="Analyze", command=analyze_text).pack()

char_label = tk.Label(root, text="Characters: 0")
char_label.pack()

word_label = tk.Label(root, text="Words: 0")
word_label.pack()

sentence_label = tk.Label(root, text="Sentences: 0")
sentence_label.pack()

common_label = tk.Label(root, text="Most Common Word: N/A")
common_label.pack()

root.mainloop()
