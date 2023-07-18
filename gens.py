###OPTIONS###

LOG_MODE = False        #If True, print the names of connected devices and the names of pressed keys to the console
EMULATE_MODE = True     #If True, emulate key combinations when pressing certain buttons on the joystick (see EMULATE)
GENS_MODE = True        #If True, run GENS and terminate the script when closing GENS
GENS_PATH = "gens.exe"  #Path to GENS, needed only when GENS_MODE is True

#On the left is a button on the joystick that calls the combination
#On the right, any key combination separated by a + sign
EMULATE = {
    "Button 4": "f5",
    "Button 5": "f8",
    "Button 8": "shift+backspace"
}

###SCRIPT###

#Needed to detect button presses, as well as new devices
from pyjoystick.sdl2 import Key, Joystick, run_event_loop

#Needed to emulate key combinations
if EMULATE_MODE:
    from pyautogui import hotkey 

if GENS_MODE:
    from subprocess import Popen    #Needed to run a new process (GENS)
    from threading import Thread    #Needed to start a new thread
    from psutil import process_iter #Needed for iterating through all processes
    from os import _exit            #Needed to stop the entire script with all threads
    from time import sleep          #Needed to wait

#Device connected
def print_add(joy):
    if LOG_MODE:
        print('Added', joy)

#Device disconnected
def print_remove(joy):
    if LOG_MODE:
        print('Removed', joy)

#State of the keys
#True if pressed, False if released
keys = {}
def key_received(key):
    keys[key] = not keys.get(key, False)
    
    #Emulate only if key was released
    if EMULATE_MODE and keys[key] == False and EMULATE.get(key, None) != None:
        hotkey(*EMULATE[key].split("+"))
    
    if LOG_MODE:
        print(key, "is ", "pressed" if keys[key] else "released")
      
#Check every second whether GENS is running. If not, shut down    
def check_for_gens():
    if not ("gens.exe" in (p.name() for p in process_iter())):
        _exit(0)
        
    sleep(1)
    Thread(target=check_for_gens).start()
        
        
#Try to run GENS and start a new thread
if GENS_MODE:
    Popen([GENS_PATH])
    Thread(target=check_for_gens).start()
    
#Detect button presses, as well as new devices in loop
run_event_loop(print_add, print_remove, key_received)