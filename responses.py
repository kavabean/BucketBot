import random


def get_response(message: str, username) -> str:

    user = username.lower()
    p_message = message.lower()
    rando = random.randint(1, 30)
    print(rando)
    if 'hanni' in p_message:
        return 'mid'

    if rando == 1:
        return 'hanni is mid'

    if rando == 2:
        return f'"{message}" is something a fool would say.'

    if rando == 21 and 'joomillion' in username:
        return 'midmillion'

    return
