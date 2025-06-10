F = True
S = False


class Board:
    def __init__(self):
        self.main_l = [[None for _ in range(3)] for _ in range(3)]

    def print_board(self):
        '''this func prints the tic tac toe board'''
        for row in range(2, -1, -1):
            print(' ', row + 1, end='  ')
            for col in range(3):
                print(f'{'|' if col != 0 else ''} {'N' if self.main_l[row][col] is None else 'x' if self.main_l[row][col] == 1 else '0'}', end=' ')
            print('')
            if row == 0:
                continue
            print('     -----------')
        print()
        print(end='      ')
        for col in range(1, 4):
            print(col, end='   ')
        print()

    def make_move(self, c: int, r: int):
        '''first checks and then makes move'''
        if self.main_l[c - 1][r - 1] is None:
            self.main_l[c - 1][r - 1] = 1 if F else 0
            return True
        return False

    def check_move(self):
        '''this func checks all players moves'''

        for i in range(3):  # check lines
            count_f, count_s = 0, 0
            for n in range(3):
                if self.main_l[i][n] == 1:
                    count_f += 1
                elif self.main_l[i][n] == 0:
                    count_s += 1
            if count_f == 3:
                print('First player win!')
                return True
            elif count_s == 3:
                print('Second player win!')
                return True

            for i in range(3):  # check lines down
                count_f, count_s = 0, 0
                for n in range(3):
                    if self.main_l[n][i] == 1:
                        count_f += 1
                    elif self.main_l[n][i] == 0:
                        count_s += 1
                if count_f == 3:
                    print('First player win!')
                    return True
                elif count_s == 3:
                    print('Second player win!')
                    return True

            count_f, count_s = 0, 0
            for i in range(3):  # check diagonals
                if self.main_l[i][i] == 1:
                    count_f += 1
                elif self.main_l[i][i] == 0:
                    count_s += 1
                if count_f == 3:
                    print('First player win!')
                    return True
                elif count_s == 3:
                    print('Second player win!')
                    return True

            count_f, count_s = 0, 0
            for i in range(3):  # check diagonals
                if self.main_l[i][2 - i] == 1:
                    count_f += 1
                elif self.main_l[i][2 - i] == 0:
                    count_s += 1
                if count_f == 3:
                    print('First player win!')
                    return True
                elif count_s == 3:
                    print('Second player win!')
                    return True

            for i in range(3):  # checks whether players played to a draw
                for n in range(3):
                    if self.main_l[i][n] is None:
                        return False
            print('Draw!')
            return True


def check_move():
    '''checkes move'''
    while True:
        choice = input(f'{'First' if F else 'Second'} player makes choice, like(3 3): ')
        try:
            c, r = list(map(int, choice.split()))
            if 3 >= c >= 1 and 3 >= r >= 1 and b.make_move(c, r):
                print('You made a move!')
                break
            else:
                print('You type incorrect coordinates. Please, try again.')
        except:
            print('You type incorrect coordinates. Please, try again.')


if __name__ == "__main__":
    print('Hi. You are at the "tic tac toe" app. Enjoy your time.')
    b = Board()
    while True:
        b.print_board()
        print()
        check_move()
        F = not F
        S = not S
        if b.check_move():
            b.print_board()
            print('Thank you that you use our app! See you soon!')
            break
