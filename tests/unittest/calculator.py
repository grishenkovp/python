def func_calculator(expression):
    d = {'+': lambda a, b: a + b,
         '-': lambda a, b: a - b,
         '*': lambda a, b: a * b,
         '/': lambda a, b: a / b, }
    allowed = '+-/*'
    if not any(_ in allowed for _ in expression):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                exp = d[sign]
                return (exp(left, right))
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак (+-/*)')
            except ZeroDivisionError:
                raise ZeroDivisionError('Делить на ноль нельзя')
            # else:
            #     print('Расчет выполнился без ошибок')
            # finally:
            #     print('Конец работы алгоритма')


if __name__ == '__main__':
    print(func_calculator('10+10'))
