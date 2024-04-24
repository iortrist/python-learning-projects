class TickTackToe():
    def __init__(self) -> None:
        pass

    def board(self, move = None):

        self.move = move()
        
        rows = [0,1,2,3]
        players = ["X", "O"]
        tile =  '[ - ]'
        # while move == None:
        for row in rows:
            if row == 0:
                print("    A    B    C")
                continue
            print(f'{row} {tile*3}')

    def move(self,move = None):

        self.move = move

        match move:
            case '1A':
                self.board('1A')
                
        
        



game = TickTackToe()
game.board()