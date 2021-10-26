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


class AllErrors(Exception):
    list_of_custom_erros = []

    def init(self):
        pass

    def collect_error(self, error_code):
        error_dict = {
            'id': InvalidNumberError,
            'number': InvalidNumberError,
            'email': InvalidEmailError,
            'phone': InvalidPhoneNumberError,
            'position': NotRecognizablePositionError,
            'name': InvalidNameError,
            'avail': AvailabilityError
        }

        for key, value in error_dict.items():
            if error_code == key:
                self.list_of_custom_erros.append(error_dict[key](value()))

        return self.list_of_custom_erros
