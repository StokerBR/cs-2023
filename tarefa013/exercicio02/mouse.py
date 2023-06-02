from produto import Produto

class Mouse(Produto):
    def __init__(self, nomeloja, preco, tipo):
        super().__init__(nomeloja, preco)
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_descricao(self):
        return super().get_descricao() + f", {self._tipo}"