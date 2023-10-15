class Function:
    """Abstract class Function"""
    def __init__(self, function_num):
        self.function_num = function_num

    def who_am_i(self):
        print(f'I AM PARENT FUNCTION with {self.function_num}')
