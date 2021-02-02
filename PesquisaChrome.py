import pyautogui


def pesquisa(pesquisa):
    pyautogui.moveTo(241, 51, duration=1)
    pyautogui.click(241, 51); pyautogui.typewrite(f'{pesquisa}')
    pyautogui.press('enter')

pesquisa('Facebook.com')