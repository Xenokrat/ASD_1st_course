from stack import Stack


def eval_postfix_expression(expr: str):
    # create stacks
    s1 = Stack()
    s2 = Stack()

    # prepare to fill s1
    expr_list = expr.split()
    expr_len = len(expr_list)

    # list of all operations
    op_dict = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '*' : lambda x, y: x * y,
        '/' : lambda x, y: x / y,
        '%' : lambda x, y: x % y,
        '**': lambda x, y: x ** y,
    }

    # fill s1
    for ind in range(expr_len - 1, -1, -1):
        s1.push(expr_list[ind])

    while s1.size() > 0:
        elem = s1.pop()

        if elem.isdigit():
            s2.push(int(elem))
            continue

        if elem == '=':
            print(s2.peek())
            break

        assert elem in op_dict, 'unknown operation'
        func = op_dict[elem]

        b = s2.pop()
        a = s2.pop()
        assert s2.size() == 0, 'there is more than 2 elements'

        res = func(a, b)
        s2.push(res)

    return s2.pop()
