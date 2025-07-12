

def number_to_word_converter(num):

    ones = [
        "zero", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"
    ]

    if 0 <= num < 20:
        return ones[num]
    
    if 20 <= num <100:
        return tens[num//100] + ("  "+ ones[num%10] if num %10 != 0 else " ")
    if 100 <= num <999:
        rest = num%100
        return ones[num // 100] + "hundred" + (" "+number_to_word_converter(rest) if rest !=0 else" ")
    else:
        return "number out of range"
    

if __name__=="__main__":
    print(number_to_word_converter(0))
    print(number_to_word_converter(50))
    print(number_to_word_converter(101))
    print(number_to_word_converter(505))
    print(number_to_word_converter(998))