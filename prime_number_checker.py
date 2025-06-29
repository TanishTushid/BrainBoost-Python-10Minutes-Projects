#prime number checker

def is_prime(n, explain=False):
    if n <= 1:
        if explain:
            print(f"{n} is not a prime number because it is less than or equal to 1.")
        return False
    if n == 2:
        if explain:
            print("2 is a prime number.")
        return True
    if n % 2 == 0:
        if explain:
            print(f"{n} is divisible by 2, so it is not a prime number.")
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            if explain:
                print(f"{n} is divisible by {i}, so it is not a prime number.")
            return False

    if explain:
        print(f"{n} is a prime number.")
    return True

def main():
    try:
        num = int(input("Enter a number: "))
        mode = input("Do you want explanation mode? (y/n): ").strip().lower()
        explain = mode == 'y'
        result = is_prime(num, explain)
        if not explain:
            print("Prime" if result else "Not Prime")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
