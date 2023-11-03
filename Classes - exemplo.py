class computador:
    def __init__(self, nome, memoria_ram, hd, cpu, gpu):
        self.nome = nome
        self.memoria_ram = memoria_ram
        self.hd = hd
        self.cpu = cpu
        self.gpu = gpu

    def ligar(self):
        print('Computador iniciando!')

    def desligar(self):
        print('Computador desligando!')

    def informacao(self):
        print(f'Nome do computador: {self.nome}. Memoria ram: {self.memoria_ram}. HD: {self.hd}. CPU: {self.cpu}. GPU: {self.gpu}')

computador1 = computador('Not', '16 gb', '1 tb', 'intel i7', 'GTX 1050')

computador1.ligar()
computador1.informacao()
computador1.desligar()
