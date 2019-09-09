import os
import time
import mmap
import signal
import struct
import posix_ipc
import threading

import os
import time
import mmap
import signal
import struct
import posix_ipc
import threading
import sys

class MultThreadProc(object):
    """docstring for matrixSumThreadProc"""
    def __init__(self, sizeInstance):
        self.memoryInstance = posix_ipc.SharedMemory('instances', 
                        flags = posix_ipc.O_CREAT, mode = 0o777, size = 4)
        self.instances = mmap.mmap(self.memoryInstance.fd, self.memoryInstance.size)
        self.memoryInstance.close_fd()
        self.instances.seek(0)
        self.instances.write(struct.pack('i', sizeInstance))
        #Semaforo
        self.sem = posix_ipc.Semaphore("test_sem", flags = posix_ipc.O_CREAT, 
            mode = 0o777, initial_value = 1)

    def refreshVariable(self):
        self.sem.acquire()
        self.instances.seek(0)
        value = struct.unpack('i', self.instances.read(4))[0]
        value -= 1
        self.instances.seek(0)
        self.instances.write(struct.pack('i', value))
        self.sem.release()

    def func(self,mR, mA, mB, i, j):
        mR.seek((i * len(mA[i]) + j) * 4)
        result = 0
        for k in range(len(mB)):
            result += int(mA[i][k]) * int(mB[k][j]) 
        mR.write(struct.pack('i', result))
        self.refreshVariable()


    def unroll(self, args, func, method, results):
        if method == "proc":
            for i in range(0, len(args[0])):
                for j in range(0, len(args[1][0])):
                    pid = os.fork()
                    if pid == 0:
                        self.func(results, args[0], args[1], i, j)
                        exit(0)
        elif method == "thre":
            for i in range(0, len(args[0])):
                for j in range(0, len(args[1][0])):
                    t = threading.Thread(target = self.func, args = (results, args[0], args[1], i, j))
                    t.start()
        else:
            print("Metodo incorreto.")
            exit(1)

    def multThread(self, matrixA, matrixB):
        #verifica condição para a soma
        result = None
        check = len(matrixA[0]) == len(matrixB)
        if(check):
            sizeMatrixR = (len(matrixA)*len(matrixA[0]))*4
            memory = posix_ipc.SharedMemory('matrixR', 
                flags = posix_ipc.O_CREAT, mode = 0o777, size = sizeMatrixR)
            matrixR = mmap.mmap(memory.fd, memory.size)
            memory.close_fd()
            
           
            self.unroll([matrixA, matrixB], self.func, 'thre', matrixR)
            while True:
                self.sem.acquire()
                self.instances.seek(0)
                valueInstances = struct.unpack('i', self.instances.read(4))[0]
                if valueInstances == 0:
                    self.sem.release()
                    break
                self.sem.release()
          
            size = 'i'*(int(sizeMatrixR / 4))
            result = list(struct.unpack(size, matrixR))
            

            matrixR.close()
            posix_ipc.unlink_shared_memory('matrixR')
            
        else:
            print("Para realizar a multiplicação: #colunas de A deve ser igual ao #linhas de B",
                     len(matrizA[0]), " != ", len(matrizB))
        posix_ipc.unlink_shared_memory('instances')
        posix_ipc.unlink_shared_memory('sem.test_sem')
        return result

    def multProc(self, matrixA, matrixB):
        #verifica condição para a soma
        result = None
        checkRow = len(matrixA) == len(matrixB)
        checkCol = len(matrixA[0]) == len(matrixB[0])
        if(checkRow and checkCol):
            sizeMatrixR = (len(matrixA)*len(matrixA[0]))*4
            memory = posix_ipc.SharedMemory('matrixR', 
                flags = posix_ipc.O_CREAT, mode = 0o777, size = sizeMatrixR)
            matrixR = mmap.mmap(memory.fd, memory.size)
            memory.close_fd()
            
           
            self.unroll([matrixA, matrixB], self.func, 'proc', matrixR)
            while True:
                self.sem.acquire()
                self.instances.seek(0)
                valueInstances = struct.unpack('i', self.instances.read(4))[0]
                if valueInstances == 0:
                    self.sem.release()
                    break
                self.sem.release()
          
            size = 'i'*(int(sizeMatrixR / 4))
            result = list(struct.unpack(size, matrixR))

            matrixR.close()
            posix_ipc.unlink_shared_memory('matrixR')
            
        else:
            print("Para realizar a multiplicação: #colunas de A deve ser igual ao #linhas de B",
                     len(matrizA[0]), " != ", len(matrizB))
        posix_ipc.unlink_shared_memory('instances')
        posix_ipc.unlink_shared_memory('sem.test_sem')
        return result
matrizA = [
    [1, 2],
    [3, 4]
]

matrizB = [
    [1, 2],
    [3, 4]
]

#teste = SumThreadProc(len(matrizA)*len(matrizA[0]))
#teste.sumThread(matrizA, matrizB)
teste = MultThreadProc(len(matrizA)*len(matrizA[0]))
teste.multThread(matrizA, matrizB)
teste = MultThreadProc(len(matrizA)*len(matrizA[0]))
teste.multProc(matrizA, matrizB)



'''

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
    result = 0
    for k in range(len(mB)):
        result += mA[i][k] * mB[k][j] 
    mR.write(struct.pack('i', result))
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

 A multiplicação de matrizes é realizada de acordo com a seguinte condição: 
o número de colunas da 1ª matriz deve ser igual ao número de linhas da 2ª matriz. 
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

'''