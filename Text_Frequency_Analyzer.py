import string
from collections import Counter


#list of common stopword to execute
stopwords = {"the", "is", "and", "in", "of", "to", "a", "that", "it", "on", "with", "as", "for"}

#clean_text
def clean_text(text):
    text = text.lower()
    return text.translate(str.maketrans('','',string.punctuation))

def analyze_text(text):
    cleaned = clean_text(text)
    words = cleaned.split()

    #remove stopwords
    filtered_word = [word for word in words if word not in stopwords]

    #grt total word count
    total_words = len(filtered_word)
    word_freq = Counter(filtered_word)
    top_5_words = word_freq.most_common(5)

    return total_words,word_freq,top_5_words

if __name__ =="__main__":
    print("📊 Text Frequency Analyzer 📊")
    print("Enter your paragraph (press Enter twice to finish): ")

    #multi-line input
    lines = []
    while True:
        line = input()
        if line.strip()=="":
            break
        lines.append(line)
    text = "\n".join(lines)

    total, freq_dict, top_5 = analyze_text(text)

    print("\n🔢 Total Words (excluding stopwords):", total)
    print("\n📈 Top 5 Most Frequent Words:")

    for word, Count in top_5:
        print(f"{word} : {Count}")

    print("\n📋 Full Word Frequency:")
    for word, count in freq_dict.items():
        print(f"{word}: {count}")