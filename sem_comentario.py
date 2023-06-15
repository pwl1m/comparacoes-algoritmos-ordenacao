class Classe:

    def mergesort(lista, inicio=0, fim=None):
    # pivo
        if fim is None:
            fim = len(lista)
        
        if fim - inicio > 1:
            meio = (fim + inicio) // 2  
            Classe.mergesort(lista, inicio, meio)
            Classe.mergesort(lista, meio, fim)
            Classe.merge(lista, inicio, meio, fim)

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
        h = 1
        n = len(vetor)
        while h > 0:
                for i in range(h, n):
                    c = vetor[i]
                    j = i
                    while j >= h and c < vetor[j - h]:
                        vetor[j] = vetor[j - h]
                        j = j - h
                        vetor[j] = c
                h = int(h / 2.2)
        return vetor
        
        
    def quickSort(vetor, ini=0, fim=None):
        fim = fim if fim is not None else len(vetor)
        if ini < fim:
            pp = Classe.particao(vetor, ini, fim)
            Classe.quickSort(vetor, ini, pp)
            Classe.quickSort(vetor, pp + 1, fim)
        return vetor

    def particao(vetor, ini, fim):
        pivo = vetor[fim - 1]
        for i in range(ini, fim):
            if vetor[i] <= pivo:
                vetor[i], vetor[ini] = vetor[ini], vetor[i]
                ini += 1
        return ini - 1
        
    def bubbleSort(vetor):
        qtd=len(vetor)
        for i in range(qtd):
            for j in range(0, (qtd-i)-1):
                if vetor[j] > vetor[j+1]:
                    aux = vetor[j]
                    vetor[j] = vetor[j+1]
                    vetor[j+1] = aux  
        return vetor
    
    def selectSort(vetor):
        qtd=len(vetor)
        for i in range(qtd):
            menor=i
            for j in range(i+1, qtd):
                if vetor[j]<vetor[menor]:
                    menor=j
            if vetor[i] != vetor[menor]:
                aux = vetor[i]
                vetor[i] = vetor[menor]
                vetor[menor] = aux
        return vetor
    
    def insertSort(vetor):
        qtd=len(vetor)
        for i in range(1, qtd):
            marcado = vetor[i]
            j=i-1
            while j>=0 and marcado <vetor[j]:
                vetor[j+1] = vetor[j]
                j-=1
            vetor[j+1] = marcado
        return vetor