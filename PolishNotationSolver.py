class NoLista(object):
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_next(self, proximo):
        self.proximo = proximo

    def get_next(self):
        return self.proximo

    def get_value(self):
        return self.valor


class Stack(object):

    def __init__(self):
        self.top = None

    def push(self, valor):
        novo = NoLista(valor)
        novo.set_next(self.top)
        self.top = novo

    def pop(self):
        r = -1
        if not self.is_empty():
            r = self.top.get_value()
            self.top = self.top.get_next()

        return r

    def top(self):
        r = -1
        if not self.is_empty():
            r = self.top.get_value
        return r

    def is_empty(self):
        return self.top is None

    def print(self):
        if not self.is_empty():
            p = self.top
            print('TOP')
            while p is not None:
                print(' --> ' + str(p.get_value()))
                p = p.get_next()
        else:
            print('EMPTY')


def solve_expression(expression):
    """
    :param expression: an expression in polish notation
    :type expression: str
    :return: the result of the expression
    """

    operations = ['+', '-', '*', '/']

    # splits the string
    treated_expression = expression.split(' ')

    # removes any additional white space
    for i in range(treated_expression.count('')):
        treated_expression.remove('')

    if len(treated_expression) == 0:
        print('Empty expression', end='')
        return

    container = Stack()

    # solves the expression
    for i in range(len(treated_expression)):
        if treated_expression[i] in operations:
            # get the first element of the stack
            if not container.is_empty():
                b = container.pop()
            else:
                print('Not enough numbers before operator', end = '')
                return
            # get the second element of the stack
            if not container.is_empty():
                a = container.pop()
            else:
                print('Not enough numbers before operator', end = '')
                return

            if treated_expression[i] == '+':
                container.push(a + b)
            elif treated_expression[i] == '-':
                container.push(a - b)
            elif treated_expression[i] == '*':
                container.push(a * b)
            elif treated_expression[i] == '/':
                if b == 0:
                    print('Division by zero', end = '')
                    return
                container.push(a / b)
        else:
            try:
                container.push(int(treated_expression[i]))
            except ValueError:
                print('There are letters or not supported characters in the expression', end='')
                return

    result = container.pop()

    if not container.is_empty():
        print('Too many numbers', end = '')
        return

    return result


# expressions in polish reverse notation
exp1 = '10 18 25 + - 20 +'
exp2 = '10       20 +'
exp3 = '10 30 * 2 / 50 -'
exp4 = '100 18 25 50 38 42 + - / * *'
exp5 = '10 + 20'
exp6 = '10 20 30 + '
exp7 = '10 20 + 30'
exp8 = '54 312 + - 1'
exp9 = '1 3 + 5 - a'
exp10 = ' '
exp11 = ' 1 0 /'


print(' --> ' + str(solve_expression(exp1)))
print(' --> ' + str(solve_expression(exp2)))
print(' --> ' + str(solve_expression(exp3)))
print(' --> ' + str(solve_expression(exp4)))
print(' --> ' + str(solve_expression(exp5)))
print(' --> ' + str(solve_expression(exp6)))
print(' --> ' + str(solve_expression(exp7)))
print(' --> ' + str(solve_expression(exp8)))
print(' --> ' + str(solve_expression(exp9)))
print(' --> ' + str(solve_expression(exp10)))
print(' --> ' + str(solve_expression(exp11)))
