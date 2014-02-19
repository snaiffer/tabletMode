#!/usr/bin/env python

import subprocess
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '100')
Config.write()

class tabletModeApp(App):
  __tableMode = False
  __DevNumList = [11, 12, 7, 10]
  def build(self):
    self.toggleButton = Button(text='Turn to TabletMode', color = [1,1,0,1])
    self.toggleButton.bind(on_press=self.toggle)
    return self.toggleButton

  def toggle(self, *args):
    for curDevNum in self.__DevNumList :
      subprocess.call(['xinput', 'set-int-prop', str(curDevNum), "Device Enabled", '8', str(int(self.__tableMode))])
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

if __name__ == '__main__':
  tabletModeApp().run()

