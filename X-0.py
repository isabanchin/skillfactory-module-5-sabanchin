

M = [[' ', 1, 2, 3], [1, '-', '-', '-'], [2, '-', '-', '-'], [3, '-', '-', '-']]
a = 'X'
b = '0'
win = 0
def pr():
    for i in range(0, 4):
        print(" ".join(map(str, M[i])))
pr()
while win == 0:
    xy = input('Введите координаты '+ a +'без разделителя (XY):')
    if xy.isdigit() == True and \
            len(xy) == 2 and \
            1<=int(xy[0])<=3 and \
            1<=int(xy[1])<=3 and \
            M[int(xy[1])][int(xy[0])] == "-":
        x = int(xy[0])
        y = int(xy[1])
        M[y][x]=a
        pr()
        if M[y][1] == M[y][2] == M[y][3] == a or \
            M[1][x] and M[2][x] and M[3][x] == a or \
            M[1][1] and M[2][2] and M[3][3] == a or \
            M[1][3] and M[2][2] and M[3][1] == a:
            print('Победил '+a)
            win = 1
        a,b = b,a
    else:
        print('Неправильные координаты')


