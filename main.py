import os
import subprocess
import time
import pyautogui

import vgamepadfunc
from vgamepadfunc import vg

from pywinauto import Application
from pywinauto import findwindows

#Connect gamepad 360
gamepad = vg.VX360Gamepad()
print("360 GAMEPAD IN")
time.sleep(1)

# change the current directory
# to specified directory
os.chdir(r"C:\Program Files (x86)\Steam\steamapps\common\Shadow of the Tomb Raider")
subprocess.Popen("SOTTR.exe") #Open the game


time.sleep(2) #Wait




#win32gui.SetForegroundWindow('Shadow of the Tomb Raider')

time.sleep(2) #Wait

#Starting the app
app = Application(backend="uia")
#app.start(r"C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe")
app.connect(path=r"C:\Program Files (x86)\Steam\steamapps\common\Shadow of the Tomb Raider")

#Focus on Window
win = app.window(title_re='.*Shadow of the Tomb Raider')

pyautogui.press('enter') #Enter through launcher

#Game Should now be ON

time.sleep(15)#Wait


#Go to Options
vgamepadfunc.pressdown(5)
vgamepadfunc.pressa()
#Go to Display and Graphics
vgamepadfunc.pressdown(3)
vgamepadfunc.pressa()
#Start Benchmark
vgamepadfunc.pressstart()

#start presentmon
os.chdir(r"C:\Users\thomalam\Documents\PRESENTMON")
subprocess.Popen("SOTTR_Presentmon.bat") #Start Presentmon

#Benchmark Should be Running
time.sleep(60)

#Turn off Application
print("Shutting off Application ")
subprocess.call(["taskkill","/F","/IM","SOTTR.exe"])








