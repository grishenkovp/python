import unittest
import calc


class CalcBasicTest(unittest.TestCase):
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

    @unittest.skip("Пропускаем данный тест")
    def test_add(self):
        """Тест на сложение"""
        print("id: " + self.id())
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        """Тест на вычитание"""
        print("id: " + self.id())
        self.assertEqual(calc.sub(4, 2), 2)

    def test_mul(self):
        """Тест на умножение"""
        print("id: " + self.id())
        self.assertEqual(calc.mul(2, 5), 10)

    def test_div(self):
        """Тест на деление"""
        print("id: " + self.id())
        self.assertEqual(calc.div(8, 4), 2)

@unittest.skip("Пропускаем данный класс")
class CalcExTest(unittest.TestCase):
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

    def test_sqrt(self):
        """Тест на извлечение корня """
        print("id: " + self.id())
        self.assertEqual(calc.sqrt(4), 2)

    def test_sub(self):
        """Тест на возведение в степень"""
        print("id: " + self.id())
        self.assertEqual(calc.pow(3, 3), 27)


if __name__ == '__main__':
    unittest.main()
