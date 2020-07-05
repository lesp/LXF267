import explorerhat as eh
import webbrowser
from time import sleep

while True:
    if eh.touch.five.is_pressed() == True:
        print("Hailing frequencies open")
        #webbrowser.open_new_tab("https://intl.startrek.com/")
        webbrowser.open_new_tab("https://meet.jit.si/BlackpoolMakerspace28-3-20")
        sleep(0.5)

