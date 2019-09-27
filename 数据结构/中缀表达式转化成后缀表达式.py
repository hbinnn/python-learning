"""
参考链接：https://www.jianshu.com/p/e149cc8e53a9
"""
operators = ['+', '-', '*', '/', '(', ')']


# 中缀表达式转化成后缀表达式
def middle2behind(expression):
    result = []             # 结果列表
    stack = []              # 栈
    for item in expression:
        if item.isnumeric():        # 如果当前字符为数字那么直接放入结果列表
            result.append(item)
        else:                       # 如果当前字符为一切其他操作符
            if len(stack) == 0:     # 如果栈空，直接入栈
                stack.append(item)

            elif item in '(/*':     # 如果当前字符为*/（，直接入栈
                stack.append(item)

            elif item == ')':       # 如果当前字符为右括号则全部弹出（碰到左括号停止）
                t = stack.pop()
                while t != '(':
                    result.append(t)
                    t = stack.pop()

            elif item in '+-' and stack[len(stack)-1] in '*/':      # 如果当前字符为加减且栈顶为乘除，则开始弹出
                if stack.count('(') == 0:       # 如果栈内没有左括号，弹出所有
                    while stack:
                        result.append(stack.pop())
                else:
                    t = stack.pop()             # 如果有左括号，弹到左括号为止
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)          # 弹出操作完成后将‘+-’入栈

            else:
                stack.append(item)      # 其余情况直接入栈（如当前字符为+，栈顶为+-）

    while stack:
        result.append(stack.pop())      # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出

    # 将>10的数重新拼接在一起 避免出现1 0两个数的现象
    i = 0
    while i != len(result) - 1:
        if result[i] != '0' and result[i + 1] == '0':
            result[i] = result[i] + result[i + 1]
            result.pop(i + 1)
        i += 1

    return result         # 返回字符串


# 计算后缀表达式
def calculate(result):
    calculate_stack = []

    # 遍历后缀表达式
    for item in result:
        # 如果为数字直接入栈
        # 遇到操作符，将栈顶的两个元素出栈
        if item not in operators:
            calculate_stack.append(item)
        else:
            # 操作数
            num1 = calculate_stack.pop()
            # 被操作数
            num2 = calculate_stack.pop()
            # 计算结果
            res = operate(num1, num2, item)
            # 将结果入栈
            calculate_stack.append(res)

    return calculate_stack[0]


# 四则运算
def operate(num1, num2, operator):
    """
    计算结果
    :param number1: 操作数
    :param number2: 被操作数
    :param operator: 操作符
    :return:
    """
    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        return num2+num1
    if operator == '-':
        return num2-num1
    if operator == '*':
        return num2*num1
    if operator == '/':
        return num2/num1


expression = "9+(3-1)*3+8/2"
result = middle2behind(expression)
print(result)
print(calculate(result))
