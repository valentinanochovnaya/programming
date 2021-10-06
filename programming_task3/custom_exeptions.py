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
