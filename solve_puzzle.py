import re


def insert_after(l, index, item):
    if index == len(l) - 1:
        l.append(item)
    else:
        l.insert(index + 1, item)


def insert_before(l, index, item):
    l.insert(index, item)


class Rule:
    def __init__(self, i, s, o):
        self.item = i
        self.symbol = s
        self.other = o

    def process(self, order):
        if self.other in order and self.item not in order:
            index = order.index(self.other)
            if self.symbol == '>':
                insert_after(order, index, self.item)
            else:
                insert_before(order, index, self.item)
            return True
        elif self.item in order and self.other not in order:
            index = order.index(self.item)
            if self.symbol == '>':
                insert_before(order, index, self.other)
            else:
                insert_after(order, index, self.other)
            return True
        else:
            return False

    def __str__(self):
        return '{} {} {}'.format(self.item, self.symbol, self.other)


def solve_puzzle(puzzle):
    result = re.search('Please solve this puzzle:\n ABCD\nA(....)\nB(....)\nC(....)\nD(....)\n', puzzle)

    rules = []

    matrix = [['-' for y in range(4)] for x in range(4)]
    for i in range(4):
        for j in range(4):
            symbol = result.group(i+1)[j]
            if i == j:
                matrix[i][j] = '='
            elif symbol != '-':
                rules.append(Rule(i, symbol, j))

    order = [rules[0].item]

    while rules and len(order) < 4:
        rules = [x for x in rules if not x.process(order)]

    for i in range(4):
        for j in range(4):
            if matrix[i][j] == '-':
                i_index = order.index(i)
                j_index = order.index(j)
                if i_index > j_index:
                    matrix[i][j] = '>'
                else:
                    matrix[i][j] = '<'

    return ' ABCD\nA{}\nB{}\nC{}\nD{}'.format(''.join(matrix[0]),
                                              ''.join(matrix[1]),
                                              ''.join(matrix[2]),
                                              ''.join(matrix[3]))
