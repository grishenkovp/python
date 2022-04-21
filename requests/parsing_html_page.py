import time
import requests


# def benchmark_1(func):
#     def wrapper():
#         start = time.time()
#         return_value = func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#         return return_value
#     return wrapper
#
#
# @benchmark_1
# def fetch_webpage_1():
#     response = requests.get('https:...')
#     try:
#         html_page = response.content.decode('utf-8', errors='ignore')
#     except:
#         html_page = response.content.decode('cp1251', errors='ignore')
#     return html_page
#
# print(fetch_webpage_1())


def benchmark_2(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value
    return wrapper


@benchmark_2
def fetch_webpage_2(url):
    response = requests.get(url)
    try:
        html_page = response.content.decode('utf-8', errors='ignore')
    except:
        html_page = response.content.decode('cp1251', errors='ignore')
    return html_page
    return html_page


webpage = fetch_webpage_2('https://...')
print(webpage)
