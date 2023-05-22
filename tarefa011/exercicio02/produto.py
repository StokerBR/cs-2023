class Produto:
    def __init__(self, nomeloja, preco):
        self._nomeloja = nomeloja
        self._preco = preco
        self._descricao = "Produto de informática"

    def get_nomeloja(self):
        return self._nomeloja

    def set_nomeloja(self, nomeloja):
        self._nomeloja = nomeloja

    def get_preco(self):
        return self._preco

    def set_preco(self, preco):
        self._preco = preco

    def get_descricao(self):
        return self._descricao