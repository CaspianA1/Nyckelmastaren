# Nyckelmästaren
  
(this means Keymaster in Swedish.)

A text-based action-RPG game. Developed by Adam Winograd and I.

Inspired by games like Zork, A Link To The Past, Dragon Warrior and Mother.

![Game Poster](https://i.imgur.com/XUv2UnH.png)

## PyPi link:
- https://pypi.org/project/nyckelmastaren-casahl/1.0.0/

## Dependencies:
- Simpleaudio: https://github.com/hamiltron/py-simple-audio
- Viu: https://github.com/atanunq/viu
- Pillow: https://github.com/python-pillow/Pillow
- An installation of Rust: https://www.rust-lang.org/learn/get-started
- Python, 3.7 or above.

All in-game graphics were made without any external libraries, which I'm really happy about. It looks like an Atari 2600 game!

## Commands:
- w / north / go north
- d / east / go east
- s / south / go south
- a / west / go west
- words of encouragement
- use / item
- inventory
- location
- settings / options
- help

## Tips:
- To start a new game:
- Select "reset game" from settings.
- If you installed the game from source, enter "python3 adventuregame.py new"
- There's a hidden weapon in the wizard Salazar's lair...
- Set the game to full screen, and zoom out your terminal window a bit, to see all of the graphics as intended.

## Installation:
- Enter the following commands in your terminal.
- pip install nyckelmastaren-casahl==1.0.0
- curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
- cargo install viu

## Run:
- Enter these commands:
- python3
- import nyckelmastaren
