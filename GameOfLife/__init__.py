__version__ = "0.0.0.2"
__usage__ = """
    Game of Life
    By: Avinash Karhana
    Description: A simple implementation of Conway's Game of Life
    Version: {v}
    Usage:
        python3 -m GameOfLife [options]
        Options:
            -h, --help                      :   Show this help message and exit.
            -v, --version                   :   Show version and exit.
            board_size=<int>                :   Set board size.
            show_generation_changes=<bool>  :   Show changes that are going to take 
                                                place in upcoming generation.
            clear_terminal=<bool>           :   Clear terminal before each generation.
            show_board_with_icons=<bool>    :   Show board with icons.
            stepper_mode=<bool>             :   Step through generations.
            next_gen_interval=<float>       :   Display new generation with given 
                                                seconds of interval.
            # In stepper mode, use `Enter` key to move to next generation. 
            # Use `CTRL+C` key-combination to exit in non stepper mode to exit.
            # Use 'Q' key in stepper mode to exit.
    Example:
        python3 -m GameOfLife board_size=50 show_generation_changes=False clear_terminal=True show_board_with_icons=true stepper_mode=False next_gen_interval=0.5

""".format(v=__version__)