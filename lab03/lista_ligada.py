from estrutura_elementar import estrutura_elementar


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList(estrutura_elementar):
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)

    def esta_vazio(self) -> bool:
        return self.inicio is None

    def remove(self, item):
        if self.inicio is None:
            return
        if self.inicio.valor == item:
            self.inicio = self.inicio.get_proximo()
            return
        aux = self.inicio
        while aux.get_proximo() is not None:
            if aux.get_proximo().valor == item:
                aux.set_proximo(aux.get_proximo().get_proximo())
                return
            aux = aux.get_proximo()

    def tamanho(self) -> int:
        count = 0
        aux = self.inicio
        while aux is not None:
            count += 1
            aux = aux.get_proximo()
        return count

    def limpa(self):
        self.inicio = None

    def procura(self, item) -> bool:
        aux = self.inicio
        while aux is not None:
            if aux.valor == item:
                return True
            aux = aux.get_proximo()
        return False

    def indice_de(self, item):
        index = 0
        aux = self.inicio
        while aux is not None:
            if aux.valor == item:
                return index
            aux = aux.get_proximo()
            index += 1
        return -1

    def recupera_indice(self, index):
        count = 0
        aux = self.inicio
        while aux is not None:
            if count == index:
                return aux.valor
            aux = aux.get_proximo()
            count += 1
        return None

