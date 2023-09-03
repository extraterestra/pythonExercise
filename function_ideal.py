from function import Function


class Function_ideal(Function):
    def __init__(self, num_y_ideal, deviation_to_test):
        self.num_y_ideal = num_y_ideal
        self.deviation_to_test = deviation_to_test
        Function.__init__(self,0)
    def who_am_i(self):
        print('I AM IDEAL FUNCTION with ')