
from pynput.keyboard import Key, Listener
import sys
 
def show(key):
 
    print('\nYou Entered {0}'.format( key))
 
    if key == Key.delete:
        # Stop listener
        sys.exit() 
# collect all event until released
with Listener(on_press = show) as listener:   
    listener.join()