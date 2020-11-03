class Pessoa:
    def __init__(self, *filhos ,  nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)



    def cumprimentar(self):
        return f'Ola{id(self)}'

if __name__ == '__main__':
    ailton = Pessoa(nome='Ailton')
    luciano = Pessoa(ailton, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(id(luciano.idade))
    for filho in luciano.filhos:
        print(filho.nome)
    print(luciano.filhos)
    luciano.sobrenome = 'Nascimento'
    del luciano.filhos
    print(luciano.__dict__)
    print(ailton.__dict__)
