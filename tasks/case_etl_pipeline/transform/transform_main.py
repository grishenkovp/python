import pandas as pd
import yaml
import os
import re
from glob import glob
from typing import List
from datetime import datetime

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('expand_frame_repr', False)

with open('settings.yaml', encoding='utf8') as f:
    settings = yaml.safe_load(f)

path_data = settings['DATA']['PATH']
path_data_transform = settings['DATA_TRANSFORM']['PATH']
path_data_control = settings['DATA_CONTROL']['PATH']
columns_name = settings['DATA_TRANSFORM']['COLUMNS_NAME']
sep = settings['DATA_TRANSFORM']['SEP']


def get_all_file(path_data: str = path_data) -> List:
    """Получить список файлов в папке"""
    all_file_name = list(glob(os.path.join(path_data, '*.xlsx')))
    return all_file_name


def is_user_id(x: str) -> bool:
    """Проверка на корректность поля user_id"""
    result = re.match(r'[u]\d{1,3}$', x)
    return False if (result is None) else True


def is_product(x: str) -> bool:
    """Проверка на корректность поля product"""
    result = re.match(r'pr\d{1,3}$', x)
    return False if (result is None) else True


def is_amount(x: int) -> bool:
    """Проверка на корректность поля amount"""
    if (type(x) == int or type(x) == float) and (x <= 1000):
        return True
    else:
        return False


def is_date(x: datetime) -> bool:
    """Проверка на корректность поля date"""
    if (type(x) == datetime):
        return True
    else:
        return False


def create_name_file(d, is_control: bool = False) -> str:
    """Генерация имени для файла"""
    date_df = d.iloc[0]['date']
    month_df = date_df.strftime('%m')
    year_df = date_df.strftime('%Y')
    if not is_control:
        name_file = 'sales-' + month_df + '-' + year_df + '.csv'
    else:
        name_file = 'sales-' + month_df + '-' + year_df + '-control' + '.csv'
    return name_file


def transform_data(path_data: str = path_data,
                   path_data_transform: str = path_data_transform,
                   path_data_control: str = path_data_control,
                   columns_name: List = columns_name,
                   sep: str = sep):
    for f in get_all_file(path_data):
        df = pd.read_excel(f)
        # Переименование столбцов
        df.columns = columns_name
        # Заполнение пустот в датасете
        df = df.fillna('нет данных')
        # Проверка столбцов на корректность значений
        df['is_date'] = df['date'].apply(lambda x: is_date(x))
        df['is_user_id'] = df['user_id'].apply(lambda x: is_user_id(x))
        df['is_product'] = df['product'].apply(lambda x: is_product(x))
        df['is_amount'] = df['amount'].apply(lambda x: is_amount(x))
        # Разделение датасета на две части: датафрейм для записи в БД и контроль
        df_correct_ = df[(df['is_date'] * df['is_user_id'] * df['is_product'] * df['is_amount']) == 1]
        df_correct = df_correct_.iloc[:, 0:4]
        df_correct.to_csv(os.path.join(path_data_transform, create_name_file(df_correct)), index=False, sep=sep)

        df_control_ = df[(df['is_date'] * df['is_user_id'] * df['is_product'] * df['is_amount']) != 1]
        df_control = df_control_.iloc[:, 0:4]
        df_control.to_csv(os.path.join(path_data_control, create_name_file(df_correct, True)), index=False, sep=sep)
