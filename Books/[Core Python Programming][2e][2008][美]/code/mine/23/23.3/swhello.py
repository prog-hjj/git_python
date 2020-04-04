#!/usr/bin/env jython
#
# TODO: NOT TESTED for lazy to install (Jython)

from pawt import swing
import sys
from java.awt import Color, BorderLayout

def quit(e):
    sys.exit()

top = swing.JFrame("PySwing")
box = swing.JPanel()
hello = swing.JLabel("Hello World!")
quit = swing.JButton("QUIT", actionPerformed=quit,
    background=Color.red, foreground=Color.white)

box.add("North", hello)
box.add("South", quit)
top.contentPane.add(box)
top.pack()
top.visible = 1  # or True for Jython 2.2+
