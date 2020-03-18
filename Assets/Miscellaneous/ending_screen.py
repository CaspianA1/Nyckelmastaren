# ending_screen.py

# credits: caspian ahlberg, adam, winograd, christopher ahlberg, and stack overflow

import time
from .reset_game import partial_reset
from .formatting import Format

frm = Format()

f = lambda num=10: "\n" + "\t" * num

def ending_screen():
    msg1 = f"{f()}With the wizard slayed, you reign as the rightful king of these lands.\n"
    msg2 = f"{f()}After nearly fifty years, the townspeople may finally return from hiding.\n"
    msg3 = f"{f()}They thank you for saving them, but most importantly, thank you,\n"
    msg4 = f"{f()}The player, for playing my game. I worked on it with a great team,\n"
    msg5 = f"{f()}and I hope to work on more games with many more. If you want to see\n"
    msg6 = f"{f()}any of my other projects, go to https://github.com/CaspianA1/ if you're curious.\n"
    msg7 = f"{f()}Credits:\n{f()}-> Caspian Ahlberg (me){f()}-> Adam Winograd (an amazing teammate and artist){f()}-> Christopher Ahlberg (for making simple solutions to complex problems){f()}-> And Stack Overflow too, early on."

    all_msgs = (msg1, msg2, msg3, msg4, msg5, msg6, msg7)

    for msg in all_msgs:
        frm.printfast(msg)
    time.sleep(10)

if __name__ == "__main__":
    ending_screen()
