import threading
import multiprocessing

def func(var1, var2):
    print('{}, {}'.format(var1, var2))
    res.append(var1 + var2)

def unroll(args, func, method, results):
    if method == 'proc':
        for i in args:
            multiprocessing.Process(target = func, args = (i[0], i[1])).start()
    elif method == 'thre':
        for i in args:
            threading.Thread(target = func, args = (i[0], i[1])).start()
    else:
        print('method incorreto.')
        exit(1)

matriz = [
    [1, 2],
    [3, 4]
]
res = multiprocessing.Manager().list()
unroll(matriz, func, 'thre', res)
# unroll([[0, 1], [0, 2]], func, 'proc', res)
