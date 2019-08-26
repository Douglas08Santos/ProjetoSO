import threading

def func(mR, mA, mB, i, j):
    # print('[{}][{}] = {}, {}'.format(i,j, mA[i][j], mB[i][j]))
    mR[i][j] = mA[i][j] + mB[i][j]

def unroll(args, func, method, results):
    if method == 'proc':
        for i in args:
            print('...')
            # multiprocessing.Process(target = func, args = (i[0], i[1])).start()
    elif method == 'thre':
        for i in range(len(args[0][0])):
            for j in range(len(args[0][1])):
                threading.Thread(target = func, args = (results, args[0], args[1], i, j)).start()
    else:
        print('method incorreto.')
        exit(1)

matrizA = [
    [1, 2],
    [3, 4]
]

matrizB = [
    [1, 2],
    [3, 4]
]

matrixR = [[0,0],[0,0]]
unroll([matrizA, matrizB], func, 'thre', matrixR)
# unroll([[0, 1], [0, 2]], func, 'proc', res)

print(matrixR)
