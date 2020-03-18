# status_screen.py

from ..Miscellaneous.formatting import Format

screen_part_1 = """
/ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \\
| HP: {} Hunger: {} Dehydration: {} _ _ _ _ |
| Phys Strength: {} Mental Strength: {} _ _ |
| Psychic Powers: {} Intelligence: {} _ _ _ |
| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |
\\ {} key{} left to find. Sword: {} _ /
"""
BLACK_BLOCK = "\033[48;5;210m" + " " + "\033[0m"

def print_status_screen(all_stats, keys_left, strongest_sword):
    for index, value in enumerate(all_stats):
        all_stats[index] = int(value)
    if strongest_sword == "No sword":
        strongest_sword += " _ "

    prefix = "s"
    if keys_left == 1:
        prefix = ""
    part_1_data = screen_part_1.format(
        all_stats[0], all_stats[1], all_stats[2],all_stats[3],
        all_stats[4], all_stats[5], all_stats[6], keys_left, prefix,
        strongest_sword.capitalize()
        )

    print(part_1_data)
