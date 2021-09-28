def menu():
    while True:
        pressed_button = input("Press a proper key button whether you want to proceed ")
        pressedButton = validate(pressed_button)
        if pressedButton == 1:
            mainProgram()
        elif pressedButton == 0:
            handleProgramExit()
            break
        elif pressedButton is None:
            print('An invalid type was printed')
            continue
        else:
            handleUnknownInput()
            break


def handleNone(value):
    return False if value is None else True


def mainProgram():
    number = input("Enter a number of rows and columns ")
    number_ = validate(number)
    handleNone(number_)
    if not handleNone(number_):
        print('An invalid type was printed')
    else:
        matrix = inputMatrix(number_)
        result = checkPalindromeRows(matrix)
        print(result)
    return


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
            if valueValidation is not None:
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


def validate(input_value):
    result = int(input_value) if input_value.isnumeric() else None
    return result

menu()
