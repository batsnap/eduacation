# -*- coding: utf-8 -*-
import ui
from random import randint
a={
   'пр_стегнуть':'и',
   'пр_клеить':'и',
   'пр_рисовать':'и',
   'пр_плыть':'и',
   'пр_бежать':'и',
   'пр_лететь':'и',
   'пр_открыть':'и',
   'пр_гореть':'и',
   'пр_задуматься':'и',
   'пр_морский':'и',
   'пр_школьный':'и',
   'пр_дорожный':'и',
   'пр_певать':'и',
   'пр_танцовывать':'и',
   'пр_говаривать':'и',
   'пр_ручить':'и',
   'пр_учить':'и',
   'пр_стрелить':'и',
   'пр_небрегать':'е',
   'пр_небрежение':'е',
   'пр_небрежительный':'е',
   'пр_лестный':'е',
   'пр_подобный':'е',
   'пр_следовать':'е',
   'пр_смыкаться':'е',
   'пр_зидент':'е',
   'пр_пятствие':'е',
   'пр_пона':'е',
   'пр_мьера':'е',
   'пр_тензия':'е',
   'пр_тендент':'е',
   'пр_парат':'е',
   'пр_грешения':'е',
   'пр_имущетсво':'е',
   'пр_амбула':'е',
   'пр_дел':'е',
   'камень пр_ткновения':'е',
   'пр_вратности':'е',
   'пр_пинания':'е',
   'пр_стижный':'е',
   'беспр_дельный':'е',
   'пр_словутый':'е',
   'пр_зентация':'е',
   'пр_рогатива':'е',
   'пр_терпевать':'е',
   'пр_валировать':'е',
   'пр_фектура':'е',
   'пр_цедент':'е',
   'пр_увеличить':'е',
   'пр_вередливый':'и',
   'пр_вереда':'и',
   'пр_чудливый':'и',
   'непр_ступный':'и',
   'пр_митивный':'и',
   'непр_хотливый':'и',
   'пр_влекательный':'и',
   'пр_лежный':'и',
   'пр_годный':'и',
   'пр_гожий':'и',
   'пр_ятный':'и',
   'пр_вилегия':'и',
   'пр_оритет':'и',
   'пр_ключение':'и',
   'пр_видение':'и',
   'пр_чина':'и',
   'пр_верженец':'и',
   'пр_сяга':'и',
   'пр_сягать':'и',
   'пр_каз':'и',
   'пр_казать':'и',
   'пр_сутствовать':'и',
   'пр_урочить':'и',
   'пр_дираться':'и',
   'пр_тязать':'и',
   'уровень пр_тязаний':'и',
   'беспр_страстный':'и',
   'пр_страстие':'и',
   'пр_мадонна':'и',
   'пр_ватный':'и',
   'пр_ватизация':'и',
   'пр_бор':'и',
   'непр_язнь':'и',
   'пр_баутка':'и',
   'пр_скорбный':'и',
   'пр_скорбием':'и',
   'без пр_крас':'и',
   'пр_умножить':'и',
   'пр_бывать на свежем воздухе':'е',
   'пр_бываение в городе':'е',
   'пр_творить мечты в жизнь':'е',
   'пр_твориться в жизнь':'е',
   'пр_ступить закон':'е',
   'пр_клоняться перед талантом':'е',
   'пр_дать друга':'е',
   'старинное пр_дание':'е',
   'пр_емник президента':'е',
   'пр_ходящие успех,слава':'е',
   'пр_вратный смылс':'е',
   'пр_дел терпению':'е',
   'пр_зирать врага':'е',
   'непр_ложная истина':'е',
   'непр_менное условие':'е',
   'пр_терпеть лишения':'е',
   'пр_бывать в москву':'и',
   'пр_бывание в город':'и',
   'пр_творить дверь':'и',
   'пр_твориться спящим':'и',
   'пр_ступить к написанию сочинения':'и',
   'пр_клоняться к земле':'и',
   'пр_дать значение смысл словам':'и',
   'пр_дание большей значимости':'и',
   'купить пр_ёмник':'и',
   'пр_ходящая няня':'и',
   'пр_вратник в замке':'и',
   'боковой пр_дел в церкви':'и',
   'пр_зреть сироту':'и',
   'пр_ложение к эзаменационным билетам':'и',
   'пр_менить правило':'и',
   'пр_терпеть к неволе':'и',
   'заг_р':'а',
   'заг_релый':'о',
   'заг_орать':'о',
   'приг_рь':'а',
   'выг_рки':'а',
   'изг_рь':'а',
   'кл_нящийся':'а',
   'покл_н':'о',
   'тв_рь':'а',
   'тв_рчество':'о',
   'утв_рь':'а',
   'з_рька':'о',
   'з_рево':'а',
   'з_ря':'а',
   'оз_рять':'а',
   'з_ревать':'о',
   'уб_рать':'и',
   'уб_ру':'е',
   'заст_лать':'и',
   'заст_лю':'е',
   'заж_гать':'и',
   'заж_чь':'е',
   'выч_тать':'и',
   'выч_ты':'е',
   'соч_тать':'е',
   'соч_тание':'е',
   'ч_та':'е',
   'к_саться':'а',
   'к_снуться':'о',
   'сн_ть':'я',
   'сн_мать':'и',
   'нач_ть':'а',
   'нач_нать':'и',
   'пол_гать':'а',
   'пол_жение':'о',
   'пол_г':'о',
   'р_стение':'а',
   'выр_щеный':'а',
   'подр_сли':'о',
   'р_сток':'о',
   'Р_стислав':'о',
   'р_стовщик':'о',
   'на выр_ст':'о',
   'отр_сль':'а',
   'отр_слевой':'а',
   'ск_кать':'а',
   'выск_чить':'о',
   'ск_чек':'а',
   'ск_чу':'а',
   'ск_чи':'а',
   'ск_чкообразный':'а',
   'м_кать хлеб в молоко':'а',
   'обм_кнуть перов в чернила':'а',
   'непром_каемый плащ':'о',
   'вым_кнуть под дождем':'о',
   'ур_внять в правах':'а',
   'зар_внять в яму':'о',
   'р_внина':'а',
   'р_внение':'а',
   'ур_вень':'о',
   'пор_вну':'о',
   'р_весник':'о',
   'пл_вец':'о',
   'пл_вчиха':'о',
   'попл_вок':'а',
   'жук пл_вунец':'а',
   'пл_вуны':'ы',
   }
c=randint(0,184)
newlist = list()
x=0
r=0
for i in a.keys():
  newlist.append(i)
def start(sender):
	global x,r
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	if x==0:
		x=1
		label.text=newlist[c]
	else:
		x=0
		r=0
		label.text='Слова'
		label2.text='Ошибки'
def but(sender):
	global c,r
	t=sender.title
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	if x==0:
		pass
	else:
		if t==a.get(newlist[c]):
			c=randint(0,184)
			label.text=newlist[c]
		else:
			r+=1
			label2.text='Ошибки'+str(r)

v = ui.load_view()
v.present('sheet')
