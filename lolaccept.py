import pyautogui as pagui
import time
import os
import sys
import threading

root_dir_path = os.path.dirname(os.path.abspath(sys.argv[0]))

# General Usage Functions

def log(msg):
    print("[INFO] " + msg)

def error(msg):
    print("[ERROR] " + msg)

def findImage(url):
    global root_dir_path
    try:
        image = pagui.locateOnScreen(root_dir_path + url, confidence=.8)
        if image is not None:
            log("Function findImage found an image. ("+url+")")
        return image
    except:
        error("Function findImage caught an error.")
        return None

def ifExists(object):
    if object is not None:
        return True
    return False

def clickIfExists(button):
    if ifExists(button):
        pagui.click(button)
        return True
    return False

def getWindow():
    return pagui.getWindow("League of Legends")

def getRelativeCord(normalized_x, normalized_y):
    window = getWindow()
    window_x, window_y = window.positon()
    size_x, size_y = window.size()
    x = normalized_x * size_x + window_x
    y = normalized_y * size_y + window_y
    return x, y

# Main Functionality

def queue():
    log("Queue listener started.")
    while 1:
        accept_button = None
        while accept_button is None:
            accept_button = findImage(r'\pictures\accept\lolaccept.png')
            if clickIfExists(accept_button):
                time.sleep(10)
            else:
                time.sleep(0.5)

def championSelect():
    log("Champion select listener started.")
    while 1:
        chat()
        banChampion()
        pickChampion()

def chat():
    chat = findImage(r'\pictures\draft\chat.png')
    if clickIfExists(chat):
        time.sleep(0.5)
        pagui.typewrite('mid or feed')
        time.sleep(0.5)
        pagui.press('enter')
        time.sleep(10)
    else:
        time.sleep(0.5)

def banChampion():
    dban = None
    while dban is None:
        dban = findImage(r'\pictures\draft\ban1.png')
        time.sleep(0.5)
    if ifExists(dban):
        search_field = findImage(r'\pictures\draft\bansearch.png')
        if clickIfExists(search_field):
            time.sleep(0.5)
            pagui.typewrite('katarina')
            time.sleep(0.5)
            pagui.click(getRelativeCord(385 / 1280, 165 / 720))
            time.sleep(0.5)
            submitban = findImage(r'\pictures\draft\banbutt.png')
            if clickIfExists(submitban):
                time.sleep(10)
            else:
                time.sleep(0.5)

def pickChampion():
    pass

# Entry Point
if __name__ == "__main__":
    queueThread = threading.Thread(target=queue, args=())
    queueThread.start()
    championSelectThread = threading.Thread(target=championSelect, args=())
    championSelectThread.start()

    queueThread.join()
    championSelectThread.join()
