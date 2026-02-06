def check_voting_eligibility(age, citizenship):
    if age < 0:
        return "Invalid age"

    if age >= 18 and citizenship.strip().lower() == "indian":
        return "Eligible to vote"
    
    return "Not eligible to vote"


# Taking user input
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship: ")

# Checking eligibility
result = check_voting_eligibility(age, citizenship)
print(result)

