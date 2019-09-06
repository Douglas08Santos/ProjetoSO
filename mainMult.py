import os
import time
import mmap
import signal
import struct
import posix_ipc
import threading


def atualizarVariavelDeInstanciasCompartilhada():
    semaforo.acquire()
    instancias.seek(0)
    valor = struct.unpack('i', instancias.read(4))[0]
    valor -= 1
    instancias.seek(0)
    instancias.write(struct.pack('i', valor))
    semaforo.release()

def func(mR, mA, mB, i, j):
    mR.seek((i * len(mA[i]) + j) * 4)
    result = 0
    for k in range(len(mB)):
        result += mA[i][k] * mB[k][j] 
    mR.write(struct.pack('i', result))
    atualizarVariavelDeInstanciasCompartilhada()

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
                t = threading.Thread(target = func, args = (results, args[0], args[1], i, j))
                t.start()
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

instanciasMemoria = posix_ipc.SharedMemory('instancias', flags = posix_ipc.O_CREAT, mode = 0o777, size = 4)
instancias = mmap.mmap(instanciasMemoria.fd, instanciasMemoria.size)
instanciasMemoria.close_fd()
instancias.seek(0)
instancias.write(struct.pack('i', len(matrizA) * len(matrizA[0])))
semaforo = posix_ipc.Semaphore("test_sem", flags = posix_ipc.O_CREAT, mode = 0o777,  initial_value=1)

''' A multiplicação de matrizes é realizada de acordo com a seguinte condição: 
o número de colunas da 1ª matriz deve ser igual ao número de linhas da 2ª matriz. '''
tamMatrizR = len(matrizA)*len(matrizB[0])
if(len(matrizA[0]) == len(matrizB)):
    memoria = posix_ipc.SharedMemory('matrizR', flags = posix_ipc.O_CREAT, mode = 0o777, size = tamMatrizR*4)
    matrizR = mmap.mmap(memoria.fd, memoria.size)
    memoria.close_fd()
    
    start = time.time()

    # unroll([matrizA, matrizB], func, 'thre', matrizR)
    unroll([matrizA, matrizB], func, 'proc', matrizR)

    while True:
        semaforo.acquire()
        instancias.seek(0)
        valorInstancias = struct.unpack('i', instancias.read(4))[0]
        if valorInstancias == 0:
            semaforo.release()
            break;
        semaforo.release()
    end = time.time()

    print(struct.unpack('iiii', matrizR))
    print('Duração: {}'.format(end - start))

    matrizR.close()
    posix_ipc.unlink_shared_memory('matrizR')
else:
    print("Para realizar a multiplicação: #colunas de A deve ser igual ao #linhas de B",
         len(matrizA[0]), " != ", len(matrizB))
