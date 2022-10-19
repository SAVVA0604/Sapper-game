from random import randint
from pyfiglet import print_figlet
from time import sleep


class Cell:
    """Presentation of the playing field cell"""

    def __init__(self, mine=False, around_mines=0):
        self.around_mines, self.mine = around_mines, mine
        self.fl_open = False


class GamePole:
    """Presentation of the Game Pole"""

    def __init__(self, N, M):
        self.pole = None
        self.N, self.M = N, M
        self.win_lose = True

    def init(self):
        """Game Pole initialization"""
        self.pole = [[] for _ in range(self.N)]
        cnt = 0
        for i_init in range(0, self.N):
            for j_init in range(0, self.N):
                self.pole[i_init].append(Cell())

        while cnt < self.M:
            line, column = randint(0, self.N - 1), randint(0, self.N - 1)

            if self.M > self.N ** 2:
                raise Exception('The number of mines more than cells!')

            if self.pole[line][column].mine is False:
                self.pole[line][column].mine = True
                cnt += 1

    def around(self):
        """Assigns a fl_open to each cell"""

        rez_list = []
        pole = self.pole
        for i_around in range(0, self.N):
            for j_around in range(0, self.N):
                rez_list.clear()
                for i1 in range(i_around - 1, i_around + 2):
                    for j1 in range(j_around - 1, j_around + 2):
                        if all((j1 != -1, j1 != self.N + 1,             #a = [1, 2, 3]
                                i1 != -1, i1 != self.N)):               #Because a[-1] = 3
                            try:
                                rez_list.append(pole[i1][j1].mine)
                            except:
                                pass
                pole[i_around][j_around].around_mines = rez_list.count(True)

    def show(self):
        """Outputs the entire field with open/closed cells"""
        pole = self.pole
        for i_show in range(self.N):
            for j_show in range(self.N):
                if pole[i_show][j_show].fl_open is False:
                    print('#', end=' ')
                else:
                    if pole[i_show][j_show].mine is True:
                        self.win_lose = False
                    else:
                        print(pole[i_show][j_show].around_mines, end=' ')
            print()


def cls():
    """Clean Python Console"""
    print("\n" * 20)


print_figlet('SAPER GAME\n by Akora', font='slant')
sleep(2)

while True:
    print('Enter two numbers separated by a space: field size and mines count!')
    try:
        n, m = map(int, input().split())
        break
    except:
        print('You did not enter two numbers!')


pole_game = GamePole(n, m)
pole_game.init()
pole_game.around()

while True:
    pole_game.show()
    cnt_list = []
    if pole_game.win_lose is False:
        print_figlet('\nYou lose!')
        break
    else:
        for i in range(n):
            for j in range(n):
                if pole_game.pole[i][j].fl_open is True:
                    cnt_list.append(None)
        if cnt_list.count(None) == n ** 2 - m:
            print_figlet('\nYou win!')
            break

    print(f'Enter the coordinates(x, y) of the cell you want to open!\n'
          f'Also, you have already opened {cnt_list.count(None)} cells.')
    x, y = map(int, input().split())

    try:
        pole_game.pole[y-1][x-1].fl_open = True
    except IndexError:
        print('No such cell exists!')
    cls()
