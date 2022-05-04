from random import randrange
from tabnanny import check
from time import sleep

class GameOfLife:
    def __init__(self):
        super().__init__()
        self.board = []
        self.last_board = []
        self.board_size = 50
        self.clear_terminal = True
        self.show_generation_changes = False
        self.show_board_with_icons = True
        self.header_message = "Game of Life"
        self.footer_message = ""
    
    def set_board_size(self, size):
        self.board_size = size
    
    def set_clear_terminal(self, clear):
        self.clear_terminal = clear

    def set_show_generation_changes(self, show):
        self.show_generation_changes = show

    def set_show_board_with_icons(self, show):
        self.show_board_with_icons = show

    def set_header_message(self, message):
        self.header_message = message
    
    def set_footer_message(self, message):
        self.footer_message = message

    def initialize(self):
        self.board = []
        for i in range(self.board_size):
            self.board.append([])
            for _ in range(self.board_size):
                temp = randrange(0, 2)
                self.board[i].append(temp)

    def currentState(self):
        # Return current state of the board in dictionary format
        return self.__dict__
    
    def clearTerminal(self):
        print('\033c\033[3J')

    def printBoard(self, board = None,dead = None, alive = None, standard_dead_icon = "⬛️", standard_alive_icon = "⬜️", transition_to_dead_icon = "💀", transition_to_alive_icon = "🟦"):
        if self.clear_terminal:
            self.clearTerminal()
            print(self.header_message)
        if not board:
            board = self.board
        print("🟫" * (self.board_size+4) + "\n")
        for i in range(self.board_size):
            print("    ", end = "")
            for j in range(self.board_size):
                if self.show_board_with_icons:
                    if (dead and [i,j] in dead) or (alive and [i,j] in alive):
                        dead_icon = transition_to_dead_icon
                        alive_icon = transition_to_alive_icon
                    else:
                        dead_icon = standard_dead_icon
                        alive_icon = standard_alive_icon
                else:
                    alive_icon = dead_icon = self.board[i][j]
                if board[i][j] == 0:
                    print(dead_icon, end = "")
                else:
                    print(alive_icon, end = "")
            print()
        print(self.footer_message)
    
    def getNumberOfLivingNeighbors(self, x, y):
        count = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i >= 0 and i < self.board_size and j >= 0 and j < self.board_size:
                    if i == x and j==y:
                        continue
                    else:
                        count+= 1 if self.board[i][j] == 1 else 0
        return count

    def nextStep(self):
        self.check_for_all_dead_state(self.board)

        new_board = list(map(list, self.board))
        dying_cells = []
        new_cells = []

        for i in range(self.board_size):
            for j in range(self.board_size):
                living_neighbors = self.getNumberOfLivingNeighbors(i,j)
                if new_board[i][j] == 1:
                    # death by underpopulation or overpopulation
                    if living_neighbors < 2 or living_neighbors > 3:
                        new_board[i][j] = 0
                        dying_cells.append([i,j])
                elif living_neighbors == 3:
                    # birth by reproduction
                    new_board[i][j] = 1
                    new_cells.append([i,j])
        if self.show_generation_changes:
            self.printBoard(new_board, dead = dying_cells, alive = new_cells)
        if not self.check_for_all_dead_state(new_board) and not self.check_for_stable_state(new_board) and not self.check_for_infinite_loop(new_board):
            self.last_board = list(map(list, self.board))
            self.board = new_board

    def check_for_all_dead_state(self, board):
        # Check if all cells are dead
        if not any(1 in x for x in board):
            self.printBoard(board)
            self.ask_user_to_restart_game(endMsg = "All cells are dead!")
            return True

    def check_for_infinite_loop(self, board):
        # Check if the board is same as last board
        if board == self.last_board:
            self.ask_user_to_restart_game(endMsg = "Infinite Loop Stage reached!")
            return True

    def check_for_stable_state(self, board):
        # Check if the board is same as previous board
        if board == self.board:
            self.ask_user_to_restart_game(endMsg = "Stable stage reached!")
            return True

    def ask_user_to_restart_game(self, endMsg = None):
        if endMsg:
            print("🟨"*(self.board_size+4) + "\n" + endMsg + "\n" + "🟨"*(self.board_size+4))
        print("\n"+"🟫" * (self.board_size+4) + "\n    Game of Life Ended\n" + "🟫" * (self.board_size+4))
        userInput = input("Do you want to start again? (y/n) : ")
        if userInput.lower()=="y":
            self.initialize()
            for i in range(0, 5):
                self.header_message = "Started Game of Life again!"
                self.footer_message = "Next generation will be displayed soon"
                self.footer_message += "." * (12-(4*i))
                if i == 4:
                    self.footer_message += "\nFrom now on next generation will be displayed at default set interval!"
                    self.printBoard()
                    sleep(4)
                self.printBoard()
                sleep(1)
                self.clearTerminal()
            self.header_message = "Game of Life!"
            self.footer_message = ""
            self.printBoard()
        else:
            exit()
