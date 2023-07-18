# GENS Hotkeys
A configurable script that emulates key presses when using a joystick, created specifically for the GENS emulator.<br /><br />
- By default, L1 does a quick save in GENS, and R2 does a quick load. The SELECT button takes a screenshot.<br />
- The script can be used without GENS, for simple emulation of keys. To do this, set **GENS_MODE** to **False**<br />
- To open the script without the console, change the file extension from **.py** to **.pyw**<br /><br />

Options
---
**LOG_MODE** - If True, print the names of connected devices and the names of pressed keys to the console.<br />
**EMULATE_MODE** - If True, emulate key combinations when pressing certain buttons on the joystick (see Setting Up Emulation).<br />
**GENS_MODE** - If True, run GENS and terminate the script when closing GENS.<br />
**GENS_PATH** - Path to GENS, needed only when GENS_MODE is True.<br /><br />

Setting Up Emulation
---
First you need to enable **LOG_MODE**, before that it is desirable to disable **EMULATE_MODE** and **GENS_MODE**. Then press the desired button on your joystick and copy its name displayed in the console. Then, find the **EMULATE** dictionary, which should look like this:
```python
EMULATE = {
    "Button 4": "f5",
    "Button 5": "f8",
    "Button 8": "shift+backspace"
}
```
Here, as the value on the left, use the previously copied name of the key that will emulate the keys combination, and as the value on the right any combination of keys separated by a + sign. After that, set the **EMULATE_MODE** to **True** and you're done.

Required modules
---
To work properly, you need to install these modules:<br />
```bat
pip install pyjoystick
pip install pyautogui
pip install psutil
```
