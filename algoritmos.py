class Classe:
    # def mergesort(lista):
    #precisamos dividir essa lista em outras listas menores(sub-listas), guardando as posicoes de inicio, de fim e de meio, a metade do lado esquerdo inicia na ponta esquerda e vai do inicio ao meio.
    # ja a lista do lado direito, tambem inicia do lado esquerdo(partindp do meio) e vai até o fim da lista
    # entao dai seriam 3 variaveis de indices (lista, inicio, fim)
    
    def mergesort(lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista)
        
        if fim - inicio > 1:
            meio = (fim + inicio) // 2  # // para divisão de inteiro
            Classe.mergesort(lista, inicio, meio)
            Classe.mergesort(lista, meio, fim)
            Classe.merge(lista, inicio, meio, fim)

    def merge(lista, inicio, meio, fim):  # juntando
        # criando a lista da esquerda
        # o que tiver na lista original do inicio até o meio
        left = lista[inicio:meio]
        right = lista[meio:fim]

        i, j = 0, 0  # i é o topo da esquerda, j topo da direita
        for k in range(inicio, fim):
            # aqui verifica se quem está no topo da lista da esquerda é menor do que quem está na lista da direita
            # dando prioridade para adicionar à lista o número menor
            # se o topo da esquerda (o maior)
            # for menor do que o que está no topo da direita
            # na posição k da lista (número que percorre),
            # adiciona o topo da left (o maior da esquerda)
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

        return
        
        
        
        
        
        
        
        
        
        
        
    def bubbleSort(vetor):
        qtd=len(vetor)
        for i in range(qtd):
        # laço interno ordena o ultimo elemento do vetor e entao reduz o numero de iterações
            for j in range(0, (qtd-i)-1):
                if vetor[j] > vetor[j+1]:
                    aux = vetor[j]
                    vetor[j] = vetor[j+1]
                    vetor[j+1] = aux  
        return
    
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
        return
    
    def insertSort(vetor):
        qtd=len(vetor)
        for i in range(1, qtd):
            marcado = vetor[i]
            j=i-1
            while j>=0 and marcado <vetor[j]:
                vetor[j+1] = vetor[j]
                j-=1
            vetor[j+1] = marcado
        return