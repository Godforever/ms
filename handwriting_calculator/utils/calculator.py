import re


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


operations = {'+': add, '-': sub, '*': mul, '/': div}
weight = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1, None: 0}

# Define the stack of data and the stack of operations
data_stack = []
operator_stack = []


def deal_data():
    op = operator_stack.pop()
    num2 = float(data_stack.pop())
    num1 = float(data_stack.pop())
    result = operations[op](num1, num2)
    data_stack.append(result)
    return result


def calculate(equation):
    while equation:
        cur = re.search(r"((^\d+\.?\d*)|(^\(\-\d+\.?\d*)|\(|\)|\+|\-|\*|/)", equation).group()
        print(cur)
        if "(-" in cur:
            bracket = cur[0]
            operator_stack.append(bracket)
            equation = equation[1:]
            num = cur[1:]
            data_stack.append(num)
            equation = equation[len(num):]

        else:
            lenth = len(cur)
            if is_number(cur):
                data_stack.append(cur)
            elif cur == ")":
                if operator_stack[-1] == "(":
                    operator_stack.pop()
                else:
                    deal_data()
                    while operator_stack[-1] != "(":
                        deal_data()
                    operator_stack.pop()
            else:
                if not (operator_stack):
                    operator_stack.append(cur)
                else:
                    if weight[cur] > weight[operator_stack[-1]]:
                        operator_stack.append(cur)
                    else:
                        if operator_stack[-1] == "(":
                            operator_stack.append(cur)
                        else:
                            deal_data()
                            while operator_stack and weight[cur] == weight[operator_stack[-1]]:
                                deal_data()
                            operator_stack.append(cur)
            equation = equation[lenth:]
    result = deal_data()
    while operator_stack:
        result = deal_data()
    return result