# Task Класс Task это основной блок, где происходит выполнение конкретного таска. Чтобы определить свою собственную
# задачу, необходимо создать класс, унаследованный от Task, и реализовать несколько методов. Зачастую переопределять
# нужно только 3 метода: run(), output(), requires().

# Task.run Здесь выполняется вся логика будущей задачи, например, скачивание или парсинг данных с внешнего
# источника, запрос в базу данных для извлечения информации и т.д.

# Task.requires В методе requires() необходимо перечислить зависимости. Зависимостями выступают другие luigi.Task классы.

# Task.output Этот метод должен возвращать 1 или более Target объектов. Target объектом может быть файл на диске,
# файл внутри HDFS, S3 или файл, лежащий на удалённом FTP сервере и т.д. Если pipeline аварийно завершается где-то
# в середине выполнения задач, повторный запуск не приведёт к повторному запуску успешно завершившихся задач,
# выполнение начнется в месте аварийной остановки скрипта.

# Task.input Этот метод не нужно переопределять. Он выступает "оберткой" над Task.requires и возвращает Target объекты,
# полученные от выполнения задач, определенных в Task.requires.



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


