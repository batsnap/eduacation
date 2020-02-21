import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
vk_session = vk_api.VkApi(token='5f42f19a10449102a600724e997d146ed5166df553696bf1b49afec75350ece076ddea129e0cefbbc1ebd')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
print('start bot')
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
    #Слушаем longpoll, если пришло сообщение то:			
        if event.text == 'привет':
            if event.from_user: #Если написали в ЛС
                vk.messages.send(user_id=event.user_id,message='Ваш текст',random_id='')
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send(chat_id=event.chat_id,message='Ваш текст',random_id='')
            else:
                vk.messages.send(peer_id=event.peer_id,message='Ваш текст',random_id='')
                
