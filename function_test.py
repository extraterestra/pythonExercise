from function import Function


class Function_test(Function):
    """Class Function_test which inherits from class Function"""
    def __init__(self, function_num):
        super().__init__(function_num)
        self.function_num = function_num

    def who_am_i(self):
        print(f'I AM TEST FUNCTION WITH {self.function_num}')
