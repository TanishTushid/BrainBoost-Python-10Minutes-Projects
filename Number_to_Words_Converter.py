def number_to_words(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
             "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    if num == 0:
        return "Zero"
    
    def helper(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        else:
            return ones[n // 100] + " Hundred" + (" " + helper(n % 100) if n % 100 != 0 else "")
        
    result = ""
    i = 0
    while num > 0:
        if num % 1000 != 0:
            result = helper(num % 1000) + " " + thousands[i] + " " + result
        num //= 1000
        i += 1

    return result.strip()

# --- CLI Loop ---
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    try:
        number = int(user_input)
        print("In words:", number_to_words(number))
    except ValueError:
        print("❌ Invalid input! Please enter an integer.")
