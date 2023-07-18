class TPilhaDupla:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.dados = [None] * tamanho
        self.topo1 = -1
        self.topo2 = tamanho

    def vazia1(self):
        return self.topo1 == -1

    def vazia2(self):
        return self.topo2 == self.tamanho

    def cheia(self):
        return self.topo1 + 1 == self.topo2

    def empilhar1(self, item):
        if self.cheia():
            print("Erro: Pilha cheia")
        else:
            self.topo1 += 1
            self.dados[self.topo1] = item

    def empilhar2(self, item):
        if self.cheia():
            print("Erro: Pilha cheia")
        else:
            self.topo2 -= 1
            self.dados[self.topo2] = item

    def desempilhar1(self):
        if self.vazia1():
            print("Erro: Pilha 1 vazia")
        else:
            item = self.dados[self.topo1]
            self.topo1 -= 1
            return item

    def desempilhar2(self):
        if self.vazia2():
            print("Erro: Pilha 2 vazia")
        else:
            item = self.dados[self.topo2]
            self.topo2 += 1
            return item


# Lendo a quantidade de operações
n = int(input())

# Criando a pilha dupla com tamanho 15
pilha_dupla = TPilhaDupla(15)

for c in range(n):
    # Lendo o tipo de operação
    operacao = input().strip()

    if operacao == 'E':
        # Lendo o lado e o valor para empilhar
        lado, valor = input().split()

        if lado == 'e':
            pilha_dupla.empilhar1(valor)
        else:
            pilha_dupla.empilhar2(valor)
    elif operacao == 'D':
        # Lendo o lado para desempilhar
        lado = input().strip()

        if lado == 'e':
            item = pilha_dupla.desempilhar1()
        else:
            item = pilha_dupla.desempilhar2()

        print(item)
