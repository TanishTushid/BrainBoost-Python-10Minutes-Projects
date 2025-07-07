# text to emoji converter

def text_to_emoji():
    user_input = input("Enter your text (or type 'exit' to quit): ")
    emoji_dict = {
          "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "angry": "😠",
    "cool": "😎",
    "laugh": "😂",
    "cry": "😭",
    "heart": "💖",
    "fire": "🔥",
    "ok": "👌",
    "yes": "👍",
    "no": "👎",
    "hello": "👋",
    "bye": "👋",
    "wow": "😲",
    "food": "🍕",
    "pizza": "🍕",
    "party": "🎉",
    "music": "🎵",
    "dog": "🐶",
    "cat": "🐱",
    "sun": "☀️",
    "moon": "🌙",
    "star": "⭐",
    "sleep": "😴",
    "smile": "😄",
    "kiss": "😘",
    "clap": "👏",
    "win": "🏆",
    "coffee": "☕",
    "book": "📚",
    "rain": "🌧️",
    "cloud": "☁️",
    "car": "🚗",
    "bike": "🚲",
    "rocket": "🚀",
    "money": "💰",
    "idea": "💡",
    "gift": "🎁",
    "camera": "📷",
    "phone": "📱"
    }
    if user_input.lower() == 'exit':
        print("👋 Goodbye!")
        return False
    
    words = user_input.lower().split()
    result = [emoji_dict.get(word, word) for word in words]
    print("👉", " ".join(result))
    return True 

if __name__=="__main__":
    while True:
       if not text_to_emoji():
            break