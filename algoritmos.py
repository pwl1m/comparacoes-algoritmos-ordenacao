def mergesort(lista, inicio=0, fim=None): 
    if fim is None: 
        fim = len(lista) 

    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio) 
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]

    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left):
            lista[k] = right[j]
            j += 1
        elif j >= len(right):
            lista[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]
            j += 1

        return lista


def shellSort(vetor):
    n = len(vetor)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            c = vetor[i]
            j = i
            while j >= h and vetor[j - h] > c:
                vetor[j] = vetor[j - h]
                j -= h
            vetor[j] = c
        h //= 2

def quickSort(vetor):
    if len(vetor) <= 1:
        return vetor

    pivo = vetor[len(vetor) // 2]
    menores, iguais, maiores = [], [], []

    for elemento in vetor:
        if elemento < pivo:
            menores.append(elemento)
        elif elemento > pivo:
            maiores.append(elemento)
        else:
            iguais.append(elemento)

    return quickSort(menores) + iguais + quickSort(maiores)

def bubbleSort(vetor):
        qtd=len(vetor)
        for i in range(qtd):
        # laço interno ordena o ultimo elemento do vetor e entao reduz o numero de iterações
            for j in range(0, (qtd-i)-1):
                if vetor[j] > vetor[j+1]:
                    aux = vetor[j]
                    vetor[j] = vetor[j+1]
                    vetor[j+1] = aux  
        return vetor
    
def selectSort(vetor):
        qtd=len(vetor)
        # laço externo definindo o menor número como o elemento da primeira posição
        for i in range(qtd):
            menor=i
            # laço interno comparando os itens posteriores ao indice i ate o final do vetor para definir o real menor numero
            for j in range(i+1, qtd):
                if vetor[j]<vetor[menor]:
                    menor=j
            # se o real menor valor do laço interno for diferente do valor no indice i atual, os valores são trocados e o laço i avança uma vez
            if vetor[i] != vetor[menor]:
                aux = vetor[i]
                vetor[i] = vetor[menor]
                vetor[menor] = aux
        return vetor
    
def insertSort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave