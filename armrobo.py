#! /usr/bin/python

import curses
import serial
import time
import termcolor as tm


stdscr = curses.initscr()#creates a window object(stdscr)
#curses.start_color()#allows to change color
#curses.noecho()#no echo in the terminal
curses.cbreak()#no need to press the "Enter key" to keys take action
stdscr.keypad(1)#enable special keys ####curses.KEY_LEFT
curses.curs_set(0)#no cursor on the screen 
#initialize port
serPort = "/dev/ttyACM0"
baudRate = 9600
ser = serial.Serial(serPort, baudRate)
#stdscr.addstr(1, 1, "Serial port " + serPort + " opened Baudrate " + str(baudRate),curses.A_BOLD)
x = 0

while 1:
  in_var = stdscr.getch()
                        #motor 1
  if in_var == ord('o'):
    stdscr.addstr(21, 7, "hola",curses.A_BOLD)
    ser.write("o")
    pos1 = ser.read()
    stdscr.addstr(4, 38, str(pos1),curses.A_BOLD)
    stdscr.refresh()
  elif in_var == ord('p'):
    ser.write("p")
    pos1 = ser.read()
    stdscr.addstr(4, 38, str(pos1),curses.A_BOLD)
                          #motor 2
  elif in_var == ord('i'):
    ser.write("i")
    pos2 = ser.read()
    stdscr.addstr(6, 38, str(pos2),curses.A_BOLD)
  elif in_var == ord('k'):
    ser.write("k")
    pos2 = ser.read()
    stdscr.addstr(6, 38, str(pos2),curses.A_BOLD)
                          #motor 3
  elif in_var == ord('d'):
    ser.write("d")
    pos3 = ser.read()
    stdscr.addstr(8, 38, str(pos3),curses.A_BOLD)
  elif in_var == ord('f'):
    ser.write("f")
    pos3 = ser.read()
    stdscr.addstr(8, 38, str(pos3),curses.A_BOLD)
                          #motor 4
  elif in_var == ord('u'):
    ser.write("u")
    pos4 = ser.read()
    stdscr.addstr(10, 38, str(pos4),curses.A_BOLD)
  elif in_var == ord('j'):
    ser.write("j")
    pos4 = ser.read()
    stdscr.addstr(10, 38, str(pos4),curses.A_BOLD)
    stdscr.addstr(12, 39, "hola",curses.A_BOLD)
                          #motor 5
  elif in_var == ord('a'):
    ser.write("a")
    pos5 = ser.read()
    stdscr.addstr(12, 38, str(pos5),curses.A_BOLD)
  elif in_var == ord('s'):
    ser.write("s")
    pos5 = ser.read()
    stdscr.addstr(12, 38, str(pos5),curses.A_BOLD)
  elif in_var == ord('q'):
    break

  stdscr.addstr(20, 20, str(in_var),curses.A_BOLD)
  stdscr.refresh()

curses.nocbreak(); stdscr.keypad(0); curses.echo(); curses.endwin()#end curses
ser.close() 