from function import Function


class Function_test(Function):
    def __init__(self, num_y_test):
        self.num_y_test = num_y_test
        Function.__init__(self, 0)

    def who_am_i(self):
        print('I AM TEST FUNCTION')
