# -*- coding: utf-8 -*-
import sys,os
import curses
import locale
from subprocess import call
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

def base(musicd, test):
	# start
	# musicd = curses.initscr()
	# curses.noecho()
	# curses.cbreak()
	# musicd.keypad(1)

	# draw
	k = 0
	cursor_x = 0
	cursor_y = 0

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
		func(musicd, status)

		musicd.move(cursor_y, cursor_x)
		# Refresh the screen
		musicd.refresh()

		# Wait for next input
		k = musicd.getch()

def func(musicd, status):

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
	musicd.addstr(height-4,0,"<Cecile Corbel - Take me hand.flac>            4m32s   70%")
	musicd.refresh()

	# btns

	btns_list = [
		[height-3, 0, "[ ⏮  Prev ]", "say 'P'"],
		[height-3, 14, "[ ⏯  Play/Pause ]", "say 'P'"],
		[height-3, 33, "[ ⏭  Next ]", "say 'P'"],
		[height-3, 47, "[ ⏹  Stop ]", "say 'P'"],
		[height-2, 7, "[ ⏪ Slow ]", "say 'P'"],
		[height-2, 19, "[ ⏩ Quick ]", "say 'P'"],
		[height-2, 46, "🔊", "say 'P'"],
		[height-2, 50, "▂", "say 'P'"],
		[height-2, 52, "▃", "say 'P'"],
		[height-2, 54, "▅", "say 'P'"],
		[height-2, 56, "▆", "say 'P'"],
		[height-2, 58, "▇", "say 'P'"]
	]
	musicd.addstr(height-2,0,"Speed  [ ⏪ Slow ]  [ ⏩ Quick ]        Sound")

def [y, x, text, script):
	# highlight
	if status[0] == y and status[1] >= x and status[1] <= x+len(text)-3:
		musicd.attron(curses.color_pair(1))
		musicd.addstr(y, x, text)
		musicd.attroff(curses.color_pair(1))
		if status[2] == 10 or status[2] == 32:
			call(script,shell=True)
	else:
		musicd.addstr(y, x, text)
	# entry
	



def main():
	curses.wrapper(base, test=1)

main()

# # exit
# musicd.getch()
# curses.nocbreak()
# musicd.keypad(0)
# curses.echo()
# curses.endwin()