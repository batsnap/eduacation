from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
 
vk = vk_api.VkApi(token="5f42f19a10449102a600724e997d146ed5166df553696bf1b49afec75350ece076ddea129e0cefbbc1ebd")
 
vk._auth_token()
 
vk.get_api()
 
longpoll = VkBotLongPoll(vk,192026272)
 
while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id != event.object.from_id:
                if event.object.text() == "привет":
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": event.object.text,
                                                "random_id": 0})
            elif event.object.peer_id == event.object.from_id:
                if event.object.text() == "привет":
                    vk.method("messages.send", {"user_id": event.object.from_id, "message": event.object.text,
                                                "random_id": 0})