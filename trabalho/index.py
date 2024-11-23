import re

CONTAS = [
    {'cpfCliente': '111.111.111-22',
        'numeroConta': '2020-9', 'saldo': 5000},  # POSIÇÃO 0
    {'cpfCliente': '222.222.222-90',
        'numeroConta': '3030-8', 'saldo': 2000}  # posicção 1
]

PESSOAS = []

# -------------------------------------------------


class Pessoa():

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def infoCliente(self):
        return f"O nome do cliente é {self.nome} - CPF: {self.cpf}"

    def pegarCpf(self):
        return self.cpf

    def pegarNome(self):
        return self.nome
# -------------------------------------------------

# DEFINIÇÃO DA CLASSE CONTA PAI


class Conta:

    def __init__(self, nomeCliente, cpfCliente, numeroConta):

        self.nomeCliente = nomeCliente
        self.cpfCliente = cpfCliente
        self.saldo = 0.0
        self.numeroConta = numeroConta

    def infoConta(self):
        pass

    def abrirConta(self):
        pass

    def depositar(self):
        pass

    def sacar(self):
        pass

    def fecharConta(self):
        pass

# ----------------------------------------------------------------------------------------------------------------------- 7
# DEFINIÇÃO DE CLASSE CONTA CORRENTE


class ContaCorrente(Conta):

    def __init__(self, nomeCliente, cpfCliente, numeroConta):
        super().__init__(nomeCliente, cpfCliente, numeroConta)
        self.codigoConta = 'Corrente'
        self.limiteChequeEspecial = 500

    def abrirConta(self, pessoa):
        CONTAS.append({"cpfCliente": pessoa.pegarCpf(),
                       "numeroConta": self.numeroConta,
                       "saldo": self.saldo,
                       "tipoConta": "Corrente",
                       "chequeEspecial": self.limiteChequeEspecial
                       })

    def infoConta(self):
        return f"""O nome do cliente é {self.nomeCliente}
                CPF: {self.cpfCliente}
                CONTA: {self.numeroConta}
                TIPO DA CONTA: {self.codigoConta}
                LIMITE DE CHEQUE: {self.limiteChequeEspecial}
            """

    def depositar(self, valor, cpf):
        indiceEncontrado = -1
        saldoAtual = 0
        for i in range(len(CONTAS)):
            if CONTAS[i]["cpfCliente"] == cpf:
                indiceEncontrado = i
                saldoAtual = CONTAS[i]['saldo']
                break

        if (indiceEncontrado == -1):
            print('CPF não encontrado')
            return
        CONTAS[indiceEncontrado]["saldo"] = saldoAtual + valor

    def sacar(self, valor, cpf):
        indiceEncontrado = -1
        saldoAtual = 0
        for i in range(len(CONTAS)):
            if CONTAS[i]["cpfCliente"] == cpf:
                indiceEncontrado = i
                saldoAtual = CONTAS[i]['saldo']
                break

        if (indiceEncontrado == -1):
            print('CPF não encontrado')
            return
        if (saldoAtual + self.limiteChequeEspecial < valor):
            print('Saldo insuficiente!')
            return

        CONTAS[indiceEncontrado]["saldo"] = saldoAtual - valor

    def fecharConta(self, cpf):
        indiceEncontrado = -1
        for i in range(len(CONTAS)):
            if CONTAS[i]["cpfCliente"] == cpf:
                indiceEncontrado = i
                break

        if (indiceEncontrado == -1):
            print('Não encontramos a conta correspondente a esse CPF')
            return

        del CONTAS[indiceEncontrado]

# ----------------------------------------------------------------------------------------------------------------------- 7
# DEFINIÇÃO DE CLASSE CONTA POUPANÇA


