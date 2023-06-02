from produto import Produto

class Livro(Produto):
    def __init__(self, nomeloja, preco, autor):
        super().__init__(nomeloja, preco)
        self._autor = autor

    def get_autor(self):
        return self._autor

    def set_autor(self, autor):
        self._autor = autor

    def get_descricao(self):
        return super().get_descricao() + f", {self._autor}"