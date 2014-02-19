#!/usr/bin/env python

############################################################
"""
It is a list of devices which will be turned off in tabletMode.
If you want you can edit this list.
To find out devices of your PC input command:
  $ xinput --list
"""
DevNumList = [
  'Video Bus', 
  'Lenovo EasyCamera', 
  'AT Translated Set 2 keyboard', 
  'SynPS/2 Synaptics TouchPad'
  ]
############################################################

import subprocess
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'top', '1')
Config.set('graphics', 'left', '1')
Config.set('graphics', 'resizable', '0')
Config.set('kivy', 'window_icon', './icon.png')
Config.write()

class tabletModeApp(App):
  __tableMode = False
  def build(self):
    self.toggleButton = Button(text='Turn to TabletMode', color = [1,1,0,1])
    self.toggleButton.bind(on_press=self.toggle)
    return self.toggleButton

  def toggle(self, *args):
    for curDevNum in DevNumList :
      subprocess.call(['xinput', 'set-int-prop', curDevNum, "Device Enabled", '8', str(int(self.__tableMode))])
    if self.__tableMode :
      self.toggleButton.text = 'Turn to TabletMode'
      self.toggleButton.color = [1,1,0,1]
      self.__tableMode = False
      print 'Laptop mode'
    else:
      self.toggleButton.text = 'Turn to LaptopMode'
      self.toggleButton.color = [0,1,0,1]
      self.__tableMode = True
      print 'Tablet mode'

  def on_stop(self, *args):
    self.__tableMode = True
    self.toggle()

if __name__ == '__main__':
  tabletModeApp().run()

