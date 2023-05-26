class Contato:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email


class Agenda:
    def __init__(self, tamanho):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos[len(self.contatos)] = contato

    def buscar_contato(self, nome=None, email=None):
        for i in range(len(self.contatos)):
            if self.contatos[i].get_nome() == nome or self.contatos[i].get_email() == email:
                return self.contatos[i]
        return None

    def excluir_contato(self, nome):
        for i in range(len(self.contatos)):
            if self.contatos[i].get_nome() == nome:
                del self.contatos[i]
                print("Contato excluído com sucesso!")
                return
        print("Contato não encontrado!")

    def listar_contatos(self):
        for i in range(len(self.contatos)):
            print("Nome: " + self.contatos[i].get_nome() + ", Email: " + self.contatos[i].get_email())