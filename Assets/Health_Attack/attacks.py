# attacks.py


class Attacks:
    def __init__(
        self, power, prob_attack, name, description, battle_phrase, miss_phrase
    ):
        self.power = power
        self.prob_attack = prob_attack
        self.name = name
        self.description = description
        self.battle_phrase = battle_phrase
        self.miss_phrase = miss_phrase

kick_knee = Attacks(
    power=10,
    prob_attack=0.7,
    name="kick knee",
    description="",
    battle_phrase="You kicked the {}'s knee!",
    miss_phrase="You tried to kick the {}'s knee, but missed",
)

bash_head = Attacks(
    power=15,
    prob_attack=0.5,
    name="bash head",
    description="",
    battle_phrase="You bashed the {}'s head!",
    miss_phrase="You wound up to bash the {}'s head, but missed",
)

slash_chest = Attacks(
    power=20,
    prob_attack=0.3,
    name="slash chest",
    description="",
    battle_phrase="You slashed the {}'s chest!",
    miss_phrase="The {} was quick and avoided your slash!",
)

stab_heart = Attacks(
    power=25,
    prob_attack=0.1,
    name="stab heart",
    description="",
    battle_phrase="You stabbed the {}'s heart!",
    miss_phrase="The {} leaped to the side, avoiding your stab!",
)

all_attacks = (kick_knee, bash_head, slash_chest, stab_heart)
