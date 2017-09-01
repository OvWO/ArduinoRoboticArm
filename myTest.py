# #! /usr/bin/python
# # -*- coding: utf-8 -*-

# import curses, time,serial

# serPort = "/dev/ttyACM3"
# baudRate = 9600
# #ser = serial.Serial(serPort, baudRate)
# print "Serial port " + serPort + " opened  Baudrate " + str(baudRate)


# stdscr = curses.initscr()#creates a window object(stdscr)
# #  curses.start_color()#allows to change color
# curses.noecho()#no echo in the terminal
# curses.cbreak()#no need to press the "Enter key" to keys take action
# stdscr.keypad(1)#enable special keys
# curses.curs_set(0)#no cursor on the screen
# """pad = curses.newpad(100, 100)
# #  These loops fill the pad with letters; this is
# # explained in the next section
# for y in range(0, 100):
#     for x in range(0, 100):
#         try:
#             pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
#         except curses.error:
#             pass

#   #  Displays a section of the pad in the middle of the screen
#   pad.refresh(0,0, 5,5, 20,75)
#   time.sleep(3)

#   """
# while 1:
#     in_var = stdscr.getch()
#     if in_var == ord('u'):
#         print "u"
#     elif in_var == ord('q'):
#       break
# """
# stdscr.addstr(2, 3, "Current mode: Typing mode", curses.A_BOLD)
# stdscr.addstr(3, 11, "Hello", curses.A_DIM)
# stdscr.addstr(3, 11, "Hello")
# stdscr.addstr(4, 12, "Current mode: Typing mode", curses.A_BLINK)
# stdscr.addstr(5, 13, "Current mode: Typing mode", curses.A_REVERSE)

# """
# #stdscr.addstr(7, 13, "Current mode: Typing mode", curses.A_UNDERLINE)
# #  stdscr.addstr(7, 13, "Current mode: Typing mode", curses.COLOR_MAGENTA)
# #  stdscr.addstr("Pretty text", curses.color_pair(1))
# stdscr.refresh()
# #time.sleep(1)
# input()
# curses.nocbreak(); stdscr.keypad(0); curses.echo(); curses.endwin()######;ser.close() #end curses


# """

# #! /usr/bin/python

# import curses
# import random
# import time
# import serial

# window = curses.initscr()


# try:
#     (h, w) = window.getmaxyx()

#     while True:
#         x = int(random.random() * w)
#         y = int(random.random() * h)
#         window.move(y, x)
#         window.addch("*")
#         window.refresh()
#         time.sleep(0.05)
# except KeyboardInterrupt:
#     pass
# finally:
#   curses.endwin()























#   def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))
#     if '{0}'.format(key.char)  == 'u':
#       print "hola"

# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

#     """

import xbox
import serial


# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)
    
joy = xbox.Joystick()




serPort = "/dev/ttyACM0"
baudRate = 9600
ser = serial.Serial(serPort, baudRate)

print "Xbox controller sample: Press Back button to exit"
# Loop until back button is pressed
while not joy.Back():
    # Show connection status

    if joy.A():
        print "A",
        ser.write("a")
    else:
        print " ",
    if joy.B():
        print "B",
        ser.write("s")
    else:
        print " ",

    # Move cursor back to start of line
   # print chr(13),
# Close out when done
joy.close()
