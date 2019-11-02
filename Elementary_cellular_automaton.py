import sys
import time

initial_state = '0000000000000000000000000000000000000001' \
                '000000000000000000000000000000000000000'                   # 79 characters with one 1 in its middle

possible_cases = ['111', '110', '101', '100', '011', '010', '001', '000']


def window(iterable, stride=3):
    """splits iterable by strides of 3 chars. Each string starting by index i"""
    for i in range(len(iterable) - stride + 1):
        yield iterable[i: i + stride]


def replace_and_print(line_list):
    """replaces 1s & 0s by black squares and spaces respectively then print"""
    line_list = line_list.replace('0', ' ')
    line_list = line_list.replace('1', u"\u2588")
    print(line_list)


def calculate_new_state(state, rules):
    """calculates the next state and closes lines with periodic boundaries"""
    closed_line = f'{state[-1]}{state}{state[0]}'
    listed = list(window(closed_line))
    new_state = ''.join(rules[stride] for stride in listed)
    return new_state


def run(rule=30, pause=0.1, lines=40):
    """runs Wolfram Elementary CA with given rule entered as command line parameter or directly as argument"""

    # checking for 1st parameter (if given), and setting it to var (code)
    if len(sys.argv) > 1:
        code = sys.argv[1]
    else:
        code = rule

    # converting given rule code to binary then filling with '0' is necessary
    param = str(bin(int(code)))[2:]
    param = param.rjust(8, '0')

    # creating dictionary based on [possibles cases] as keys, and converted binary code as values respectively
    rules = {possible_cases[i]: list(param)[i] for i in range(0, len(param), 1)}

    replace_and_print(initial_state)
    state = initial_state

    for i in range(lines - 1):                           # -1 as the initial state has been replaced and printed above
        time.sleep(pause)
        state = calculate_new_state(state, rules)
        replace_and_print(state)


if __name__ == '__main__':
    run(rule=90)
