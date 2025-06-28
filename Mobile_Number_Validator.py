#Mobile Number Validator (India-specific)


def mobile_number_validator(number):
    if len(number) != 10:
        return "Invalid: Must be 10 digits."

    if not number.isdigit():
        return "Invalid: Should contain only digits"

    if number[0] not in ['6', '7', '8', '9']:
        return "Invalid: Should start with 6, 7, 8, or 9"
        
    return "Valid Indian mobile number!"

def main():
    user_input= input("Enter a mobile Number: ")
    result = mobile_number_validator(user_input)
    print(result)

if __name__ =="__main__":
    while True:
        main()