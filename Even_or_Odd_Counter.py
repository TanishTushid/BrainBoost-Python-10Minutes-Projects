# even odd counter

def even_odd_counter():
    print("Even Odd Counter")

    user_input = input("Enter numbers (comma-separated): ")

    numbers = [int(num.strip()) for num in user_input.split(',') if num.strip().isdigit()]

    odd_count = 0
    even_count = 0

    for num in numbers:
        if num %2 == 0:
            print(f"{num} is Even")
            even_count += 1 
        else :
            print(f"{num} is odd")
            odd_count += 1
    
    print("summary")
    print(f"total even: {even_count}")
    print(f"total odd: {odd_count}")

if __name__=="__main__":
    even_odd_counter()