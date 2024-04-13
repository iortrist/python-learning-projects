import os

def hexToDecimal(hexNumber) -> int:
    hexNumbers = {
                    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
                    }

    decimalNumber = 0
    hexLength = len(hexNumber)-1

    for char in hexNumber:
        if char not in hexNumbers:
            return f'Invalid hex number. Please try again'
        else:
            decimalNumber = decimalNumber + (hexNumbers[char] * (16**hexLength))
            hexLength-= 1
            
    return f"The hex value of {hexNumber} is equivalent to {decimalNumber} in decimal"

def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


convert = ''

while convert == '':      
  
    user_input = input("Enter the Hex you wish to convert: ")

    clearConsole()

    print(hexToDecimal(user_input.upper())+"\n") 
    
    convert = input("Press Enter to convert another otherwise press any keys and then Enter...   ")
    
    clearConsole()

