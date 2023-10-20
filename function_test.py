from function import Function

class Function_test(Function):
    """Class Function_test which inherits from class Function"""
    def __init__(self, function_num):
        super().__init__(function_num)
        self.function_num = function_num

    def get_number(self):
        return self.function_num

    def print_function_number(self):
        print(f'Test function with number {self.function_num}')