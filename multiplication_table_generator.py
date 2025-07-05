# Multiplication Table Generator

def table_generator():
    print("📊 Multiplication Table Generator")

    user_input = input("Enter a number (or type 'exit' to quit): ").strip()

    if user_input.lower() == 'exit':
        print("👋 Goodbye!")
        return False  # signal to exit the loop

    try:
        num = int(user_input)
        print(f"\nMultiplication Table for {num}:\n")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

    return True  # signal to continue the loop

if __name__ == "__main__":
    while True:
        if not table_generator():
            break
