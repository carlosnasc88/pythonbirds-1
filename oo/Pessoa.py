class Pessoa:
    def __init__(self,nome=None, idade=32):
        self.idade = idade
        self.nome = nome



    def cumprimentar(self):
        return f'Ola{id(self)}'

if __name__ == '__main__':
    p = Pessoa('Carlos')
    print(Pessoa.cumprimentar(p))
    print(id(p.nome))
    p.nome = 'Alberto'
    print(p.cumprimentar())