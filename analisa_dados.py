import numpy as np
import time


class Analisa:
    vetor = None  # Variável de classe para armazenar o vetor gerado

    @classmethod
    def geraAleatorio(cls, n):
        if cls.vetor is None:  # Verifica se o vetor já foi gerado
            # Vetor aleatório de N posições com valores entre 0 e 999 é gerado
            cls.vetor = np.random.randint(1000, size=n)
        return cls.vetor

    @classmethod
    def calculaTempo(cls, algoritmo, n, repeticoes=1000):
        totalTime = 0
        for i in range(repeticoes):
            start = time.time()
            vetor = cls.geraAleatorio(n)
            algoritmo(vetor)
            totalTime += time.time() - start
        return totalTime / repeticoes

    @classmethod
    def criaOrdenado(cls, n, repeticoes=1000):
        totalTime = 0
        vetor = v_o(n)
        valores = cls.geraAleatorio(n)
        for i in range(repeticoes):
            start = time.time()
            for j in range(len(valores)):
                vetor.insere(valores[j])
            totalTime += time.time() - start
        return totalTime / repeticoes

def v_o(n):
    # Implemente a função v_o de acordo com a sua lógica
    pass
