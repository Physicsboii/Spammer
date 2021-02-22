import keyboard



import pyautogui,time

time.sleep(5)
#type or paste your sentences in the words file or make a file called words.txt. 

f = open("words",'r')

for word in f:
    keyboard.write(word)
    keyboard.press_and_release("enter")


