class ContaBancaria:
    
    def __init__ (self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False


    def __str__(self):
        return f'Nome(titular): {self.titular}\nSaldo: {self.saldo}'
        
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo

conta1 = ContaBancaria('Rodolfo', 150)
conta2 = ContaBancaria('Josefa', 1060)

print (conta1)
print (conta2)

conta3 = ContaBancaria('Roberta', 180)
print(f'Antes de ativar: Conta ativa ? {conta3._ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar: Conta ativa ? {conta3._ativo}')

conta4 = ContaBancaria('Fernando', 5525)
print(f'Titular da conta 4: {conta4.titular}')

class ClienteBanco:

    def __init__(self, nome, cpf, idade, endereco, cep):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereco = endereco
        self.cep = cep

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco('Ana', '056.125.489-55', 30, 'Rua 1', '67.254-100')
cliente2 = ClienteBanco('Maria', '456.547.122-44', 18, 'Rua Onore', '78.456-100')
cliente3 = ClienteBanco('Roberio', '456.123.896-42', 52, 'Rua Franca', '15.745-100')

conta_cliente1 = ClienteBanco.criar_conta('Ana', 1000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")
