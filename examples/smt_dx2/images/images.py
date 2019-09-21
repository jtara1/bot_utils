from os.path import join, dirname


class Images:
    __dir = dirname(__file__)
    __dir_demons_turn = join(__dir, 'demons_turn')
    __dir_demons_status = join(__dir, 'demons_status')
    __dir_demons_party_portrait = join(__dir, 'demons_party_portrait')
    __dir_ui = join(__dir, 'ui')

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
    apocalypse = join(__dir, 'apocalypse.PNG')

    # demons status
    concentrate_status = join(__dir_demons_status, 'concentrate3.PNG')  # alt: 'concentrate.png'

    # fame exchange
    exchange_100 = join(__dir, 'ex-100.PNG')

    # general ui
    next = join(__dir, 'next.png')
    close = join(__dir, 'close.PNG')

    # hells park ui
    one = join(__dir_ui, '1.PNG')
    two = join(__dir_ui, '2.PNG')
    three = join(__dir_ui, '3.PNG')
    four = join(__dir_ui, '4.PNG')
    five = join(__dir_ui, '005.PNG')
    six = join(__dir_ui, '006.PNG')
    seven = join(__dir_ui, '007.PNG')
    eight = join(__dir_ui, '008.PNG')
    nine = join(__dir_ui, '009.PNG')
    ten = join(__dir_ui, '010.PNG')

    # other ui
    enter = join(__dir_ui, 'enter2.PNG')

    # portraits of demons when the current turn is their tur
    trump = join(__dir_demons_turn, 'trump.PNG')
    fenrir = join(__dir_demons_turn, 'fenrir.PNG')
    jack_frost = join(__dir_demons_turn, 'jack-frost.PNG')
    pyro_jack = join(__dir_demons_turn, 'pyro-jack.PNG')
