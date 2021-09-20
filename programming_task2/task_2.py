while True:
    try:
        processButton = int(input("Press a button whether you want to proceed "))
        if processButton == 1:
            def inputMatrix(rows, columns):
                if rows == columns:
                    matrix = []
                    for i in range(rows):
                        temp = []
                        for j in range(columns):
                            value = int(input("Enter a value "))
                            temp.append(value)
                        matrix.append(temp)
                    return matrix
                else:
                    print("Rows and columns don't match, it should have been a square matrix")


            def checkPalindromRows(matrix_):
                length = len(matrix_)
                flag = False
                result = []
                for i in range(length):
                    for j in range(length):
                        if matrix_[i][j] == matrix_[i][length - j - 1]:
                            flag = True
                        else:
                            flag = False
                    if flag:
                        result.append(i)
                return result

            rows_ = int(input("Enter rows "))
            columns_ = int(input("Enter columns "))
            matrixx = inputMatrix(rows_, columns_)
            result_ = checkPalindromRows(matrixx)
            if not result_:
                print("There was an error, resulting matrix == [], cannot proceed")
            else:
                print(result_)
        elif processButton == 0:
            print("End of program")
            break
        else:
            print("Unknown button was pressed, end of program")
            break
    except ValueError:
        print("It should be an integer, try again")
    except TypeError:
        print("Cannot calculate length from non-square matrix")
    except KeyboardInterrupt:
        print("There was an error, please, start again")