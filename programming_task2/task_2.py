def menu():
    while True:
        pressed_button = input("Press a proper key button whether you want to proceed ")
        pressedButton = validate(pressed_button)
        if pressedButton != None:
            if pressedButton == 1:
                number = input("Enter a number of rows and columns ")
                numberValidation = validate(number)
                if numberValidation != None:
                    matrix = inputMatrix(numberValidation)
                    result = checkPalindromeRows(matrix)
                    print(result)
                else:
                    print('An invalid type was printed')
                    continue
            elif pressedButton == 0:
                handleProgramExit()
                break
            else:
                handleUnknownInput()
                break
        else:
            handleUnknownInput()
            break


def handleProgramExit():
    print("End of the program.")
    return


def handleUnknownInput():
    print("Unknown button was pressed. End of the program.")
    return


def inputMatrix(number):
    matrix = []
    for i in range(number):
        temp = []
        for j in range(number):
            value = input("Enter a value ")
            valueValidation = validate(value)
            if valueValidation != None:
                temp.append(valueValidation)
            else:
                print('An invalid type was printed, cannot proceed')
                return []
        matrix.append(temp)
    return matrix


def checkPalindromeRows(matrix):
    length = len(matrix)
    flag = False
    result = []
    for i in range(length):
        for j in range(length):
            if matrix[i][j] == matrix[i][length - j - 1]:
                flag = True
            else:
                flag = False
        if flag:
            result.append(i)
    return result


def validate(input):
    result = int(input) if input.isnumeric() else None
    return result

menu()
