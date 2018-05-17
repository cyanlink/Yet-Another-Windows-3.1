# -*- coding: utf-8 -*-
import curses
import locale
locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

# start
musicd = curses.initscr()
curses.noecho()
curses.cbreak()
musicd.keypad(1)

# in
# musicd.addstr("		121312312312")
# musicd.addstr("\n		112312312321")
# musicd.addstr("\n		112312312321")
height, width = musicd.getmaxyx()
musicd.addstr(height-4,0,"<Cecile Corbel - Take me hand.flac>		4m32s	70%")
musicd.addstr(height-3,0,"[ ⏮  Prev ]  [ ⏯  Play/Pause ]  [ ⏭  Next ]  [ ⏹  Stop ]	")
musicd.addstr(height-2,0,"Speed  [ ⏪ Slow ]  [ ⏩ Quick ]		Sound	🔊 ▂ ▃ ▅ ▆ ▇ ")
musicd.refresh()
                                

musicd.addstr(height-5,width-32,"        ♬ 𝄞        ◥◤~~~~◥◤")
musicd.addstr(height-4,width-32,"     ♪♫            ┃　 　　┃")
musicd.addstr(height-3,width-32,".  ♩     __  __    ≡━ ﹏ ━≡")
musicd.addstr(height-2,width-32,"|\/|/  \(_ |/      ┗━━┳∞┳━━┛")
musicd.addstr(height-1,width-32,"|  |\__/__)|\__   　 ┏┫　┣┓")






# exit
musicd.getch()
curses.nocbreak()
musicd.keypad(0)
curses.echo()
curses.endwin()