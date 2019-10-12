from os.path import join, dirname


class Images:
    __dir = dirname(__file__)
    __dir_ui = join(__dir, 'ui')
    __dir_items = join(__dir, 'items')
    __dir_npcs = join(__dir, 'npcs')
    __dir_farm = join(__dir, 'farm')

    # ui
    buy = join(__dir_ui, 'buy.png')
    pay = join(__dir_ui, 'pay.png')
    accept = join(__dir_ui, 'accept.PNG')
    take_all = join(__dir_ui, 'take-all.PNG')
    take = join(__dir_ui, 'take.PNG')

    # items
    t6_fletcher_journal = join(__dir_items, 't6-fletcher-journal.PNG')
    t6_tinker_journal = join(__dir_items, 't6-tinker-journal.PNG')

    # npcs
    fletcher_npc = join(__dir_npcs, 'fletcher-npc3.PNG')

    # farm
    t8_herb = join(__dir_farm, 't8-herb.PNG')

    t5_herb_seeds = join(__dir_farm, 't5-herb-seeds.PNG')

    watering_can1 = join(__dir_farm, 'watering-can1.PNG')
    watering_can2 = join(__dir_farm, 'watering-can2.PNG')

    empty_dirt_field = join(__dir_farm, 'empty-dirt-field.PNG')