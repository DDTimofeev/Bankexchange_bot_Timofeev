class ParentException(Exception):
    def __init__(self, message,
                 error):  # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
        super().__init__(message)  # помним про вызов конструктора родительского класса
        print(f"Errors: {error}")  # печатаем ошибку


class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
    def __init__(self, message, error):
        super().__init__(message, error)


try:
    raise ChildException("message", "error")  # поднимаем исключение-наследник, передаём дополнительный аргумент
except ParentException as e:
    print(e)  # выводим информацию об исключении