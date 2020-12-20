from time import sleep
import wget
a=True
for i in range(114,171):
    url='https://www.doors-treasures.ru/img/cards/1'+str(i)+'.png'
    a=True
    while a:
        sleep(0.5)
        try:
            filename = wget.download(url)
            a=False
        except:
            pass