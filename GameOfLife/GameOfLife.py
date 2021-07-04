from random import randrange

class GameOfLife:
    def __init__(self,size=50):
        super().__init__()
        self.board=[]
        self.size=size
    
    def initialize(self):
        for i in range(self.size):
            self.board.append([])
            one_num=0
            for j in range(self.size):
                temp = randrange(0, 2)
                if temp==1 and one_num>(self.size*(0.45)):
                    temp=0
                else:
                    one_num+=1
                self.board[i].append(temp)

    def currentState(self):
        return self.board
    
    def clearTerminal(self):
        print('\033c\033[3J')

    def printBoard(self, dead_cell_icon="⬜️", live_cell_icon="⬛️", changing_Cell={"tolive":[],"todead_under":[],"todead_over":[]}, clear_screen=True):
        if clear_screen: 
            self.clearTerminal()
            print("Game of Life\nStatus:Running\n")
        else:
            print("\nChanging Tiles:")
        for row in range(len(self.board)):
            s=""
            for col in range(len(self.board[row])):
                dead_cell=dead_cell_icon
                live_cell=live_cell_icon
                if self.board[row][col]==0:
                    if (row,col) in changing_Cell['todead_under']:
                        dead_cell="💀"
                    if (row,col) in changing_Cell['todead_over']:
                        dead_cell="💣"
                    s+=dead_cell
                else:
                    if (row,col) in changing_Cell['tolive']:
                        live_cell="🌕"
                    s+=live_cell
            print(s)

    def nextStep(self, show_changing=False):
        new_changed_board=self.board
        changing_Cell={"tolive":[],"todead_under":[],"todead_over":[]}
        log=""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                #Checking Number of Live Neighbor
                TotalNeighbor = 0
                
                #top left
                if (not (i-1<0)) and (not (j-1<0)):
                    if self.board[i-1][j-1]==1:
                        TotalNeighbor+=1
                #top center
                if (not (i-1<0)):
                    if self.board[i-1][j]==1:
                        TotalNeighbor+=1
                #top right
                if (not (i-1<0)) and (not (j+1>=len(self.board[i]))):
                    if self.board[i-1][j+1]==1:
                        TotalNeighbor+=1
                #mid left
                if (not (j-1<0)):
                    if self.board[i][j-1]==1:
                        TotalNeighbor+=1
                #mid center (Self)
                #if self.board[i][j]==1:
                #    TotalNeighbor+=1
                #mid right
                if (not (j+1>=len(self.board[i]))):
                    if self.board[i][j+1]==1:
                        TotalNeighbor+=1
                #lower left
                if (not (i+1>=len(self.board))) and (not (j-1<0)):
                    if self.board[i+1][j-1]==1:
                        TotalNeighbor+=1
                #lower center
                if (not (i+1>=len(self.board))):
                    if self.board[i+1][j]==1:
                        TotalNeighbor+=1
                #lower right
                if (not (i+1>=len(self.board))) and (not (j+1>=len(self.board[i]))):
                    if self.board[i+1][j+1]==1:
                        TotalNeighbor+=1
                
                #Rule1 Any live cell with fewer than two live neighbor dies, as if by underpopulation.
                if TotalNeighbor<2 and self.board[i][j]==1:
                    new_changed_board[i][j]=0
                    changing_Cell['todead_under'].append((i,j))
                    log+="Killed ("+str(i+1)+", "+str(j+1)+") due to under population\n"
                #Rule2 Any live cell with two or three live neighbor lives on to the next generation.
                if (TotalNeighbor==2 or TotalNeighbor==3) and self.board[i][j]==1:
                    new_changed_board[i][j]=1
                    log+="Keeping Alive ("+str(i+1)+", "+str(j+1)+") due to 2,3 Living Neighbour\n"
                #Rule3 Any live cell with more than three live neighbor dies, as if by overpopulation.
                if TotalNeighbor>3 and self.board[i][j]==1:
                    new_changed_board[i][j]=0
                    changing_Cell['todead_over'].append((i,j))
                    log+="Killed ("+str(i+1)+", "+str(j+1)+") due to over population\n"
                #Rule4 Any dead cell with exactly three live neighbor becomes a live cell, as if by reproduction.
                if TotalNeighbor==3 and self.board[i][j]==0:
                    new_changed_board[i][j]=1
                    changing_Cell['tolive'].append((i,j))
                    log+="Reviving ("+str(i+1)+", "+str(j+1)+") due to 3 Living Neighbour\n"
        
        self.board=new_changed_board

        if show_changing:
            self.printBoard(changing_Cell=changing_Cell, clear_screen=False, live_cell_icon="🟦")
            print(log)
