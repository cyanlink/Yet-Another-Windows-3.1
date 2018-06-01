# -*- coding: utf-8 -*-
import sys,os
import curses
import locale
import subprocess
from subprocess import call
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

def base(musicd, test):

	mplayer = subprocess.Popen("mplayer -really-quiet -slave -msglevel global=4 -idle -input nodefault-bindings /Users/dimpurr/Workflow/00Programing/Shell/shell-practice/main/playground/ignore/music/*", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	mplayer.stdin.write("pause\n")

	# start
	# musicd = curses.initscr()
	# curses.noecho()
	# curses.cbreak()
	# musicd.keypad(1)

	# draw
	height, width = musicd.getmaxyx()
	k = 0
	cursor_y = height - 3
	cursor_x = 0

	musicd.clear()
	musicd.refresh()

	# Loop where k is the last character pressed
	while (k != ord('q')):

		# Initialization
		musicd.clear()
		height, width = musicd.getmaxyx()

		if k == curses.KEY_DOWN:
			cursor_y = cursor_y + 1
		elif k == curses.KEY_UP:
			cursor_y = cursor_y - 1
		elif k == curses.KEY_RIGHT:
			cursor_x = cursor_x + 1
		elif k == curses.KEY_LEFT:
			cursor_x = cursor_x - 1

		cursor_x = max(0, cursor_x)
		cursor_x = min(width-1, cursor_x)

		cursor_y = max(0, cursor_y)
		cursor_y = min(height-1, cursor_y)

		if test == 1:
			keystr = "Last key pressed: {}".format(k)[:width-1]
			statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
			if k == 0:
				keystr = "No key press detected..."[:width-1]
			musicd.addstr(0,0,keystr)
			musicd.addstr(1,0,statusbarstr)

		status = [cursor_y, cursor_x, k, height, width]
		func(musicd, status, mplayer)

		musicd.move(cursor_y, cursor_x)
		# Refresh the screen
		musicd.refresh()

		# Wait for next input
		k = musicd.getch()

def func(musicd, status, mplayer):

	# unpack
	cursor_y = status[0]
	cursor_x = status[1]
	k = status[2]
	height = status[3]
	width = status[4]

	# color
	curses.start_color()
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	# right
	musicd.addstr(height-5,width-32,"        ♬ 𝄞        ◥◤~~~~◥◤")
	musicd.addstr(height-4,width-32,"     ♪♫            ┃　 　　┃")
	musicd.addstr(height-3,width-32,".  ♩     __  __    ≡━ ﹏ ━≡")
	musicd.addstr(height-2,width-32,"|\/|/  \(_ |/      ┗━━┳∞┳━━┛")
	musicd.addstr(height-1,width-32,"|  |\__/__)|\__   　 ┏┫　┣┓")


	# left
	height, width = musicd.getmaxyx()
	musicd.addstr(height-4,0,"<Cecile Corbel - Take me hand.flac>")

	# btns
	btns_list = [
		[height-3, 0, "[ ⏮  Prev ]", "pt_step -1"],
		[height-3, 14, "[ ⏯  Play/Pause ]", "pause"],
		[height-3, 34, "[ ⏭  Next ]", "pt_step 1"],
		[height-3, 48, "[ ⏹  Stop ]", "seek 0 1\npause"],
		[height-2, 8, "[ ⏪ Slow ]", "speed_incr -0.1'"],
		[height-2, 20, "[ ⏩ Quick ]", "speed_incr +0.1"],
		[height-2, 44, "🔊", "volume 0"],
		[height-2, 47, "▂", "volume 0.2"],
		[height-2, 49, "▃", "volume 0.4"],
		[height-2, 51, "▅", "volume 0.6"],
		[height-2, 53, "▆", "volume 0.8"],
		[height-2, 55, "▇", "volume 1"]
	]
	musicd.addstr(height-2,0,"Speed                               Volume")
	for i in range(len(btns_list)):
		btn = btns_list[i]
		btns(btns_list, musicd, status, btn[0], btn[1], btn[2], btn[3], i, mplayer, height)

	musicd.refresh()

def btns(btns_list, musicd, status, y, x, text, script, i, mplayer, height):
	# highlight
	if status[0] == y and status[1] >= x and status[1] <= x+len(text)-3:
		musicd.attron(curses.color_pair(1))
		musicd.addstr(y, x, text)
		musicd.attroff(curses.color_pair(1))

		# enter
		if status[2] == 10 or status[2] == 32:

			# mplayer.stdin.write("get_property speed\n")
			# # a = mplayer.stdout.read(0)
			# # mplayer.stdout.truncate()
			# a = mplayer.stdout.readline()[10:-4]
			# musicd.addstr(height-2,7, a)
			# # mplayer.stdin.write("pause\n")

			# call(script,shell=True)
			mplayer.stdin.write(script+'\n')
			
	else:
		musicd.addstr(y, x, text)

def main():
	curses.wrapper(base, test=0)

main()

# # exit
# musicd.getch()
# curses.nocbreak()
# musicd.keypad(0)
# curses.echo()
# curses.endwin()