from mouse import Mouse
from livro import Livro

class ProdutoInvalidoException(Exception):
    pass

class ProdutoTeste:
    def __init__(self):
        self.carrinho = []

    def adicionar_ao_carrinho(self, produto):
        if not isinstance(produto, (Mouse, Livro)):
            raise ProdutoInvalidoException("Tipo de Produto inválido")
        self.carrinho.append(produto)

    def exibir_descricao_carrinho(self):
        for produto in self.carrinho:
            print(produto.get_descricao())

produto_teste = ProdutoTeste()

try:
    produto_teste.adicionar_ao_carrinho(Mouse("Loja A", 50.0, "Mouse óptico, Saída USB. 1.600 dpi"))
    produto_teste.adicionar_ao_carrinho(Livro("Loja B", 30.0, "Autor 1"))
    
    produto_teste.adicionar_ao_carrinho("Produto inválido") # Lança ProdutoInvalidoException
    
    produto_teste.adicionar_ao_carrinho(Livro("Loja C", 40.0, "Autor 2"))
    produto_teste.adicionar_ao_carrinho(Mouse("Loja D", 25.0, "Mouse Logitech"))
    
except ProdutoInvalidoException as e:
    print(e)
    
produto_teste.exibir_descricao_carrinho()