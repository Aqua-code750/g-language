import pyautogui

def move_mouse(x, y):
    pyautogui.moveTo(int(x), int(y))
    return 1
    
def click(button='left'):
    pyautogui.click(button=str(button))
    return 1

def type_text(text):
    pyautogui.typewrite(str(text))
    return 1

def press_key(key):
    pyautogui.press(str(key))
    return 1

def get_mouse_pos():
    x, y = pyautogui.position()
    return f"{x},{y}"
