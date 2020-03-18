# swords.py

class Sword:
    def __init__(self, name, mapletter, strength, description, has_animation = False):
        self.name = name
        self.mapletter = mapletter
        self.strength = strength
        self.description = description
        self.has_animation = has_animation


null_sword = Sword(
    name="null sword", mapletter="h", strength=None, description="This is a null sword."  # TODO: Not needed (maybe?)
)

rusty_sword = Sword(
    name="rusty sword",
    mapletter="r",
    strength=10,
    description="This is a rusty old sword that you found on the ground.",
    has_animation = True
)
gold_sword = Sword(
    name="gold sword",
    mapletter="g",
    strength=30,
    description="This is a fine golden sword, with a crown engraved on the handle.",
    has_animation = True
)
diamond_sword = Sword(
    name="diamond sword",
    mapletter="d",
    strength=50,  # TODO: use sword descriptions
    description="This 100% pure diamond sable is of the finest quality. It reflects a prism of light when you turn it back and forth.",
    has_animation = True

)
plasma_sword = Sword(
    name="plasma sword",
    mapletter="p",
    strength=100,
    description="This plasma sword can slay any opponent. With this, you are unstoppable.",
    has_animation = True
)

bucky_ball = Sword(
    name="bucky ball",
    mapletter="bb",
    strength=10000,
    description="This is the best weapon ever!",
    has_animation = True
)

all_swords = (rusty_sword, gold_sword, diamond_sword, plasma_sword, bucky_ball)
