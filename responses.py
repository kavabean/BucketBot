import random


def get_response(message: str, username) -> str:

    user = username.lower()
    p_message = message.lower()
    rando = random.randint(1, 15)
    print(rando)

    if rando == 2:
        return f'"{message}" is something a fool would say.'

    if rando == 15 and 'goob' in username:
        return 'You look like a merper not gonna lie'

    if 'jiya' in username:
        return 'You look very pretty today, as always!'
    return
