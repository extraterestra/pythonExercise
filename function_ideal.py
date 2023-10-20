from function import Function

class Function_ideal(Function):
    """Class Function_ideal which inherits from class Function"""
    def __init__(self, function_num, deviation_to_test):
        super().__init__(function_num)
        self.function_num = function_num
        self.deviation_to_test = deviation_to_test

    def get_number(self):
        return self.function_num

    def print_function_number(self):
        print(f'Ideal function with number {self.function_num}')
