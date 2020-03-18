# audio_control.py

import os
import time
import simpleaudio as sa
from threading import Thread
from maps import Position

pos_obj = Position()

class SoundWrapper:
	def __init__(self, track_name, play_obj):
		self.track_name = track_name
		self.play_obj = play_obj


wrapped_sound_obj = SoundWrapper(
	track_name = "",
	play_obj = None,
	)


pos_audio_binding = {
	"do": "8-Bit 2.wav",

	"h": "8-Bit 2.wav",
	"h0.5": "8-bit 16.wav",
	"h0.75b": "8-Bit 12.wav",
	"h0.75t": "8-Bit 12.wav",
	"h2": "8-Bit 7.wav",
	# "h2": "8-Bit 8.wav",
	"h3": "8-Bit 9.wav",
	"h4": "8-Bit 20.wav",
	"h5": "8-Bit 12.wav",

	"bl": "8-Bit 9.wav",

	"acr2_bb": "8-Bit 17.wav",
	"acrbb_2": "8-Bit 17.wav",
	"bbf": "8-Bit 17.wav",
	"bb": "8-Bit 17.wav",

	"pch": "8-Bit 18_.wav",
	"bu": "8-Bit 18_.wav",
	"la": "8-Bit 21.wav",
	"ch": "8-Bit 21.wav",

	"so": "8-Bit 18_.wav",
	"mm": "8-Bit 18_.wav",
	"cf": "8-Bit 21.wav",
	"wh": "8-Bit 21.wav",

	"gu": "8-Bit 13.wav",
	"ni": "8-Bit 13.wav",
	"to": "8-Bit 13.wav",

	"usta0_1": "8-Bit 11.wav",
	"dsta1_0": "8-Bit 11.wav",
	"usta1_2": "8-Bit 11.wav",
	"dsta2_1": "8-Bit 11.wav",
	"acr0_0.5": "8-Bit 11.wav",
	"acr0.5_0": "8-Bit 11.wav",
	"acr0.5_0.75": "8-Bit 13.wav",  # before: 8-Bit 25.wav
	"acr0.75_0.5": "8-Bit 13.wav",  # before: 8-Bit 25.wav
	"acr0.75_home": "8-Bit 13.wav",
	"acrhome_0.75": "8-Bit 13.wav",
	"acr0.75_plaza": "8-Bit 13.wav",
	"acrplaza_0.75": "8-Bit 13.wav",

	"t": "8-Bit 3 copy 2.wav",
	"go": "8-Bit 3 copy 2.wav",
	"o": "8-Bit 10.wav",
	"hu": "8-Bit 10.wav",
	"dr": "8-Bit 19.wav",
	"m": "8-Bit 19.wav",
	"w": "8-Bit 23.wav",

	"r": "8-Bit 4.wav",
	"g": "8-Bit 4.wav",
	"d": "8-Bit 14.wav",
	"p": "8-Bit 21.wav",

	"bk": "8-Bit 11.wav",
	"sk": "8-Bit 24.wav",
	"gk": "8-Bit 21.wav",

	# "G": "8-Bit 1.wav",  # this will be changed.
	# "W": "8-Bit 1.wav",
	# "BW": "8-Bit 1.wav",
	# "A": "8-Bit 1.wav",
	# "h0.25": "8-Bit 25.wav",


	"En": "8-Bit 25.wav",
	"h0.25": "8-Bit 1.wav",
	"be": "8-Bit 1.wav",
	"wi": "8-Bit 1.wav",

	"h0": "8-Bit 20.wav",


	# use:
	# 8-Bit 5.wav



}

# idea idea idea:
# a null position, like "", which can be set easily
# or, some way to choose your own music based on this - set it to an imaginary position of like "lightning-bolt-castle"
# during a cutscene
# and then turn it back to its real position again


def play_audio(track_name):
	wave_dir = os.getcwd() + "/Assets/Audio/WAV_New/" + track_name
	wave_obj = sa.WaveObject.from_wave_file(wave_dir)
	play_obj = wave_obj.play()
	return play_obj

'''See below.'''
'''There needs to be a timer. Here's why:'''
'''If there is no pause, this will check'''
'''for the position a ton of times per second.'''
'''Checking so often, eventually, when the'''
'''positon is changing, that file will be'''
'''empty for a split second. This yields an error.'''
'''With the pause, that file has time to update - and not have'''
'''a split second where it is empty when going through this loop again and again.'''

# error: writing to prmat and plmat file takes way too long. Like, a whole second.

var_dir = os.getcwd() + "/Assets/Global_Vars/"

def stop_audio():
    with open(f"{var_dir}audio_stop_check.txt", "w"):
        pass

def main_audio_loop():
	global wrapped_sound_obj

	while True:
		if open(f"{var_dir}audio_stop_check.txt", "r").read() == "":
			break

		time.sleep(1)
		pos = pos_obj.global_pos("get")
		# print("Pos: " + str(pos))
		pos_x, pos_y = pos[0], pos[1]
		prmat = pos_obj.get_mat("prmat")
		# print("PRMAT: " + str(prmat))
		track = pos_audio_binding[prmat[pos_x][pos_y]]

		# print("track: " + track)

		if wrapped_sound_obj.track_name != track:
			sa.stop_all()
			play_obj = play_audio(track)
			wrapped_sound_obj.track_name = track
			wrapped_sound_obj.play_obj = play_obj
			continue

		else:
			if wrapped_sound_obj.play_obj.is_playing() is False:
				play_obj = play_audio(wrapped_sound_obj.track_name)
				wrapped_sound_obj.play_obj = play_obj
				continue
