import re

def is_valid_credit_card(card_number):
    # Regular expression to match the required pattern
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    
    # Check if the card number matches the pattern
    if not re.match(pattern, card_number):
        return "Invalid"
    
    # Remove hyphens from the card number
    card_number = card_number.replace('-', '')
    
    # Check for four or more consecutive repeated digits
    if re.search(r'(\d)\1{3}', card_number):
        return "Invalid"
    
    return "Valid"

def main():
    # Read the number of credit card numbers
    N = int(input().strip())
    
    # Read each credit card number and check its validity
    results = [is_valid_credit_card(input().strip()) for _ in range(N)]
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
