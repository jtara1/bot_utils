from os.path import join, dirname


class Images:
    __dir = dirname(__file__)
    __dir_demons_turn = join(__dir, 'demons_turn')

    # duel lobby
    duel = join(__dir, 'duel.png')
    start_duel = join(__dir, 'start-duel.png')

    # fight entrance & exit
    victory = join(__dir, 'victory3.png')
    lose = join(__dir, 'lose.PNG')

    # duel / fight
    auto_on = join(__dir, 'auto on (off state).png')
    auto_off = join(__dir, 'auto on (on state).png')
    concentrate = join(__dir, 'concentrate.png')
    pass_turn = join(__dir, 'pass.png')
    tag = join(__dir, 'tag.png')

    # fame exchange
    exchange_100 = join(__dir, 'ex-100.PNG')

    # general ui
    next = join(__dir, 'next.png')
    close = join(__dir, 'close.PNG')

    # portraits of demons when the current turn is their tur
    trump = join(__dir_demons_turn, 'trump.PNG')
    fenrir = join(__dir_demons_turn, 'fenrir.PNG')
    jack_frost = join(__dir_demons_turn, 'jack-frost.PNG')
    pyro_jack = join(__dir_demons_turn, 'pyro-jack.PNG')