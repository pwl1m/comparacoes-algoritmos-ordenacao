class Classe:
    # def mergesort(lista):
    # precisamos dividir essa lista em outras listas menores(sub-listas)
    # guardando as posicoes de inicio, de fim e de meio

    def mergesort(lista, inicio=0, fim=None):#
        if fim is None: 
            fim = len(lista)
        # divide recursivamente, o array até que um sub-array possua 1 elemento.
        if fim - inicio > 1:
            meio = (fim + inicio) // 2 # dividir
            Classe.mergesort(lista, inicio, meio) # recursividade
            Classe.mergesort(lista, meio, fim) 
            Classe.merge(lista, inicio, meio, fim) # aqui vai juntar

    def merge(lista, inicio, meio, fim): 
        left = lista[inicio:meio] # lista da esquerda
        right = lista[meio:fim] # lista da direita

        i, j = 0, 0
        for k in range(inicio, fim): # k é que verifica o topo da lista
            if i >= len(left): # se o topo da lista da esquerda for maior do que o topo da lista da direita
                lista[k] = right[j] # adiciona na lista direita na posição j(direita) da lista
                j += 1 # avança a posição do topo da lista da direita
            elif j >= len(right):
                lista[k] = left[i]
                i += 1
            elif left[i] < right[j]:# se o número na posição i (esquerdo) for menor que da posição j (direito)
                lista[k] = left[i] # coloca o número na posição i (esquerdo)
                i += 1 # avança a posição do topo da lista da esquerda
            else:
                lista[k] = right[j] #adiciona o topo da lista na direita da posição a direita
                j += 1 
        return lista 

vetor_inicial = [7, 2, 5, 1, 8, 3]
print("Vetor inicial:", vetor_inicial)

Classe.mergesort(vetor_inicial)
print("Vetor resultante do Merge Sort:", vetor_inicial)