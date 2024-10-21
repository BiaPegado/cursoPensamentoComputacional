import hashlib

# Autentica conta e senha
def autenticar(num_conta, senha, banco):
    if banco.get(num_conta):
        if banco[num_conta][0] == criptografar(senha):
            return True
        else:
            print("Senha incorreta!")
    else:
        print("Conta não existe!")
    return False

# Criptografa senha
def criptografar(texto):
    hash_sha256 = hashlib.sha256()
    hash_sha256.update(texto.encode())
    return hash_sha256.hexdigest()

# Cria conta nova
def criar_conta(nome_usuario, senha, banco):
    num_conta = '123-00' + str(len(banco))
    banco[num_conta] = [criptografar(senha), nome_usuario, 0]
    print("Conta criada com sucesso!")
    print(f"Número da conta: {num_conta}\nNome do usuário: {nome_usuario}")

# Exclui conta
def excluir_conta(num_conta, senha, banco):
    if autenticar(num_conta, senha, banco):
        del banco[num_conta]
        print(f"Conta {num_conta} excluída com sucesso!")
    

# Faz transferência
def transferir(num_conta_origem, num_conta_destino, valor, banco):
    if  banco[num_conta_origem][2] >= valor: 
        print("Digite sua senha novamente: ")
        senha = input()
        if autenticar(num_conta_origem, senha, banco):
            if banco.get(num_conta_destino):
                banco[num_conta_origem][2] -= valor
                banco[num_conta_destino][2] += valor
                print(f"Transferência de {valor} efetuada com sucesso!")
            else:
                print("Conta destino não existe!")
    else:
        print("Saldo insuficiente!")

# Faz saque
def sacar(num_conta, valor, banco):
    if  banco[num_conta][2] >= valor: 
        print("Digite sua senha novamente: ")
        senha = input()
        if autenticar(num_conta, senha, banco):
            banco[num_conta][2] -= valor
            print(f"Saque de {valor} efetuado com sucesso!")
    else:
        print("Saldo insuficiente!")
# Deposita valor em conta
def depositar(num_conta, valor, banco):
    print("Digite sua senha novamente: ")
    senha = input()
    if autenticar(num_conta, senha, banco):
        banco[num_conta][2] += valor
        print(f"Depósito de {valor} efetuado com sucesso!")

def detalhar_conta(num_conta, banco):
    print(f'''
Número da conta: {num_conta}
Nome do usuário: {banco[num_conta][1]}
Saldo: {banco[num_conta][2]}
''')

# Banco com key = número da conta e lista contendo senha criptografada com SHA, nome do usuário e valor em conta
banco = {
    '123-000' : ['55a5e9e78207b4df8699d60886fa070079463547b095d1a05bc719bb4e6cd251', 'Juquinha', 100] # A senha é "senha123"
}

inicio = '''
Selecione uma opção:
1 - Fazer login
2 - Criar conta
3 - Sair
'''

acao_conta = '''
Selecione uma opção:
1 - Sacar
2 - Depositar
3 - Fazer Transferência
4 - Informar Saldo
5 - Sair
'''

rodando = True
while rodando:
    print(inicio)
    opcao = int(input())
    match opcao:
        case 1:
            print("Informe o número da sua conta:")
            num_conta = input()
            print("Informe a senha da sua conta:")
            senha = input()
            if autenticar(num_conta, senha, banco):
                while rodando:
                    print(acao_conta)
                    opcao = int(input())
                    match opcao:
                        case 1:
                            print("Informe o valor:")
                            valor = int(input())
                            sacar(num_conta, valor, banco)
                        case 2:
                            print("Informe o valor:")
                            valor = int(input())
                            depositar(num_conta, valor, banco)
                        case 3:
                            print("Informe o número da conta destino:")
                            num_conta_destino = input()
                            print("Informe o valor:")
                            valor = int(input())
                            transferir(num_conta, num_conta_destino, valor, banco)
                        case 4:
                            detalhar_conta(num_conta, banco)
                        case 5:
                            rodando = False
                        case _:
                            print ("Opção inválida!")
        case 2:
            print("Informe o nome do usuário:")
            nome_usuario = input()
            print("Informe a senha da conta:")
            senha = input()
            criar_conta(nome_usuario, senha, banco)
        case 3:
            rodando = False
        case _:
            print ("Opção inválida!")