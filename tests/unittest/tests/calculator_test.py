from unittest import TestCase, main, skip
from calculator import func_calculator

# Запуск всех тестов в папке Additional Arguments: discover -s tests -p "*_test.py"

# Методы, используемые при непосредственном написании тестов (проверка условий, сообщение об ошибках).

# TestCase класс предоставляет набор assert-методов для проверки и генерации ошибок:
#
# assertEqual(a, b)	        a == b
# assertNotEqual(a, b)	    a != b
# assertTrue(x)	            bool(x) is True
# assertFalse(x)	        bool(x) is False
# assertIs(a, b)	        a is b
# assertIsNot(a, b)	        a is not b
# assertIsNone(x)	        x is None
# assertIsNotNone(x)	    x is not None
# assertIn(a, b)	        a in b
# assertNotIn(a, b)	        a not in b
# assertIsInstance(a, b)	isinstance(a, b)
# assertNotIsInstance(a, b)	not isinstance(a, b)

# Assert’ы для контроля выбрасываемых исключений и warning’ов:
#
# assertRaises(exc, fun, *args, **kwds)	        Функция fun(*args, **kwds) вызывает исключение exc
# assertRaisesRegex(exc, r, fun, *args, **kwds)	Функция fun(*args, **kwds) вызывает исключение exc, сообщение которого совпадает с регулярным выражением r
# assertWarns(warn, fun, *args, **kwds)      	Функция fun(*args, **kwds) выдает сообщение warn
# assertWarnsRegex(warn, r, fun, *args, **kwds)	Функция fun(*args, **kwds) выдает сообщение warn и оно совпадает с регулярным выражением r

# Assert’ы для проверки различных ситуаций:
#
# assertAlmostEqual(a, b)	 round(a-b, 7) == 0
# assertNotAlmostEqual(a, b) round(a-b, 7) != 0
# assertGreater(a, b)	     a > b
# assertGreaterEqual(a, b)	 a >= b
# assertLess(a, b)	         a < b
# assertLessEqual(a, b)	     a <= b
# assertRegex(s, r)	         r.search(s)
# assertNotRegex(s, r)	     not r.search(s)
# assertCountEqual(a, b)	 a и b имеют одинаковые элементы (порядок неважен)

# Типо-зависимые assert’ы, которые используются при вызове assertEqual(). Приводятся на тот случай, если необходимо использовать конкретный метод.
#
# assertMultiLineEqual(a, b)	строки (strings)
# assertSequenceEqual(a, b)	    последовательности (sequences)
# assertListEqual(a, b)	        списки (lists)
# assertTupleEqual(a, b)	    кортежи (tuplse)
# assertSetEqual(a, b)	        множества или неизменяемые множества (frozensets)
# assertDictEqual(a, b)	       словари (dicts)



class CalculatorTest(TestCase):
    @classmethod
    def setUpClass(cls):
        # Метод действует на уровне класса, т.е. выполняется перед запуском тестов класса.
        print('setUpClass')
        print('==========')

    @classmethod
    def tearDownClass(cls):
        # Запускается после выполнения всех тестов класса, требует наличия декоратора @classmethod.
        print("==========")
        print("tearDownClass")

    def setUp(self):
        # Метод вызывается перед запуском каждого теста. Как правило, используется для подготовки окружения для теста.
        print("Set up for [" + str(self.shortDescription()) + "]")

    def tearDown(self):
        # Метод вызывается после завершения работы каждого теста. Используется для “приборки” за тестом.
        print("Tear down for [" + str(self.shortDescription()) + "]")
        print("")

    def test_plus(self):
        """Тест на сложение"""
        print("id: " + self.id())
        self.assertEqual(func_calculator('90+10'), 100)

    def test_subtraction(self):
        """Тест на вычитание"""
        print("id: " + self.id())
        self.assertEqual(func_calculator('100-10'), 90)

    def test_multi(self):
        """Тест на умножение"""
        print("id: " + self.id())
        self.assertEqual(func_calculator('10*10'), 100)

    def test_divide(self):
        """Тест на деление"""
        print("id: " + self.id())
        self.assertEqual(func_calculator('100/10'), 10)

    def test_no_signs(self):
        """Тест на наличие арифметического знака"""
        print("id: " + self.id())
        with self.assertRaises(ValueError) as e:
            func_calculator('aaabbbccc')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    @skip("Пропускаем данный тест")
    def test_many_signs(self):
        """Тест на наличие единственного арифметического знака"""
        print("id: " + self.id())
        with self.assertRaises(ValueError) as e:
            func_calculator('10*10*10')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак (+-/*)', e.exception.args[0])

    def test_strings(self):
        """Тест на наличие цифр в строке"""
        print("id: " + self.id())
        with self.assertRaises(ValueError) as e:
            func_calculator('a+b')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак (+-/*)', e.exception.args[0])

    def test_no_ints(self):
        """Тест на наличие целых чисел в строке"""
        print("id: " + self.id())
        with self.assertRaises(ValueError) as e:
            func_calculator('10.2 * 10.3')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак (+-/*)', e.exception.args[0])

if __name__ == '__main__':
    main()
