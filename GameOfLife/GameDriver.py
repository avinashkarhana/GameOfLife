from time import sleep

if __package__ == "GameOfLife":
    from .GameOfLife import GameOfLife
else:
    from GameOfLife import GameOfLife

def StartGame(*args):
    # Instantiate GameOfLife object
    game = GameOfLife()

    # Set game driver to step mode
    stepper_mode = False

    # Set next generation display interval
    next_gen_interval = 0

    # Set game parameters
    for i in args:
        optKeyPair = i.split("=")
        if len(optKeyPair) != 2:
            continue
        option, value = optKeyPair
        if option == "board_size":
            game.board_size = int(value)
        elif option.lower()=="show_generation_changes" and value.lower()=="true":
            game.show_generation_changes = True
            game.clear_terminal = False
        elif option.lower()=="clear_terminal" and value.lower()=="true" and not game.show_generation_changes:
            game.clear_terminal = True
        elif option.lower()=="show_board_with_icons":
            if value.lower()=="true":
                game.show_board_with_icons = True
            if value.lower()=="false":
                game.show_board_with_icons = False
        elif option.lower()=="stepper_mode" and value.lower()=="true":
            stepper_mode = True
        elif option.lower()=="next_gen_interval":
            next_gen_interval = float(value)

    # Initialize Game
    game.initialize()
    while True:
        game.printBoard()
        game.nextStep()
        if stepper_mode:
            j=input()
            if j.lower()=="q":break
        elif next_gen_interval > 0 and next_gen_interval < 999999:
            sleep(next_gen_interval)
        else:
            sleep(2)
    return None
