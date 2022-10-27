import pyautogui
import time
message = 5
while message > 0 :
    time.sleep(5)
    pyautogui.typewrite('i love you honey, love is power, love is peace, love is happiness, love is life, love never dies.')
    time.sleep(3)
    pyautogui.press('enter')
    message = message - 1