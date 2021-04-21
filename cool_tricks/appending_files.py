import datetime
from time import sleep

for i in range(5):
    file_builder = open('cool_tricks\logger.txt', 'a+')
    file_builder.write(f'{datetime.datetime.now()}\n')
    file_builder.close()

    print('file created success!!')
    sleep(1)