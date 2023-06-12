import numpy as np
import time
from algoritmos import Classe
from vetor_ordenado import vetorOrdenado as v_o

def calculaTempo(algoritmo, repeticoes = 1000):
        totalTime = 0
        for i in range(repeticoes):
            #para cada repetição do laço, um vetor aleatório de 100 poisções com valores entre 0 e 999 é gerado
            start = time.time()
            vetor = np.random.randint(1000, size=100)
            algoritmo(vetor)
            totalTime += time.time() - start
        return totalTime / repeticoes
    
def criaOrdenado(repeticoes = 1000):
    totalTime = 0
    for i in range(repeticoes):
        start = time.time()
        vetor = v_o(100)
        valores = np.random.randint(1000, size=100)
        for j in range(len(valores)):
            vetor.insere(valores[j])
            totalTime+= time.time() - start
    return totalTime / repeticoes
        
if __name__ == "__main__":
    
    print("1000 vetores")
    print("100 posições")
    print("média de tempo de criação de vetor ordenado  {:.16f} segundos".format(criaOrdenado()))
    print("média de tempo de mergeSort  {:.16f} segundos".format(calculaTempo(Classe.mergesort)))
    print("média de tempo de bubbleSort {:.16f} segundos".format(calculaTempo(Classe.bubbleSort)))
    print("média de tempo de selectSort {:.16f} segundos".format(calculaTempo(Classe.selectSort)))
    print("média de tempo de insertSort {:.16f} segundos".format(calculaTempo(Classe.insertSort)))