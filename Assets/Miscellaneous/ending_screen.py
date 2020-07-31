# ending_screen.py

# credits: caspian ahlberg, adam, winograd, christopher ahlberg, and stack overflow

import os, time, random
from .reset_game import partial_reset
from .formatting import Format  # periods before there
from ..Audio.audio_control import play_audio

frm = Format()

message = ("{}With the wizard slayed, you reign as the rightful king of these lands.",
"{}After nearly fifty years, the townspeople may finally return from hiding.",
"{}They thank you for saving them, but most importantly, thank you,",
"{}The player, for playing my game. I worked on it with a great team,",
"{}and I hope to work on more games with many more. If you want to see",
"{}any of my other projects, go to https://github.com/CaspianA1/ if you're curious.",
"{}Credits:",
"{}- Caspian Ahlberg (me)",
"{}- Adam Winograd (an amazing teammate and artist)",
"{}- Christopher Ahlberg (for making simple solutions to complex problems)",
"{}- And Stack Overflow too, early on :)")

def ending_screen():
    time.sleep(1)
    frm.clear_screen()
    play_audio(f"8-Bit {random.choice((27, 28))}.wav")
    spacing = "\t" * (os.get_terminal_size()[0] // 35)
    for row in message:
        frm.printfast("\n" + row.format(spacing) + "\n", override_speed = 0.1)
    time.sleep(60)

if __name__ == "__main__":
    ending_screen()