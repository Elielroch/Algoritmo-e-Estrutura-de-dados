from estrutura_elementar import estrutura_elementar


class ArrayList(estrutura_elementar):
    def __init__(self):
         self.list = []

    def esta_vazio(self) -> bool:
        if len(self.list)==0:
         return True
        else:
         return False

    def inserir(self, item):
        self.list.append(item)

    def remove(self, item):
        if item in self.list:
            self.list.remove(item)

    def tamanho(self) -> int:
        return len(self.list)

    def limpa(self):
         self.list = []

    def procura(self, item) -> bool:
        return item in self.list

    def indice_de(self, item):
         if item in self.list:
            return self.list.index(item)
         else:
            return -1

    def recupera_indice(self, index):
        if 0 <= index < len(self.list):
            return self.list[index]
        return None