class ContaPoupanca(Conta):

    JUROS_MENSAL = 0.5

    def __init__(self, nomeCliente, cpfCliente, numeroConta):
        super().__init__(nomeCliente, cpfCliente, numeroConta)
        self.codigoConta = 'Poupança'
        self.jurosMensal = ContaPoupanca.JUROS_MENSAL

    def abrirConta(self, pessoa):
        CONTAS.append({"cpfCliente": pessoa.pegarCpf(),
                       "numeroConta": self.numeroConta,
                       "saldo": self.saldo,
                       "tipoConta": "Poupança",
                       "jurosMensal": self.jurosMensal
                       })

    def infoConta(self):
        return f"""O nome do cliente é {self.nomeCliente}
                CPF: {self.cpfCliente}
                CONTA: {self.numeroConta}
                TIPO DA CONTA: {self.codigoConta}
                RENDIMENTO MENSAL DA CONTA: {self.jurosMensal}
            """
        # SALDO COM RENTABILIDADE DE 0.5% AO MÊS: {((self.jurosMensal / 100) * self.saldo) + self.saldo}

    def depositar(self, valor, cpf):
        indiceEncontrado = -1
        saldoAtual = 0
        for i in range(len(CONTAS)):
            if CONTAS[i]["cpfCliente"] == cpf:
                indiceEncontrado = i
                saldoAtual = CONTAS[i]['saldo']
                break

        if (indiceEncontrado == -1):
            print('CPF não encontrado')
            return
        CONTAS[indiceEncontrado]["saldo"] = saldoAtual + valor

    def sacar(self, valor, cpf):
        indiceEncontrado = -1
        saldoAtual = 0
        for i in range(len(CONTAS)):
            if CONTAS[i]["cpfCliente"] == cpf:
                indiceEncontrado = i
                saldoAtual = CONTAS[i]['saldo']
                break

        if (indiceEncontrado == -1):
            print('CPF não encontrado')
            return
        if (saldoAtual < valor):
            print('Saldo insuficiente!')
            return

        CONTAS[indiceEncontrado]["saldo"] = saldoAtual - valor

    def fecharConta(self, cpf):
        indiceEncontrado = -1
        for i in range(len(CONTAS)):
            if CONTAS[i]["cpfCliente"] == cpf:
                indiceEncontrado = i
                break

        if (indiceEncontrado == -1):
            print('Não encontramos a conta correspondente a esse CPF')
            return

        del CONTAS[indiceEncontrado]

    def calcularRendimento(self, cpf):
        indiceEncontrado = -1
        for i in range(len(CONTAS)):
            if CONTAS[i]["cpfCliente"] == cpf:
                indiceEncontrado = i
                break

        if indiceEncontrado == -1:
            print('Não encontramos a conta correspondente a esse CPF')
            return

        saldoAtual = CONTAS[indiceEncontrado]['saldo']
        rendimento = (self.jurosMensal / 100) * saldoAtual
        saldoComRendimento = saldoAtual + rendimento

        return saldoComRendimento


# pessoa = Pessoa("Kaike Fernandes", "122.122.122-12")
# print(pessoa.infoCliente())
# conta = Conta(pessoa.pegarNome(), pessoa.pegarCpf(), "00001-2", "013")
# print(conta.infoConta())
# pessoa2 = Pessoa("Dioguinho", "122.122.122-12")
# conta2 = Conta(pessoa2.pegarNome(), pessoa2.pegarCpf(), 13, '013')
# conta2.abrirConta(pessoa2)
#  ------------------------------- INSERINDO INFORMAÇÕES COM INPUT -------------------------------


def validar_cpf(cpf):
    """Verifica se o CPF está no formato correto xxx.xxx.xxx-xx."""
    return bool(re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf))


print("Insira suas informações: ")
nome = input("Nome: ")
cpf = input("Insira seu CPF (xxx.xxx.xxx-xx): ")

while not validar_cpf(cpf):
    print("CPF inválido! Por favor, insira no formato xxx.xxx.xxx-xx.")
    cpf = input("Insira seu CPF (xxx.xxx.xxx-xx): ")

x = True
while x:
    print("\nCriar uma conta: ")
    print("1 - Conta Corrente")
    print("2 - Conta Poupança")
    tipo_conta = int(input("Digite o tipo da conta desejado: "))

    if tipo_conta in [1, 2]:
        if tipo_conta == 1:
            novaconta = ContaCorrente(nome, cpf, '9999-5')
        elif tipo_conta == 2:
            novaconta = ContaPoupanca(nome, cpf, '5555-7')
        x = False
    else:
        print('Escolha um valor válido!')

print("\nFazer depósito: ")
valor = float(input("Qual o valor a ser depositado: "))

# Criar a pessoa e abrir a conta
pessoa_teste = Pessoa(nome, cpf)
novaconta.abrirConta(pessoa_teste)
novaconta.depositar(valor, cpf)

# Verificar se a conta é poupança antes de calcular o rendimento
if isinstance(novaconta, ContaPoupanca):
    saldo_com_rendimento = novaconta.calcularRendimento(cpf)
    print(f"Saldo com rendimento: R$ {saldo_com_rendimento:.2f}")
else:
    print(f"Saldo atual: R$ {valor:.2f}")

# Exibir todas as contas e seus saldos
print("\nInformações das contas:")
for conta in CONTAS:
    print(conta)

# Realizar um saque
print("\nFazer saque:")
valor_saque = float(input("Qual o valor a ser retirado: "))
novaconta.sacar(valor_saque, cpf)

# Exibir o saldo após o saque
print("\nInformações das contas após o saque:")
for conta in CONTAS:
    print(conta)


# pprint("\n")

# pprint.pprint(CONTAS)
# pprint.pprint(CONTAS, indent=4)


# Etapa 3 - Herança e Tipos de Conta:
# Criar subclasses que herdam de Conta, como:
# ContaCorrente: com limites de cheque especial.
# ContaPoupanca: com rendimentos sobre o saldo.
# Implementar métodos específicos para cada tipo de conta, como calcular juros na
# ContaPoupanca e verificação do cheque especial para sacar
