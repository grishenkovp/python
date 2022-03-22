from load.load_main import load_data, create_table, select_postgresql
from extract.extract_main import extract_data
from transform.transform_main import transform_data
from sql.scripts import test_table_sql


def pipeline():
    # Копируем файлы из хранилища
    # extract_data()
    # Разбираем датасеты и сохраняем результаты в csv-файлы
    # transform_data()
    # Создаем таблицу в БД
    # create_table()
    # Записываем в нее значения
    # load_data()
    # Проверяем корректность загрузки данных
    print(select_postgresql(test_table_sql))


if __name__ == '__main__':
    pipeline()
