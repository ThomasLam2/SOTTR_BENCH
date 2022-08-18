import os
import subprocess
import time
import pyautogui
import pygetwindow as gw
import vgamepad as vg

#Connect gamepad 360
gamepad = vg.VX360Gamepad()
print("360 GAMEPAD IN")
time.sleep(1)

# change the current directory
# to specified directory
os.chdir(r"C:\Program Files (x86)\Steam\steamapps\common\Shadow of the Tomb Raider")
subprocess.Popen("SOTTR.exe") #Open the game


time.sleep(2) #Wait


#Focus on Window
win = gw.getWindowsWithTitle('Shadow of the Tomb Raider')[0]
win.activate()

time.sleep(2) #Wait

pyautogui.press('enter') #Enter through launcher

#Game Should now be ON

time.sleep(10)#Wait

def pressdown(times):
    time.sleep(0.5)
    for i in range(times):
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
        time.sleep(0.2)
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        gamepad.update()
        time.sleep(0.2)

def pressa():
    time.sleep(0.5)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

def pressstart():
    time.sleep(0.5)
    gamepad.press_button(button=vg.XUSB_BUTTON(0x0010))
    gamepad.update()
    time.sleep(0.1)
    gamepad.release_button(button=vg.XUSB_BUTTON(0x0010))
    gamepad.update()

#Go to Options
pressdown(4)
pressa()
#Go to Display and Graphics
pressdown(3)
pressa()
#Start Benchmark
pressstart()

time.sleep(20)





