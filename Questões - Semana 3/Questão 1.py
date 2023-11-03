class substancia:
    def __init__(self, nome, formula_molecular, massa_inicial, localizacao):
        self.nome = nome
        self.formula_molecular = formula_molecular
        self.massa_inicial = float(massa_inicial)
        self.localizacao = localizacao

    def usado(self, massa_usada):
        self.massa_inicial -= massa_usada
        if float(self.massa_inicial) <= 0:
            print(f'Não há mais {self.nome}.')
        else:
            print(f'Ainda restam {self.massa_inicial}g de {self.nome}.')
    def posto(self, massa_posta):
        self.massa_inicial += massa_posta
        print(f'A nova quantidade total é {self.massa_inicial}.')

HCl = substancia('Ácido clorídrico', 'HCl', '1000', 'A01')
NaOH = substancia('Hidróxido de sódio', 'NaOH', '500', 'B01')

HCl.usado(500)
HCl.usado(500)
NaOH.posto(500)

