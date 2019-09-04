import os
import mmap
import signal
import struct
import posix_ipc
import threading


def func(mR, mA, mB, i, j):
    mR.seek((i * len(mA[i]) + j) * 4)
    result = 0
    for k in range(len(mB)):
        result += mA[i][k] * mB[k][j] 
    mR.write(struct.pack('i', result))

def unroll(args, func, method, results):
    if method == 'proc':
        for i in range(0, len(args[0][0])):
            for j in range(0, len(args[0][1])):
                pid = os.fork()
                if pid == 0:
                    func(results, args[0], args[1], i, j)
                    exit(0)
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
''' A multiplicação de matrizes é realizada de acordo com a seguinte condição: 
o número de colunas da 1ª matriz deve ser igual ao número de linhas da 2ª matriz. '''

if(len(matrizA[0]) == len(matrizB)):
    memoria = posix_ipc.SharedMemory('matrizR', flags = posix_ipc.O_CREAT, mode = 0o777, size = 16)
    matrizR = mmap.mmap(memoria.fd, memoria.size)
    memoria.close_fd()
    unroll([matrizA, matrizB], func, 'thre', matrizR)
    unroll([matrizA, matrizB], func, 'proc', matrizR)

    print(struct.unpack('iiii', matrizR))

    matrizR.close()
    posix_ipc.unlink_shared_memory('matrizR')
else:
    print("Para realizar a multiplicação: #colunas de A deve ser igual ao #linhas de B",
         len(matrizA[0]), " != ", len(matrizB))
