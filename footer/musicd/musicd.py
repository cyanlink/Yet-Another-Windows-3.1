# -*- coding: utf-8 -*-
import sys
import os
import curses
import locale
from subprocess import call
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

def base(musicd, test, nowkey):
	# start
	# musicd = curses.initscr()
	# curses.noecho()
	# curses.cbreak()
	# musicd.keypad(1)

	height, width = musicd.getmaxyx()
	# draw
	k = 0
	cursor_x = height - 3
	cursor_y = 0

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

		musicd.move(cursor_y, cursor_x)

		# if k == curses.KEY_DOWN and nowkey < len(btns_list):
		# 	cursor_y = btns_list[nowkey+1][0]
		# 	nowkey += 1
		# elif k == curses.KEY_UP and nowkey > 0:
		# 	cursor_y = btns_list[nowkey-1][0]
		# 	nowkey -= 1
		# elif k == curses.KEY_RIGHT and nowkey < len(btns_list):
		# 	cursor_x = btns_list[nowkey+1][1]
		# 	nowkey += 1
		# elif k == curses.KEY_LEFT and nowkey > 0:
		# 	cursor_x = btns_list[nowkey-1][1]
		# 	nowkey -= 1

		# cursor_x = max(0, cursor_x)
		# cursor_x = min(width-1, cursor_x)

		# cursor_y = max(0, cursor_y)
		# cursor_y = min(height-1, cursor_y)

		# musicd.move(cursor_y, cursor_x)

		if test == 1:
			keystr = "Last key pressed: {}".format(k)[:width-1]
			keystr = "Last nowkey pressed: {}".format(nowkey)[:width-1]
			statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(
				cursor_x, cursor_y)
			if k == 0:
				keystr = "No key press detected..."[:width-1]
			musicd.addstr(0, 0, keystr)
			musicd.addstr(1, 0, statusbarstr)

		status = [cursor_y, cursor_x, k, height, width]
		func(musicd, status, btns_list)

		# Refresh the screen
		musicd.refresh()

		# Wait for next input
		k = musicd.getch()


def func(musicd, status, btns_list):

	# unpack
	cursor_y, cursor_x, k, height, width = status

	# color
	curses.start_color()
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	# right
	musicd.addstr(height-5, width-32, "        ♬ 𝄞        ◥◤~~~~◥◤")
	musicd.addstr(height-4, width-32, "     ♪♫            ┃　 　　┃")
	musicd.addstr(height-3, width-32, ".  ♩     __  __    ≡━ ﹏ ━≡")
	musicd.addstr(height-2, width-32, "|\/|/  \(_ |/      ┗━━┳∞┳━━┛")
	musicd.addstr(height-1, width-32, "|  |\__/__)|\__   　 ┏┫　┣┓")

	# left
	height, width = musicd.getmaxyx()
	musicd.addstr(
		height-4, 0, "<Cecile Corbel - Take me hand.flac>            4m32s   70%")
	musicd.refresh()

	# btns
	musicd.addstr(height-2, 0, "Speed  [ ⏪ Slow ]  [ ⏩ Quick ]        Sound")
	for i in range(len(btns_list)):
		btn = btns_list[i]
		btns(btns_list, musicd, status, btn[0], btn[1], btn[2], btn[3], i)


def btns(btns_list, musicd, status, y, x, text, script, i):

	# unpack
	cursor_y, cursor_x, k, height, width = status

	# highlight
	if cursor_y == y and cursor_x >= x and cursor_x <= x+len(text)-3:
		musicd.attron(curses.color_pair(1))
		musicd.addstr(y, x, text)
		musicd.attroff(curses.color_pair(1))
		nowkey = i

		# enter
		if status[2] == 10 or status[2] == 32:
			call(script, shell=True)

	else:
		musicd.addstr(y, x, text)


def main():
	curses.wrapper(base, test=1, nowkey=0)


main()

# # exit
# musicd.getch()
# curses.nocbreak()
# musicd.keypad(0)
# curses.echo()
# curses.endwin()
