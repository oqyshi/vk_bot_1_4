import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
import random

session = {}
vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()


def main():
    for event in longpoll.listen():
        print(event)
        if event.obj.message:
            name = vk.users.get(user_id=event.obj.message['from_id'])[0]['first_name']
            city = None
            try:
                city = vk.users.get(user_id=event.obj.message['from_id'], fields='city')[0]['city']['title']
            except Exception:
                pass
            if city:
                vk.messages.send(peer_id=event.obj.message['from_id'],
                                 message=f'Привет, {name}! Как поживает {city}?',
                                 random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(peer_id=event.obj.message['from_id'],
                                 message=f'Привет, {name}!',
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
