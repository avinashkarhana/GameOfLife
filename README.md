[![Build and Publish to PyPI](https://github.com/avinashkarhana/GameOfLife/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/avinashkarhana/GameOfLife/actions/workflows/publish-to-pypi.yml)

# GameDriver

A simple implementation of Conway's Game of Life.

Pythonic interface for easy imports to other projects.

    Check `GameDriver.py` for reference

## INSTALLATION:
    > pip install py-GameOfLife

## USAGE:
    python3 main.py [options]
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
    Example:
        python3 main.py board_size=50 show_generation_changes=False clear_terminal=True show_board_with_icons=true stepper_mode=False next_gen_interval=0.5
