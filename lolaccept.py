import pyautogui as pagui
import time
import os
import sys

root_dir_path = os.path.dirname(os.path.abspath(sys.argv[0]))

# General Usage Functions

def findImage(url):
    global root_dir_path
    return pagui.locateOnScreen(root_dir_path+url, confidence=.8)

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
    accept_button = None
    while accept_button is None:
        accept_button = findImage(r'\pictures\accept\lolaccept.png')
        if clickIfExists(accept_button):
            time.sleep(10)
        else:
            time.sleep(0.5)

def checkq():
    firstpick = None
    while firstpick is None:
        firstpick = findImage(r'\pictures\accept\firstpick.png')
        if clickIfExists(accept_button):
            time.sleep(10)
        else:
            time.sleep(0.5)

def banChampion():
    dban = None
    while dban is None:
        dban = findImage(r'\pictures\draft\ban1.png')
        time.sleep(0.5)
    if ifExists(dban):
        bsearch_field = findImage(r'\pictures\draft\bansearch.png')
        if clickIfExists(bsearch_field):
            time.sleep(0.5)
            pagui.typewrite('katarina')
            # time.sleep(0.5)
            # champion_x, champion_y = getRelativeCord(385 / 1280, 165 / 720)
            # pagui.click(champion_x, champion_y)
            # time.sleep(0.5)
            submitban = findImage(r'\pictures\draft\banbutt.png')
            pagui.click(submitban)

def pickChampion():
    dpick = None
    while dpick is None:
        dpick = findImage(r'\pictures\draft\picking.png')
        time.sleep(0.5)
    if ifExists(dpick):
        psearch_field = findImage(r'\pictures\draft\search.png')
        if clickIfExists(psearch_field):
            time.sleep(0.5)
            pagui.typewrite('vi')
            submitpick = findImage(r'\pictures\draft\pickbutt.png')
            pagui.click(submitpick)
def chat():
    chat = findImage(r'\pictures\draft\chat.png')
    if clickIfExists(chat):
        pagui.typewrite('mid or feed')
        pagui.press('enter')

# Entry Point
queue()
#checkq()
banChampion()
pickChampion()
chat()
