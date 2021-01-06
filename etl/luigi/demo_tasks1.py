# Task Класс Task это основной блок, где происходит выполнение конкретного таска.
# Task.run Основная бизнес-логика шага.
# Task.requires В методе необходимо перечислить зависимости.
# Task.output Этот метод должен возвращать Target объект.
# Task.input Этот метод не нужно переопределять. Он выступает "оберткой" над Task.requires и возвращает Target объекты,
# полученные в Task.requires.

# Запускаем в терминале
# python -m luigi_demo_tasks Task_2 --local-scheduler

import luigi

class Task_1(luigi.Task):

   filename = "first.txt"

   def run(self):
       with open(self.filename, 'w') as f:
           f.write("first!")

   def output(self):
       return luigi.LocalTarget(self.filename)


class Task_2(luigi.Task):

   filename = "second.txt"

   def run(self):
       with open(self.filename, 'w') as f:
           f.write("second!")

   def requires(self):
       return Task_1()

   def output(self):
       return luigi.LocalTarget(self.filename)


if __name__ == '__main__':
   luigi.run()


