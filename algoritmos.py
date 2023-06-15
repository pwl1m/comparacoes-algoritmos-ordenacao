class Classe:
    # def mergesort(lista):
    # precisamos dividir essa lista em outras listas menores(sub-listas)
    # guardando as posicoes de inicio, de fim e de meio,
    # a metade do lado esquerdo inicia na ponta esquerda e vai do inicio ao meio.
    # lista do lado direito:
    # inicia do lado esquerdo(só que dessa vez partindo do meio) e vai até o fim da lista
    # então são 3 variaveis:
    # lista é onde sao armazenados
    # inicio - esta indicando a posicao a estar na esquerda
    # meio - servindo para decidir a divisao
    # fim  - sempre ordenado estar do lado direito
    def mergesort(lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista)

        if fim - inicio > 1:
            meio = (fim + inicio) // 2
            # exemplo de 9 precisa ser inteiro para ser 4 em vez de 4.5
            # comeca a andar ate o meio
            Classe.mergesort(lista, inicio, meio) 
            Classe.mergesort(lista, meio, fim)
            Classe.merge(lista, inicio, meio, fim)

    # aqui vai juntar
    def merge(lista, inicio, meio, fim):
        left = lista[inicio:meio]
        right = lista[meio:fim]

        i, j = 0, 0  # i é o topo da esquerda, j topo da direita
        for k in range(inicio, fim):
            # aqui verifica se quem está no topo da lista da esquerda é menor do que quem está na lista da direita
            # dando prioridade para adicionar à lista o número menor
            # se o topo da esquerda (o maior) for menor do que o que está no topo da direita
            # na posição k da lista (o numero analisado) adiciona o topo da left (o maior da esquerda)
            # caso contrário, adiciona na posição k da lista o que está no topo da lista da direita (o maior número)
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
        qtd=len(vetor)
        for i in range(1, qtd):
            marcado = vetor[i]
            j=i-1
            while j>=0 and marcado <vetor[j]:
                vetor[j+1] = vetor[j]
                j-=1
            vetor[j+1] = marcado
        return vetor