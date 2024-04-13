def clearConsole() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def factorial(number) -> str:
    try:
        number = int(number)

        if number < 0:
            return 'Please enter a positive integer.'
    
    except ValueError:
        return 'Please enter a valid integer.'

    
    
    if number == 0:
        return f'Factorial of {number}: \n\n{number}! = 1'
        
    result = 1
    formattedResult = f'Factorial of {number}: \n\n{number}! = {number}'

    while number > 0:
        result *=  number
        number -= 1

        if number != 0:
            formattedResult+= f' x {number}'

    return f'{formattedResult} = {result}'

number = input("Enter a number: ")
print(factorial(number))