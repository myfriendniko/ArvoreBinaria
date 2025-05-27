class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = Node(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = Node(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    def em_ordem(self):
        self._em_ordem_recursivo(self.raiz)
        print()

    def _em_ordem_recursivo(self, no):
        if no:
            self._em_ordem_recursivo(no.esquerda)
            print(no.valor, end=' ')
            self._em_ordem_recursivo(no.direita)

if __nome__ == "__main__":
    arvore = ArvoreBinaria()
    valores = [10, 5, 15, 3, 7, 12, 18]

    for v in valores:
        arvore.inserir(v)

    print("Percurso em ordem:")
    arvore.em_ordem()
