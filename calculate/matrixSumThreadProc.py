import os
import time
import mmap
import signal
import struct
import posix_ipc
import threading
import sys


# atualiza a variavel de instancias compartilhada
def refreshVariable():
    semaforo.acquire()
    instancias.seek(0)
    valor = struct.unpack('i', instancias.read(4))[0]
    valor -= 1
    instancias.seek(0)
    instancias.write(struct.pack('i', valor))
    semaforo.release()

def func(mR, mA, mB, i, j):
    mR.seek((i * len(mA[i]) + j) * 4)
    mR.write(struct.pack('i', mA[i][j] + mB[i][j]))
    refreshVariable()
    

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

#main 
if(len(matrizA) == len(matrizB) and len(matrizA[0]) == len(matrizB[0])):
    memoria = posix_ipc.SharedMemory('matrizR', flags = posix_ipc.O_CREAT, mode = 0o777, size = 16)
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
    print("O #linhas, ou o #colunas, entre as matrizes são diferentes",
         "Linhas: ", len(matrizA), ", ", len(matrizB),
          "Colunas: ", len(matriz[0]), ", ", len(matrizB[0]))                                                 
