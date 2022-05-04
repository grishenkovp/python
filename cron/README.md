### Алгоритм работы
#### Установка cron
* sudo apt update
* sudo apt upgrade
* sudo apt install cron
* sudo systemctl enable cron

#### Создание виртуального окружения
* python3 -m venv .env
* source .env/bin/activate

#### Написание и запуск файла c задачей, которую нужно поставить на регулярное выполнение

#### Конроль списка выполняемых задач
* crontab -l