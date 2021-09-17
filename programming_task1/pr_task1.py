def input_array(length):
    array = []
    if length % 2 == 0:
        for i in range(length):
            element = int(input())
            array.append(element)
    else:
        print("Length can't be devided into 2")
        return
    return array


def array_modification(array):
    half_length = len(array)//2
    result_array = []
    for i in range(half_length, len(array)):
        result_array.append(array[i])
    for i in range(half_length):
        result_array.append(array[i])
    return result_array


try:
    size = int(input("Enter a length of an array "))
    arr = input_array(size)
    result = array_modification(arr)
    print(result)
except ValueError:
    print("Invalid value type was printed")
except TypeError:
    print("Resulting array is an empty array")