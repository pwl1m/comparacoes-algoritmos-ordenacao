import numpy as np

class vetorOrdenado:
  def __init__(self,n):
    self._cMax = n
    self._ultimaP = -1
    self._valores = np.empty(self._cMax, dtype=int)

  def imprime(self):
    if self._ultimaP == -1:
      print("vetor vazio")
      return -1
    else:
      for i in range(self._ultimaP+1):
        print(f'posição: {i} valor: {self._valores[i]}')
      return

  def insere(self, n):
# verifica se o vetor esta cheio
    if self._ultimaP == self._cMax:
      return-1
# percorre o vetor procurando pelo primeiro valor maior que N
    for i in range(0, self._ultimaP+1):
      if self._valores[i]>n:
# apos encontrar o primeiro vaor maior que N, move todos os valores posteriores para a direita
        for y in range(self._ultimaP+1, i, -1):
          self._valores[y] = self._valores[y-1]
# insere N no espaço onde estava o primeiro valor maior que N e aumenta a ultima posição valida, apos isso retorna para parar o laço
        self._ultimaP+=1
        self._valores[i] = n
        return
# se o vetor estiver vazio o valor é inserido na primeira posição disponivel (0)
    self._ultimaP+=1
    self._valores[self._ultimaP] = n
    return
  
  def insereOrdenado(valores):
    vetor = vetorOrdenado(len(valores))
    for i in range(len(valores)):
      vetor.insere(valores[i])

  def exclui(self, n):
    for i in range (self._ultimaP):
      if n==self._valores[i]:
        for y in range (i, self._ultimaP):
          self._valores[y] = self._valores[y+1]
        self._ultimaP-=1
        return "c"
    return-1
  
  def pesquisaSimples(self,n):
    for i in range(self._ultimaP+1):
      if n == self._valores[i]:
        return i
    return -1

  def pesquisaBinaria (self, n) :
    limite_inferior = 0
    limite_superior = self._ultimaP
    while True :
      posicao_atual = int (( limite_inferior +limite_superior ) / 2)
      if self._valores [ posicao_atual ] == n:
        return posicao_atual
      elif limite_inferior > limite_superior :
        return -1
      else :
        if self._valores [ posicao_atual ] < n :
          limite_inferior = posicao_atual + 1
        else :
          limite_superior = posicao_atual - 1