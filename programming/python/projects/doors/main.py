from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
monstrs=['Монстры 1 уровня','Монстры 1 уровня','Монстры 1 уровня','Монстры 1 уровня','Монстры 1 уровня','Монстры 10 уровня','Монстры 10 уровня','Монстры 10 уровня','Монстры 12 уровня','Монстры 12 уровня','Монстры 12 уровня','Монстры 14 уровня','Монстры 14 уровня','Монстры 16 уровня','Монстры 16 уровня','Монстры 16 уровня','Монстры 16 уровня','Монстры 18 уровня','Монстры 18 уровня','Монстры 2 уровня','Монстры 2 уровня','Монстры 2 уровня','Монстры 2 уровня','Монстры 2 уровня','Монстры 20 уровня','Монстры 4 уровня','Монстры 4 уровня','Монстры 4 уровня','Монстры 4 уровня','Монстры 6 уровня','Монстры 6 уровня','Монстры 6 уровня','Монстры 6 уровня','Монстры 8 уровня','Монстры 8 уровня','Монстры 8 уровня','Монстры 8 уровня']
namemonstrs=['Калечный Гоблин','Пасюк с Кувалдой','Сочащаяся Слизь','Типа вошки','Трава в Горшке','3872 Орка','Просто Тролль','Сопливый Нос','Бигфут','Закос под Вампира','Демон с Язычком','Обдолбанный Голем','Страховой Агент','Белые Братья','Король Тут','Невыразимо Жуткий Неописуемый Ужас','Гиппогриф','Бульрог','Кальмадзилла','Г-н Кости','Летучие Лягушки','Питбуль','Здоровенная Бешеная Цыпа','Желатиновый Октаэдр','Плутониевый Дракон','Гарпистки','Лепрекон','Наскипидаренные Улитки','Неживой Коник','Адвокат','Дотошный Ботан','Рыгачу','Утикора','Амазонка','Бабыри','Газебо','Лицесос']
boost=['Усилители монстров','Усилители монстров','Зелье5','Зелье5','Усилители монстров','Зелье2','Усилители монстров','Зелье5','Зелье2','Зелье2','Усилители монстров','Зелье3','Зелье2','Зелье2','Зелье3','Зелье3']
nameboost=['Амбал','Детеныш','Клёвые Шарики','Мэджик Мисайл!','Мозг','Питье Противно-Спортивное','Псих','Радиоактивноэлектрокислотное Зелье','Спячечное Зелье','Стакан Яппи','Старикан','Зелье Холодильного Взрыва','Зелье Идиотской Храбрости','Зелье Ротовой Вони','Зелье Жгучего Яда','Пелье Зутаницы']
rasy=['Расы c коктейлями','Расы c коктейлями','Расы c коктейлями','Расы c коктейлями','Расы c коктейлями','Расы c коктейлями','Расы c коктейлями','Расы c коктейлями','Расы c коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями','Расы c коктейлями','Расы c коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями','Классы, с коктейлями']
namerasy=['Дварф','Дварф','Дварф','Эльф','Эльф','Эльф','Хафлинг','Хафлинг','Хафлинг','Клирик','Клирик','Клирик','Расовый Коктейль','Расовый Коктейль','Классовый Коктейль','Классовый Коктейль','Воин','Воин','Воин','Волшебник','Волшебник','Волшебник','Вор','Вор','Вор']
proklyatie=['Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия','Проклятия']
nameproklyatie=['Изгнание из Класса','Кривящее Зеркало','Курица на Башне','Налоги','Потеря 1 Большой Шмотки','Потеря Двух Карт','Потеря 1 Уровня!','Потеря 1 Уровня!','Смена Класса','Смена Пола','Смена Расы','Потеря Броника','Потеря Головняка','Потеря Обувки','Утка Обреченности','Утрата 1 Маленькой Шмотки','Утрата 1 Маленькой Шмотки','Утрата Расы','В конец мерзкое Проклятие!']
level=['Уровень','Уровень','Уровень','Уровень','Уровень','Уровень','Уровень','Уровень','Уровень','Уровень']
namelevel=['1,000 Голдов','Кульная Ошибка при Сложении','Муравьиный Геноцид','Подкормленный Мастер','Расчет Наемника','Сломленный Мастер','Уровенный Вор','Утилизация Трупов','Заклинание Непонятных Правил','Зелье Крутизны']
shmot=['Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки','Шмотки']
nameshmot=['Башмаки Могучего Пенделя','Башмаки Реально Быстрого Бега','Бензопила Кровавого Расчленения','Боевая стремянка','Чарующая Дуда','Доспехи Поперек-Себя-Шире','Дуб Джентльменов','Кинжал Измены','Коленеотбойный Молоточек','Колготки Великанской Силы','Колотушка Резкости','Кожаный Прикид','Лучок С Ленточками','Меч Коварного Бастарда','Меч Песни и Пляски','Меч Широты Взглядов','Мифрильные Доспехи','Небоись-Бандана','Одиннадцатифутовый Кий','Огромная Каменюга','Острые Коленки','Пафосный Баклер','Паленые Доспехи','Плащ Замутнения','Пойнтовая Шляпа','Посох Напалма','Рапира Такнечестности','Реально Конкретный Титул','Сандалеты-Протекторы','Сэндвич Запоздалого Прозрения с сыром и селедкой','Шлем Бесстрашия','Шлем-Рогач','Швейцарская Армейская Алебарда','Склизкие Доспехи','Тёрка Умиротворения','Вездешний Щит']
door=['Двери вспомогательные','Двери атакующие','Двери вспомогательные','Сокровища вспомогательные','Сокровища вспомогательные','Двери атакующие','Сокровища вспомогательные','Сокровища вспомогательные','Сокровища вспомогательные','Сокровища вспомогательные','Двери атакующие','Двери вспомогательные','Сокровища вспомогательные','Сокровища вспомогательные','Сокровища вспомогательные','Двери вспомогательные','Двери защитные','Двери атакующие','Двери защитные','Сокровища вспомогательные','Сокровища вспомогательные']
namedoor=['Божественное Вмешательство','Бродячая Тварь','Чит','Читерский Кубик','Дупельгангер','Гадкая Парочка','Хотельное Кольцо','Хотельное Кольцо','Наемничек','Наколенники Развода','Бродячая Тварь','Помоги Себе Сам!','Стенка-встанька','Штырь Лозоходца','Тюбик Клея','Ура, клад!','Ушел на базу','Заморок','Зелье Дружбы','Зелье Невидимости','Зелье Стрелочника']


def open_log():
    
def cards():
    global a
    log=a.find_elements_by_class_name("pointer")
    print(len(log))
def zakrit():
    global a
    a.close()
def print_live_log():
    global a,log
    log=[]
    while True:
        log1=a.find_elements_by_class_name("pointer")
        for i in range(len(log1)):
            if log1[i].text not in log:
                print(log1[i].text)
                log.append(log1[i].text)
        sleep(4)
def print_log():
    global a
    log1=a.find_elements_by_class_name("pointer")
    for i in range(len(log1)):
        print(log1[i].text)
'''j=True
while j:
    print('Выберете действие:\n1)Запустить \n2)Количество карт\n3)открыть лог\n4)закрыть\n5)live log\n6)all log')
    try:
        b=int(input('Действие:'))
        if b==1:
            start()
        elif b==2:
            cards()
        elif b==3:
            open_log()
        elif b==4:
            a.close()
            j=False
        elif b==5:
            print_live_log()
        elif b==6:
            print_log()
    except:
        pass'''