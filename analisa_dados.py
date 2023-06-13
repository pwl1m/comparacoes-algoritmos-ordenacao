import numpy as np
import time
from vetor_ordenado import vetorOrdenado as v_o

class Analisa:
    def geraAleatorio(n):
        #vetor aleatório de N poisções com valores entre 0 e 999 é gerado
        vetor = np.random.randint(1000, size=n)
        return vetor

    def calculaTempo(algoritmo, n, repeticoes = 1000):
            totalTime = 0
            for i in range(repeticoes):
                start = time.time()
                vetor = Analisa.geraAleatorio(n)
                algoritmo(vetor)
                totalTime += time.time() - start
            return totalTime
        
    def criaOrdenado(n, repeticoes = 1000):
        totalTime = 0
        for i in range(repeticoes):
            start = time.time()
            vetor = v_o(100)
            valores = Analisa.geraAleatorio(n)
            for j in range(len(valores)):
                vetor.insere(valores[j])
                totalTime+= time.time() - start
        return totalTime / repeticoes