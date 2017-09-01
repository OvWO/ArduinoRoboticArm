#! /usr/bin/python
# -*- coding: utf-8 -*-
# by Luis Carlos Lopez V

#### CLEAN UP
#### ERASE READ FROM ARDUINO AND SEND FROM ARDUINO 
#### ADD MANUAL TO THE COUNTER NOUMBER OF THE DEGREEES SO THAT IT CANT BE DELETED

import curses
import serial

stdscr = curses.initscr()#creates a window object(stdscr)
#curses.start_color()#allows to change color
curses.noecho()#no echo in the terminal

curses.cbreak()#no need to press the "Enter key" to keys take action
stdscr.keypad(1)#enable special keys ####curses.KEY_LEFT
curses.curs_set(0)#no cursor on the screen 
#initialize port
serPort = "/dev/ttyACM0"
baudRate = 9600
ser = serial.Serial(serPort, baudRate)
stdscr.addstr(1, 1, "Robotic Arm",curses.A_BOLD)
stdscr.addstr(2, 1, "Running on serial port " + serPort + " opened at Baudrate " + str(baudRate),curses.A_BOLD)
pos1 = "open"
pos2 = 90
pos3 = 90
pos4 = 90
pos5 = 90

win = curses.newwin(50, 12, 0, 0)

###
stdscr.addstr(4, 3,"The curren  STATE  of motor 1 is: ",curses.A_BLINK)
stdscr.addstr(6, 3,"The current DEGREES of motor 2 is: ",curses.A_BLINK)
stdscr.addstr(8, 3,"The current DEGREES of motor 3 is: ",curses.A_BLINK)
stdscr.addstr(10, 3,"The current DEGREES of motor 4 is: ",curses.A_BLINK)
stdscr.addstr(12, 3,"The current DEGREES of motor 5 is: ",curses.A_BLINK)

stdscr.addstr(4, 38, str(pos1),curses.A_BOLD)
stdscr.addstr(6, 38, str(pos2),curses.A_BOLD)
stdscr.addstr(8, 38, str(pos3),curses.A_BOLD)
stdscr.addstr(10, 38, str(pos4),curses.A_BOLD)
stdscr.addstr(12, 38, str(pos5),curses.A_BOLD)

stdscr.addstr(4, 50,"Press");stdscr.addstr(4, 56,"O", curses.A_BOLD);stdscr.addstr(4, 58,"to open")
stdscr.addstr(5, 50,"Press");stdscr.addstr(5, 56,"P", curses.A_BOLD);stdscr.addstr(5, 58,"to close");
stdscr.addstr(6, 50,"Press");stdscr.addstr(6, 56,"I",curses.A_BOLD);stdscr.addstr(6, 58,"to go up");
stdscr.addstr(7, 50,"Press");stdscr.addstr(7, 56,"K",curses.A_BOLD);stdscr.addstr(7, 58,"to go down");
stdscr.addstr(8, 50,"Press");stdscr.addstr(8, 56,"D",curses.A_BOLD);stdscr.addstr(8, 58,"to go to the left");
stdscr.addstr(9, 50,"Press");stdscr.addstr(9, 56,"F",curses.A_BOLD);stdscr.addstr(9, 58,"to go to the right");
stdscr.addstr(10, 50,"Press");stdscr.addstr(10, 56,"U",curses.A_BOLD);stdscr.addstr(10, 58,"to go up");
stdscr.addstr(11, 50,"Press");stdscr.addstr(11, 56,"J",curses.A_BOLD);stdscr.addstr(11, 58,"to go down");
stdscr.addstr(12, 50,"Press");stdscr.addstr(12, 56,"A",curses.A_BOLD);stdscr.addstr(12, 58,"to go to the left");
stdscr.addstr(13, 50,"Press");stdscr.addstr(13, 56,"S",curses.A_BOLD);stdscr.addstr(13, 58,"to go to the right");

while True:
  in_var = stdscr.getch()
  stdscr.addstr(22, 2,"Press");stdscr.addstr(22, 8,"Q", curses.A_BOLD);stdscr.addstr(22, 10,"to quit")
  stdscr.addstr(22, 57,"Connection Established", curses.A_REVERSE)
                              #motor 1
  if in_var == ord('o'):
    ser.write("o")
    pos1 = ser.read()
    stdscr.refresh()
    stdscr.addstr(4, 38, "open",curses.A_BOLD)

    #stdscr.addstr(4, 38, str(pos1),curses.A_BOLD)
    #stdscr.refresh()
  elif in_var == ord('p'):
    ser.write("p")
    pos1 = ser.read()
    stdscr.refresh()
    stdscr.addstr(4, 38, "close",curses.A_BOLD)

    #stdscr.addstr(4, 38, str(pos1),curses.A_BOLD)
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
    stdscr.addstr(21, 1, "breaking loop",curses.A_BOLD)
    break
  # if joy.A():
  #     print "A"
  #     stdscr.addstr(21, 1, "breaking loop",curses.A_BOLD)

  # else:
  #     print " "
  #     stdscr.addstr(21, 1, "breaking loop",curses.A_BOLD)

 # stdscr.addstr(20, 20, str(in_var),curses.A_BOLD)

  stdscr.refresh()

curses.nocbreak(); stdscr.keypad(0); curses.echo(); curses.endwin()#end curses
ser.close() 
