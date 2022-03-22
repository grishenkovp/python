import os
from glob import glob
import yaml
import shutil

with open('settings.yaml', encoding='utf8') as f:
    settings = yaml.safe_load(f)

path_data = settings['DATA']['PATH']
path_datalake = settings['DATALAKE']['PATH']
code_str = settings['DATALAKE']['CODE_STR']


def extract_data(path_data: str = path_data,
                 path_datalake: str = path_datalake,
                 code_str: str = code_str) -> None:
    """Импорт файлов из хранилища в локальную папку"""
    for f in list(glob(os.path.join(path_datalake, '*.xlsx'))):
        if code_str in f:
            shutil.copy(f, path_data)
