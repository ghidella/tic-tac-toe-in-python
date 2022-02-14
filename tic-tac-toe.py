import random


class Game:
    def __init__(self, player, machine):
        self.__player = player
        self.__machine = machine
        self.__positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def board(self):
        print(
            f'  {self.__positions[0]}  |  {self.__positions[1]}  |  {self.__positions[2]} \n-----------------\n  {self.__positions[3]}  |  {self.__positions[4]}  |  {self.__positions[5]} \n-----------------\n  {self.__positions[6]}  |  {self.__positions[7]}  |  {self.__positions[8]} ')

    def player(self):
        a = False
        while not a:
            player = int(input('Select your piece:\n(1) O\n(2) X\n'))
            if player == 1:
                print('You choose O')
                self.__player = 'O'
                self.__machine = 'X'
                a = True
            elif player == 2:
                print('You choose X')
                self.__player = 'X'
                self.__machine = 'O'
                a = True
            else:
                print('Invalid Option, please select again')

    def player_move(self):
        game = False
        while not game:
            position = int(input('Choose the number referring to the position to place your piece on the board\n'))
            if position not in range(1, 10):
                print('This position does not exist, please choose again')
                continue
            elif self.__positions[position - 1] == 'O' or self.__positions[position - 1] == 'X':
                print('This position is already occupied, please choose another one')
                continue
            else:
                self.__positions[position - 1] = self.__player
                break

    def machine_move(self):
        input('Machine turn, press ENTER to continue...')
        game = False
        while not game:
            position = random.randrange(1, 10)
            if self.__positions[position - 1] == 'O' or self.__positions[position - 1] == 'X':
                continue
            else:
                self.__positions[position - 1] = self.__machine
                break

    def win(self):
        if self.__positions[0] == self.__positions[1] and self.__positions[1] == self.__positions[2]:
            return True
        elif self.__positions[0] == self.__positions[4] and self.__positions[4] == self.__positions[8]:
            return True
        elif self.__positions[0] == self.__positions[3] and self.__positions[3] == self.__positions[6]:
            return True
        elif self.__positions[4] == self.__positions[1] and self.__positions[1] == self.__positions[7]:
            return True
        elif self.__positions[4] == self.__positions[2] and self.__positions[2] == self.__positions[6]:
            return True
        elif self.__positions[4] == self.__positions[3] and self.__positions[3] == self.__positions[5]:
            return True
        elif self.__positions[8] == self.__positions[5] and self.__positions[5] == self.__positions[2]:
            return True
        elif self.__positions[8] == self.__positions[7] and self.__positions[7] == self.__positions[6]:
            return True


# GAMEPLAY
print('*******************************\n*****TIC TAC TOE IN PYTHON*****\n*******************************')
game = Game('default', 'default')
game.player()
draw = 0
while not game.win():
    game.board()
    game.player_move()
    game.board()
    draw += 1
    if draw == 9:
        break
    game.machine_move()
    draw += 1
print('Game Over')
