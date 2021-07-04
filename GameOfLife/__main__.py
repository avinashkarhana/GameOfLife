import sys
from .StartGame import StartGame
import threading
from time import sleep

if __name__ == "__main__":
    argv=[]
    if len(sys.argv)>1:
        argv+=sys.argv[1:]
    thr = threading.Thread(target=StartGame, args=argv, kwargs={})
    thr.start()
    print("Started Game of Life")
    sleep(3)
    thr.is_alive()
    while True:
        try:
            pass
        except KeyboardInterrupt:
            thr.join()
            break
    print("\nGame of Life Stopped")
