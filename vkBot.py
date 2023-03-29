import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from mainToken import maintoken


def send_message(user_id, message):
    session.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': 0
    })


session = vk_api.VkApi(token=maintoken)
for event in VkLongPoll(session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id

        if text == 'ку':
            send_message(user_id, 'smth text...')

