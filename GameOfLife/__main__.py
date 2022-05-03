import sys
import threading
from time import sleep
if __package__ == "GameOfLife":
    from GameOfLife.__init__ import __usage__, __version__
    from GameOfLife.GameDriver import StartGame
else:
    from __init__ import __usage__, __version__
    from GameDriver import StartGame

argv=[]
if len(sys.argv)>1:
    argv+=sys.argv[1:]

for i in argv:
    if i in ["-h", "--help"]:
        print(__usage__)
        exit()
    if i in ["-v", "--version"]:
        print(__version__)
        exit()

thr = threading.Thread(target=StartGame, args=argv, kwargs={})
thr.start()
print("Started Game of Life")
sleep(3)
thr.is_alive()
while True:
    try:
        if not thr.is_alive():
            break
    except KeyboardInterrupt:
        thr.join()
        break
    except Exception as e:
        break
print("\nGame of Life Stopped")
