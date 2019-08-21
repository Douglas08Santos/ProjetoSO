def func(var1, var2):
    print('{}, {}'.format(var1, var2))

def unroll(args, func, method, results):
    # TODO
    if method == 'proc':
        print('Processos...')
    elif method == 'thre':
        print('Threads...')
    else:
        print('method incorreto.')
        exit(1)

res = []
unroll([[0, 1], [0, 2]], func, 'thre', res)
unroll([[0, 1], [0, 2]], func, 'proc', res)
