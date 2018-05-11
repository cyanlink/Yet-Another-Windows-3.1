import curses

# start
musicd = curses.initscr()
curses.noecho()
curses.cbreak()
musicd.keypad(1)

# in
musicd.border(0)
musicd.addstr(12,25,"Hello!")
musicd.refresh()

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)
win.border(0)
win.addstr(3,1,"Win!")
win.refresh()

# exit
musicd.getch()
curses.nocbreak()
musicd.keypad(0)
curses.echo()
curses.endwin()