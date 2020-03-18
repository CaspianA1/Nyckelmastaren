# defenses.py

from maps import Position


class Defenses:
    def __init__(
        self, absorb, probdefense, name, description, battle_phrase, miss_phrase
    ):
        self.absorb = absorb
        self.probdefense = probdefense
        self.name = name
        self.description = description
        self.battle_phrase = battle_phrase
        self.miss_phrase = miss_phrase


chest_block = Defenses(
    absorb=5,
    probdefense=0.9,
    name="chest block",
    description="",
    battle_phrase="You blocked the {}'s attack with a chest block!",
    miss_phrase="The {}'s speed left you unable to block.",
)

run_away = Defenses(
    absorb = 0,
    probdefense=0.3,
    name="run away",
    description="",
    battle_phrase="You ran away from the {}'s {}, losing your chance at gaining any experience.",
    miss_phrase="While trying to run away, the {} snatched you right back.",
)

duck = Defenses(
    absorb=0,
    probdefense=0.6,
    name="duck",
    description="",
    battle_phrase="You avoided the {}'s attack!",
    miss_phrase="While trying to duck, the {} knocked you off your feet.",
)

quick_dodge = Defenses(
    absorb=15,
    probdefense=0.5,
    name="quick dodge",
    description="",
    battle_phrase="You darted to the side, avoiding the {}'s attack!",
    miss_phrase="While trying to dodge, the {} knocked you down.",
)

all_defenses = (chest_block, run_away, duck, quick_dodge)
