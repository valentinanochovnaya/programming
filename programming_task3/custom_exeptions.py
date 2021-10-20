class InvalidEmailError(Exception):
    def __init__(self, message='An invalid email was printed'):
        self.message = message


class InvalidPhoneNumberError(Exception):
    def __init__(self, message='An invalid phone number was printed'):
        self.message = message


class NotRecognizablePositionError(Exception):
    def __init__(self, message='There is not such position'):
        self.message = message


class IdAlreadyExistsError(Exception):
    def __init__(self, message='Id is already exists'):
        self.message = message


class InvalidNameError(Exception):
    def __init__(self, message='Name should not contain numbers'):
        self.message = message


class InvalidNumberError(Exception):
    def __init__(self, message='An invalid number was printed'):
        self.message = message


class AvailabilityError(Exception):
    def __init__(self, message='Freelancer cannot work that much'):
        self.message = message


class FilePathError(Exception):
    def __init__(self, message='File does not exist'):
        self.message = message


class AllErrors(Exception):
    list_of_custom_erros = []

    def init(self):
        pass

    def collect_error(self, error_code):
        if error_code == 'number':
            number_error = InvalidNumberError()
            self.list_of_custom_erros.append(number_error)
        elif error_code == 'email':
            email_error = InvalidEmailError()
            self.list_of_custom_erros.append(email_error)
        elif error_code == 'phone':
            phone_error = InvalidPhoneNumberError()
            self.list_of_custom_erros.append(phone_error)
        elif error_code == 'position':
            position_error = NotRecognizablePositionError()
            self.list_of_custom_erros.append(position_error)
        elif error_code == 'name':
            name_error = InvalidNameError()
            self.list_of_custom_erros.append(name_error)
        elif error_code == 'id':
            id_error = IdAlreadyExistsError()
            self.list_of_custom_erros.append(id_error)
        elif error_code == 'file':
            file_error = FilePathError()
            self.list_of_custom_erros.append(file_error)
        elif error_code == 'avail':
            availability_error = FilePathError()
            self.list_of_custom_erros.append(availability_error)
        else:
            return
        return self.list_of_custom_erros