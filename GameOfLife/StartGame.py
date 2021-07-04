from .GameOfLife import GameOfLife
from time import sleep

def StartGame(*args):
    game = GameOfLife(int(args[0]))
    game.initialize()
    show_changes_flag=False
    if len(args)>2 and args[2].lower()=="true":
        show_changes_flag=True
    while True:
            game.printBoard()
            game.nextStep(show_changing=show_changes_flag)
            if args[1].lower()=="input":
                j=input()
                if j.lower()=="q":break
            else:
                if int(args[1])>0 and int(args[1])<999999:
                    sleep(int(args[1]))
                else:
                    sleep(2)
    exit()
