def is_divisible_by_11(number):
    if not isinstance(number, int) or number < 0:
        return False
    
    alternating_sum = 0
    digit_position = 0
    
    while number > 0:
        digit = number % 10
        number //= 10
        
        if digit_position % 2 == 0:
            alternating_sum += digit

        else:
            alternating_sum -= digit
        
        digit_position += 1
    
    return alternating_sum % 11 == 0

while True:
    try:
        number = input("Enter a number: ")
        
        if not number.isdigit():
            raise ValueError("That is not a valid number.")
        
        number = int(number)
        
        if is_divisible_by_11(number):
            print("This is divisible by 11.")
        else:
            print("This is not divisible by 11.")
        
        break
    
    except ValueError as ve:
        print(f"Error: {ve}")
