from crontab import CronTab

my_cron = CronTab(user='pavel')

# Создание задачи
# db_job = my_cron.new(command='python3 /home/pavel/Документы/crontab/write_data.py',
#                      comment='insert new record into table')
# db_job.minute.every(1)

# my_cron.write()

# print('Cron job create successfully')

# Удаление задачи
for job in my_cron:
    if job.comment == 'insert new record into table':
        my_cron.remove(job)
        my_cron.write()
        print('Cron job delete successfully')