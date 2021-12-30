class Board:
    def __init__(self, boardStr):
        self.board = [['' for i in range(5)] for j in range(5)]
        for i in range(5):
            self.board[i] = [int(STR) for STR in boardStr[i].split()]
        self.unmarkedBoard = [[True for i in range(5)] for j in range(5)]
    
    def markBoard(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                    self.unmarkedBoard[i][j] == False
                    break
    
    def checkBoard(self, number):
        for row in self.unmarkedBoard:
            if row == [False for i in range(5)]:
                return self.get
