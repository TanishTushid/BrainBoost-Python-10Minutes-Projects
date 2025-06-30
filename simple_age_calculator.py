from datetime import datetime, timedelta

def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    today = datetime.today()

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    # Adjust if days are negative
    if days < 0:
        months -= 1
        # Get days in previous month
        previous_month = today.replace(day=1) - timedelta(days=1)
        days += previous_month.day

    # Adjust if months are negative
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def main():
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    y, m, d = calculate_age(dob_input)
    print(f"You are {y} years, {m} months, and {d} days old.")

if __name__ == "__main__":
    main()
