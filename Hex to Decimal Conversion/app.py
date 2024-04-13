import os

def hexToDecimal(hexNum) -> int:
    hexNumbers = {
                    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
                    }

    decimalNum = 0
    hexLength = len(hexNum)-1

    for i in hexNum:
        if i.upper() not in hexNumbers:
            return f'Invalid input. Please try again'
        else:
            decimalNum = decimalNum + (hexNumbers[i.upper()] * (16**hexLength))
            hexLength-= 1
            
    return f"The hex value of {hexNum.upper()} is equivalent to {decimalNum} in decimal"

def clearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


convert = ''

while convert.name == '':      
  
    user_input = input("Enter the Hex you wish to convert: ")

    clearConsole()

    print(hexToDecimal(user_input)+"\n") 
    
    convert = input("Press Enter to convert another otherwise press any keys...   ")
    
    clearConsole()

