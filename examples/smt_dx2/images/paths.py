from os.path import join, dirname


class Images:
    __dir = dirname(__file__)

    # duel lobby
    duel = join(__dir, 'duel.png')
    start_duel = join(__dir, 'start-duel.png')
    next = join(__dir, 'next.png')  # general
    lose = join(__dir, 'lose.PNG')

    # duel / fight
    auto_on = join(__dir, 'auto on (off state).png')
    auto_off = join(__dir, 'auto on (on state).png')
    concentrate = join(__dir, 'concentrate.png')
    pass_turn = join(__dir, 'pass.png')
    tag = join(__dir, 'tag.png')

    # fame exchange
    exchange_100 = join(__dir, 'ex-100.PNG')
    close = join(__dir, 'close.PNG')  # general
