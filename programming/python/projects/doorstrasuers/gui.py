from tkinter import *  
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
def gen_string(l):
    k=''
    for i in range(len(l)):
        k+=l[i]+'\n'
    return k
def start():
    global a
    opts = Options()
    opts.set_headless()
    assert opts.headless
    a=webdriver.Firefox(options=opts)
    a.get("http://www.doors-treasures.ru/start.aspx")
    elem=a.find_element_by_name("tbLogin")
    elem.send_keys("batsnap")
    elem=a.find_element_by_name("tbPassword")
    elem.send_keys("112001Batkur",Keys.ENTER)
    result.config(text='вход выполнен')
    window.update()
def get_num_lobby():
    global a
    k=str(noumber.get())
    c='http://www.doors-treasures.ru/gamelogs.aspx?gameid='+k
    a.get(c)
    check()

def check():
    global a
    log=a.find_elements_by_class_name("pointer")
    while True:
        log=a.find_elements_by_class_name("pointer")
        for i in range(len(log)):
            if log[i].text in namemonstrs:
                del monstrs[namemonstrs.index(log[i].text)]
                del namemonstrs[namemonstrs.index(log[i].text)]
            elif log[i].text in nameboost:
                del boost[nameboost.index(log[i].text)]
                del nameboost[nameboost.index(log[i].text)]
            elif log[i].text in namerasy:
                del rasy[namerasy.index(log[i].text)]
                del namerasy[namerasy.index(log[i].text)]
            elif log[i].text in nameproklyatie:
                del proklyatie[nameproklyatie.index(log[i].text)]
                del nameproklyatie[nameproklyatie.index(log[i].text)]
            elif log[i].text in namelevel:
                del level[namelevel.index(log[i].text)]
                del namelevel[namelevel.index(log[i].text)]
            elif log[i].text in nameshmot:
                del shmot[nameshmot.index(log[i].text)]
                del nameshmot[nameshmot.index(log[i].text)]
            elif log[i].text in namedoor:
                del door[namedoor.index(log[i].text)]
                del namedoor[namedoor.index(log[i].text)]
            else:
                pass
        testlbl1.config(text=gen_string(monstrs))
        testlbl2.config(text=gen_string(namemonstrs))
        testlbl3.config(text=gen_string(boost))
        testlbl4.config(text=gen_string(nameboost))
        testlbl5.config(text=gen_string(rasy))
        testlbl6.config(text=gen_string(namerasy))
        testlbl7.config(text=gen_string(proklyatie))
        testlbl8.config(text=gen_string(nameproklyatie))
        testlbl9.config(text=gen_string(level))
        testlbl10.config(text=gen_string(namelevel))
        testlbl11.config(text=gen_string(shmot))
        testlbl12.config(text=gen_string(nameshmot))
        testlbl13.config(text=gen_string(door))
        testlbl14.config(text=gen_string(namedoor))
        window.update()
        sleep(0)

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
typename='Тип карты'
namecard='Название карты'
window = Tk()  
window.geometry('10000x1000')
window.title("МАЙНЧИКИН")  

type1=Label(window,text=typename,font='Times 8')
type1.grid(column=0,row=0)
testlbl1=Label(window,text=gen_string(monstrs),font='Times 10')
testlbl1.grid(column=0,row=1)

type2=Label(window,text=typename,font='Times 8')
type2.grid(column=0,row=2)
testlbl3=Label(window,text=gen_string(boost),font='Times 10')
testlbl3.grid(column=0,row=3)

type3=Label(window,text=typename,font='Times 8')
type3.grid(column=2,row=0)
testlbl5=Label(window,text=gen_string(rasy),font='Times 10')
testlbl5.grid(column=2,row=1)

type4=Label(window,text=typename,font='Times 8')
type4.grid(column=2,row=2)
testlbl7=Label(window,text=gen_string(proklyatie),font='Times 10')
testlbl7.grid(column=2,row=3)

type5=Label(window,text=typename,font='Times 8')
type5.grid(column=4,row=0)
testlbl9=Label(window,text=gen_string(level),font='Times 10')
testlbl9.grid(column=4,row=1)

type6=Label(window,text=typename,font='Times 8')
type6.grid(column=6,row=0)
testlbl11=Label(window,text=gen_string(shmot),font='Times 10')
testlbl11.grid(column=6,row=1)

type7=Label(window,text=typename,font='Times 8')
type7.grid(column=8,row=0)
testlbl13=Label(window,text=gen_string(door),font='Times 10')
testlbl13.grid(column=8,row=1)



name1=Label(window,text=namecard,font='Times 8')
name1.grid(column=1,row=0)
testlbl2=Label(window,text=gen_string(namemonstrs),font='Times 10')
testlbl2.grid(column=1,row=1)

name2=Label(window,text=namecard,font='Times 8')
name2.grid(column=1,row=2)
testlbl4=Label(window,text=gen_string(nameboost),font='Times 10')
testlbl4.grid(column=1,row=3)

name3=Label(window,text=namecard,font='Times 8')
name3.grid(column=3,row=0)
testlbl6=Label(window,text=gen_string(namerasy),font='Times 10')
testlbl6.grid(column=3,row=1)

name4=Label(window,text=namecard,font='Times 8')
name4.grid(column=3,row=2)
testlbl8=Label(window,text=gen_string(nameproklyatie),font='Times 10')
testlbl8.grid(column=3,row=3)

name5=Label(window,text=namecard,font='Times 8')
name5.grid(column=5,row=0)
testlbl10=Label(window,text=gen_string(namelevel),font='Times 10')
testlbl10.grid(column=5,row=1)

name6=Label(window,text=namecard,font='Times 8')
name6.grid(column=7,row=0)
testlbl12=Label(window,text=gen_string(nameshmot),font='Times 10')
testlbl12.grid(column=7,row=1)

name7=Label(window,text=namecard,font='Times 8')
name7.grid(column=9,row=0)
testlbl14=Label(window,text=gen_string(namedoor),font='Times 10')
testlbl14.grid(column=9,row=1)





btn=Button(window,text='start',command=start)
btn.grid(column=7,row=4)
result=Label(window,text='вход не выполнен')
result.grid(column=7,row=5)

noumber=Entry(window)
noumber.grid(column=8,row=4)
btn2=Button(window,text='Введи номер лобби',command=get_num_lobby)
btn2.grid(column=8,row=5)

test=Label(window,text='kol-vo card',font='Times 8')
test.grid(column=9,row=4)
window.mainloop()