
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
def generate_prime(limit):
    primes = []
    for num in range(2,limit + 1 ):
        if is_prime(num):
            primes.append(num)
    return primes
if __name__=="__main__":
#test
    choice = input("check (C) or generate (G) primes? ").lower()

    if choice == "c":
        n = int(input("Enter a number to check: "))
        print(f"{n} is {'a prime' if is_prime(n) else 'not a prime'}")

    elif choice == 'g':
        limit = int(input("Generate prime up to: "))
        print(generate_prime(limit))
    else:
        print("invalid")