import time
import requests

def benchmark_1(func):        
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper

@benchmark_1
def fetch_webpage_1():
    webpage = requests.get('https://google.com')
	return webpage.text
	
print(fetch_webpage_1())


def benchmark_2(func):    
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

@benchmark_2
def fetch_webpage_2(url):
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage_2('https://google.com')
print(webpage)