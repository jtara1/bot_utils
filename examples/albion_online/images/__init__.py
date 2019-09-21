from os.path import join, dirname


class Images:
    __dir = dirname(__file__)
    __dir_ui = join(__dir, 'ui')
    __dir_items = join(__dir, 'items')

    # ui
    buy = join(__dir_ui, 'buy.png')
    pay = join(__dir_ui, 'pay.png')
    accept = join(__dir_ui, 'accept.PNG')
    take_all = join(__dir_ui, 'take-all.PNG')

    # items
    t6_fletcher_journal = join(__dir_items, 't6-fletcher-journal.PNG')
    t6_tinker_journal = join(__dir_items, 't6-tinker-journal.PNG')