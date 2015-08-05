#!/usr/bin/python

import urwid
import urwid.curses_display
import loginview


"""
NOTES
-----
These are the possible colors we can use:
black, dark red, dark green, brown, dark blue, dark magenta, dark cyan, light gray

This file is an attempt to remove the object oriented approach of having the 
screen implementation be in a class. I don't think it makes much sense to use
classes here as we aren't dealing with objects.
So, I'm trying to make it a functional programming approach.

!!!!
I just read on urwid's site that urwid.AttrWrap is deprecated
http://urwid.org/reference/deprecated.html
it's not absolutely necessary to change all the previous ones right now, but
moving forward we should use AttrMap
http://urwid.org/reference/widget.html#attrmap

"""

#This class is used to store all of the data pertaining to the database connection
#It is used in a similar manner to a C struct
class UserDBInfo:
  def __init__(self):
    self.db_uname = ""
    self.db_name = ""
    self.db_pw = ""
    self.db_conn = ""
    self.db_obj = ""
    self.psql = False
    self.mysql = False

#This is the color palette used for the program. the format is "name, foreground, background"
palette = [
  ('header', 'light gray', 'dark red'),
  ('topmenu', 'light gray', 'dark blue'),
  ('leftside', 'light gray', 'dark cyan'),
  ('body', 'black', 'light gray'),
  ('bg', 'black', 'light gray'),
  ('btn','light gray','dark cyan'),
  ('btnf','light gray','dark blue'),
  ('main_sel', 'black', 'light gray'),
  ('main_self', 'light gray', 'black'),
  ('selected', 'light gray', 'dark red'),
  ('error', 'light gray', 'dark red')
]

#Main function to start the program
def main():
  #creating the object to store all database information
  user_info = UserDBInfo()

  #This function handles all input that isn't directly handled by a widget. This is
  #what allows the user to exit the program.
  def unhandled_input(key):
    if key == 'q':
      user_info.db_conn.close()
      raise urwid.ExitMainLoop()

  #call function to create login screen widget, which is opening widget used
  login_widget = loginview.create_main_view(user_info)
  
  #create loop variable and then call urwid event loop
  loop = urwid.MainLoop(login_widget, palette, unhandled_input=unhandled_input, screen=urwid.curses_display.Screen())
  loop.run()


if __name__ == '__main__':
  main()
