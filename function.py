from abc import abstractmethod

class Function:
    """Parent class Function"""
    def __init__(self, function_num):
        self.function_num = function_num

    @abstractmethod
    def get_number(self):
        pass

    @abstractmethod
    def print_function_number(self):
        pass