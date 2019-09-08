import os
import time
import mmap
import signal
import struct
import posix_ipc
import threading
import sys

class SumThreadProc(object):
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
        mR.seek((i * len(mA[i]) + j)*4)
        mR.write(struct.pack('i', int(mA[i][j]) + int(mB[i][j])))
        self.refreshVariable()


    def unroll(self, args, func, method, results):
        if method == "proc":
            for i in range(0, len(args[0])):
                for j in range(0, len(args[0][0])):
                    pid = os.fork()
                    if pid == 0:
                        self.func(results, args[0], args[1], i, j)
                        exit(0)
        elif method == "thre":
            for i in range(0, len(args[0])):
                for j in range(0, len(args[0][0])):
                    t = threading.Thread(target = self.func, args = (results, args[0], args[1], i, j))
                    t.start()
        else:
            print("Metodo incorreto.")
            exit(1)

    def sumThread(self, matrixA, matrixB):
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
            
           
            self.unroll([matrixA, matrixB], self.func, 'thre', matrixR)
            while True:
                self.sem.acquire()
                self.instances.seek(0)
                valueInstances = struct.unpack('i', self.instances.read(4))[0]
                if valueInstances == 0:
                    self.sem.release()
                    break
                self.sem.release()
            #O problema que faltar está aqui
            size = 'i'*(int(sizeMatrixR / 4))
            print("mr: ", matrixR.size())
            print("size: ",len(size))
            result = list(struct.unpack(size, matrixR))
            print("ListR: ",result)
            

            matrixR.close()
            posix_ipc.unlink_shared_memory('matrixR')
            
        else:
            print("O #linhas, ou o #colunas, entre as matrizes são diferentes",
                 "Linhas: ", len(matrizA), ", ", len(matrizB),
                  "Colunas: ", len(matriz[0]), ", ", len(matrizB[0]))
        posix_ipc.unlink_shared_memory('instances')
        posix_ipc.unlink_shared_memory('sem.test_sem')
        return result

    def sumProc(self, matrixA, matrixB):
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
          
            result = list(struct.unpack('iiii', matrixR))
            #print("ListR: ",result)
            

            matrixR.close()
            posix_ipc.unlink_shared_memory('matrixR')
            
        else:
            print("O #linhas, ou o #colunas, entre as matrizes são diferentes",
                 "Linhas: ", len(matrizA), ", ", len(matrizB),
                  "Colunas: ", len(matriz[0]), ", ", len(matrizB[0]))
        posix_ipc.unlink_shared_memory('instances')
        posix_ipc.unlink_shared_memory('sem.test_sem')
        return result
'''
matrizA = [
    [1, 2],
    [3, 10]
]

matrizB = [
    [1, 2],
    [3, 15]
]

teste = SumThreadProc(len(matrizA)*len(matrizA[0]))
teste.sumThread(matrizA, matrizB)
teste = SumThreadProc(len(matrizA)*len(matrizA[0]))
teste.sumProc(matrizA, matrizB)
'''