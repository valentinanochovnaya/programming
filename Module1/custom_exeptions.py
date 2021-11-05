class NotRecognizableCityError(Exception):
    def __init__(self, message='There is not such city'):
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


class UsernameAlredyExists(Exception):
    def __init__(self, message='A username is alredy exists'):
        self.message = message


class TooMuchMoneyToSpend(Exception):
    def __init__(self, message='You do not have that much money'):
        self.message = message


class BudgetTypeError(Exception):
    def __init__(self, message='Invalid type'):
        self.message = message


class AllErrors(Exception):
    list_of_custom_erros = []

    def init(self):
        pass

    def collect_error(self, error_code):
        error_dict = {
            'id': InvalidNumberError,
            'number': InvalidNumberError,
            'city': NotRecognizableCityError,
            'name': InvalidNameError,
            'name_exists': UsernameAlredyExists,
            'not_enough_money': TooMuchMoneyToSpend,
            'budget_type': BudgetTypeError
        }

        for key, value in error_dict.items():
            if error_code == key:
                self.list_of_custom_erros.append(error_dict[key](value()))

        return self.list_of_custom_erros
