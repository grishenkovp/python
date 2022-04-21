from calculator import func_calculator
import pytest
import random

def create_list_values():
    list_values = []
    for _ in range(4):
        x = random.randint(1, 1000)
        sign = '+-/*'[random.randint(0, 3)]
        y = random.randint(1, 1000)
        exp_string = str(x) + sign + str(y)
        z = eval(exp_string)
        list_values.append((exp_string, z))
    return list_values

list_values = create_list_values()
# list_values = [('90+10', 100), ('100-10', 90), ('10*10', 100), ('100/10', 10)]

@pytest.mark.parametrize('exp, result',list_values)
def test_calculator(exp, result):
    """Тест арифметических операций"""
    assert func_calculator(exp) == result


@pytest.mark.parametrize('exp, e', [('100/0', ZeroDivisionError), ('100/a', ValueError)])
def test_with_error(exp, e):
    """Тест на корректность передаваемых значений и деление на ноль"""
    with pytest.raises(e):
        func_calculator(exp)
