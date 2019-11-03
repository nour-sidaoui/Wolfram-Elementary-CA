import sys
import time


class CA:
    initial_state = '0000000000000000000000000000000000000001000000000000000000000000000000000000000'  # 79 chars
    possible_cases = ['111', '110', '101', '100', '011', '010', '001', '000']

    def __init__(self, rule):
        self.line = self.initial_state
        self.rule = rule

    @staticmethod
    def window(iterable, stride=3):
        """splits iterable by strides of 3 chars. Each string starting by index i"""
        for i in range(len(iterable) - stride + 1):
            yield iterable[i: i + stride]

    def converter_dict(self):
        """returns a dictionary based on [possibles cases] as keys, and converted binary code as values respectively"""
        if len(sys.argv) > 1:               # checking for 1st parameter (if given)
            code = sys.argv[1]
        else:
            code = self.rule

        param = str(bin(int(code)))[2:]     # converting given rule code to binary [2:]
        param = param.rjust(8, '0')         # filling with '0' from the left if necessary

        return {CA.possible_cases[i]: list(param)[i] for i in range(0, len(param), 1)}

    def replace_and_print(self):
        """replaces 1s & 0s by black squares and spaces respectively then print"""
        x = self.line
        x = x.replace('0', ' ')
        x = x.replace('1', u"\u2588")
        print(x)

    def update_line(self, rules):
        """calculates the next state and closes lines with periodic boundaries"""
        y = self.line
        closed_line = f'{y[-1]}{y}{y[0]}'
        listed = list(self.window(closed_line))
        self.line = ''.join(rules[stride] for stride in listed)

    def run(self, pause=0.05, lines=40):
        """runs Wolfram Elementary CA with given rule entered as command line parameter or directly as argument"""
        rules = self.converter_dict()

        for i in range(lines):
            time.sleep(pause)
            self.replace_and_print()
            self.update_line(rules)


if __name__ == '__main__':
    a = CA(90)
    a.run()
