class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def toBDColletion(self):
        return{
            'nome': self.nome,
            'preco': self.preco,
            'quantidade': self.quantidade
        }