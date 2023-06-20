from algoritmos import bubbleSort, mergesort, quickSort, insertSort, selectSort, shellSort
import random
import time

def measure_time(algoritmo, vetor): # Função para medir o tempo de execução de um algoritmo
    inicio = time.time() # Inicia a contagem do tempo
    algoritmo(vetor) 
    fim = time.time() # Finaliza a contagem do tempo
    tempo = fim - inicio 
    time.sleep(0.001)  # Adicione uma pequena pausa de 1 milissegundo para evitar que o tempo seja 0
    return tempo

if __name__ == "__main__":
    algoritmos = {
        "Quick Sort": quickSort,
        "Merge Sort": mergesort,
        "Insert Sort": insertSort,
        "Shell Sort": shellSort,
        "Select Sort": selectSort,
        "Bubble Sort": bubbleSort
    }
    vetor_desordenado_10000 = [random.randint(1, 5000) for _ in range(10000)]
    vetor_desordenado_25000 = [random.randint(1, 5000) for _ in range(25000)]
    vetor_desordenado_50000 = [random.randint(1, 5000) for _ in range(50000)]
    vetor_ordenado_10000 = sorted(vetor_desordenado_10000)
    vetor_ordenado_25000 = sorted(vetor_desordenado_25000)
    vetor_ordenado_50000 = sorted(vetor_desordenado_50000)
    
    for nome, algoritmo in algoritmos.items(): # Percorre o dicionário de algoritmos
        print(nome)
        tempo_desordenado_10000 = measure_time(algoritmo, vetor_desordenado_10000)
        tempo_desordenado_25000 = measure_time(algoritmo, vetor_desordenado_25000)
        tempo_desordenado_50000 = measure_time(algoritmo, vetor_desordenado_50000)
        tempo_ordenado_10000 = measure_time(algoritmo, vetor_ordenado_10000)
        tempo_ordenado_25000 = measure_time(algoritmo, vetor_ordenado_25000)
        tempo_ordenado_50000 = measure_time(algoritmo, vetor_ordenado_50000)
        print("Tempo para ordenar vetor DESordenado (10k):", tempo_desordenado_10000)
        print("Tempo para ordenar vetor DESordenado (25k):", tempo_desordenado_25000)
        print("Tempo para ordenar vetor DESordenado (50k):", tempo_desordenado_50000)
        print("Tempo para ordenar vetor ORdenado    (10k):", tempo_ordenado_10000)
        print("Tempo para ordenar vetor ORdenado    (25k):", tempo_ordenado_25000)
        print("Tempo para ordenar vetor ORdenado    (50k):", tempo_ordenado_50000)
        print("#############################################")