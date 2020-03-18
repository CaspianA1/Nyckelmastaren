# enemies.py

# when an enemy dies, you get money.
# subclass with polymorphism for different enemies, and then instances of those individual enemies

from maps import Position
import random

pos_class = Position()


class Enemy:
    def __init__(
        self,
        *args,
        name=None,
        mapletter=None,
        defense_chance=None,
        fs=None,  # fs = fighting status
        hp=None,
        will_init=None,
        strength=None,
        nullenemy=None,
        troll=None,
        goblin=None,
        ogre=None,
        huldra=None,
        draugr=None,
        moloch=None,
        wizard=None,
        description=None,
        attack_message=None,
        attack_message_2=None,
        kill_stats_incr=None
    ):
        self.name = name
        self.mapletter = mapletter
        self.defense_chance = defense_chance
        self.fs = fs  # fs is fighting status
        self.hp = hp
        self.will_init = will_init
        self.strength = strength
        self.nullenemy = nullenemy
        self.troll = troll
        self.goblin = goblin
        self.ogre = ogre
        self.huldra = huldra
        self.draugr = draugr
        self.moloch = moloch
        self.wizard = wizard
        self.description = description
        self.attack_message = attack_message
        self.attack_message_2 = attack_message_2
        self.kill_stats_incr = kill_stats_incr


nullenemy = Enemy(
    name="nullenemy",
    mapletter="h",
    # defense_chance=80,  # as in 80%
    defense_chance=None,
    fs=False,
    hp=0,
    will_init=0,
    # probesc=None,
    strength=0,  # had to change
    nullenemy=True,
    description="This is a null enemy.",
    attack_message="No attack here.",
    attack_message_2="",
    kill_stats_incr={
        "hp": 5,
        "phys strength": 1,
        "mental strength": 2,
        "psychic powers": 0.5,
        "intelligence": 1,
    },
)
# all spaces in the game count as a standard null enemy spot. Once you have beaten an enemy, that spot is replaced with a nullenemy spot.

troll = Enemy(
    name="troll",
    mapletter="t",
    defense_chance=65,
    fs=False,
    hp=40,
    will_init=0.5,
    strength=20,
    troll=True,
    description="This troll doesn't look very scary. You can take it!",
    attack_message="The troll picked you up, smashing you against the cobblestone wall!",  # brick before
    attack_message_2="The troll tickled you so you cried!",
    kill_stats_incr={
        "hp": 10,
        "phys strength": 2,
        "mental strength": 4,
        "psychic powers": 1,
        "intelligence": 2,
    },
)
goblin = Enemy(
    name="goblin",
    mapletter="go",
    defense_chance=55,  # 60
    fs=False,
    hp=30,  # 100
    will_init=1,
    strength=30,
    goblin=True,
    description="This goblin seems a bit suspicious. Be careful...",
    attack_message="The goblin slashed you with its scythe!",
    # attack_message_2="The goblin smashed your rib with a sledgehammer!",
    attack_message_2="The goblin stabbed you with its scythe!",
    kill_stats_incr={
        "hp": 11,
        "phys strength": 4,
        "mental strength": 6,
        "psychic powers": 2,
        "intelligence": 4,
    },
)
ogre = Enemy(
    name="ogre",
    mapletter="o",
    defense_chance=45,  # 55
    fs=False,
    hp=120,
    will_init=0.7,
    strength=40,
    ogre=True,
    description="Is this Shrek? Sure smells like it.",
    attack_message="The ogre struck you with a machete!",
    # attack_message_2="The fat ogre kicked you in the stomach!",
    attack_message_2="The fat ogre sliced your forearm!",  # open your forearm!
    kill_stats_incr={
        "hp": 12,
        "phys strength": 5,
        "mental strength": 7,
        "psychic powers": 3,
        "intelligence": 5,
    },
)
huldra = Enemy(
    name="huldra",
    mapletter="hu",
    defense_chance=35,  # 50
    fs=False,
    hp=130,
    will_init=0.7,
    strength=50,
    huldra=True,
    description="Her harmonious voice enchants you. Do not let her take you away...",
    attack_message="The huldra began to hypnotize you. Do not let yourself be so weak...",
    attack_message_2="The huldra started to lure you into her cave. Resist!",
    kill_stats_incr={
        "hp": 13,
        "phys strength": 6,
        "mental strength": 8,
        "psychic powers": 4,
        "intelligence": 6,
    },
)
draugr = Enemy(
    name="draugr",
    mapletter="dr",
    defense_chance=25,  # 45
    fs=False,
    hp=150,
    will_init=0.6,
    strength=60,
    draugr=True,
    description="Draugrs can live forever! Think carefully about this...",
    attack_message="The draugr chopped your right hand off!",
    attack_message_2="The draugr cut your cheek with its sword!",
    kill_stats_incr={
        "hp": 14,
        "phys strength": 7,
        "mental strength": 9,
        "psychic powers": 5,
        "intelligence": 7,
    }
    # in some way, print the moloch image to a new terminal window
)

moloch = Enemy(
    name="moloch",
    mapletter="m",
    defense_chance=20,  # 40
    fs=False,
    hp=150,
    will_init=0.6,
    strength=70,
    moloch=True,
    description="The moloch will eat your children. Escape while you can!",
    attack_message="The moloch rammed you with its mighty horns!",
    attack_message_2="The moloch howled at you, making you scared!",
    kill_stats_incr={
        "hp": 15,
        "phys strength": 2,
        "mental strength": 4,
        "psychic powers": 6,
        "intelligence": 8,
    },
)
wizard = Enemy(
    name="wizard",
    mapletter="w",
    defense_chance=15,  # 35
    fs=False,
    hp=160,
    will_init=1,
    strength=80,  # 140  # 200
    wizard=True,
    # description="Wizard Salazar has been waiting for you. Leave heed his sly tricks, for he has many...",
    description="Wizard Salazar has been waiting for you. Pay note to his sly tricks, for he has many...",
    attack_message="Salazar sliced your chest open with his infinite powers, leaving you weak...",
    attack_message_2="Salazar's mighty staff echoed through the spire, knocking you down.",
    kill_stats_incr={
        "hp": 16,
        "phys strength": 3,
        "mental strength": 5,
        "psychic powers": 7,
        "intelligence": 9,
    },
)

# all_enemies = (nullenemy, troll, goblin, huldra, draugr, moloch, wizard)
all_enemies = (troll, goblin, ogre, huldra, draugr, moloch, wizard)


# The goblin stabbed you with its burning pitchfork.
