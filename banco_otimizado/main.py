mensagem = '''

Olá, seja bem vindo ao banco.
Escolha a opção desejada:

\033[1;30m
[A] - Vincular Usuário
[C] - Cliente do Banco
[L] - Listar Contas
[S] - Sacar
[D] - Depositar
[E] - Histórico do Extrato
[Q] - Sair\033[0m

==>

'''
saque_realizado = 0
saldo = 0.00
saque_diario = 3
limite_maximo = 500.00
extrato = []
AGENCIA = "0001"
usuarios = []
contas = []
numero_conta = 1

print(mensagem)
def sacar (saldo,valor,extrato,saque_realizado):
    saque_diario = 3
    if saque_realizado >= saque_diario:
        print("\033[1;31m❌ Seu limite de saques diários acabou.\033[0m")
    elif valor > limite_maximo:
        print("\033[1;31m❌ O valor máximo de saque é R$500.\033[0m")
    else:
        saldo -= valor
        saque_realizado += 1
        extrato.append(f"Saque:\nR${valor:.2f}\n")
        print("\033[1;32m✅ Saque realizado.\033[0m")
        print(f"Saldo atual: R${saldo:.2f}")
        print(f"Você possui {saque_diario-saque_realizado} saques diários")

    return saldo,valor,extrato,saque_realizado

def depositar (saldo,valor,extrato):
    saldo += valor
    if valor > 0:
        extrato.append(f"Déposito:\nR${valor:.2f}\n")
        print(f"\033[1;32m✅ Depósito realizado.\033[0m")
        print(f"R${valor:.2f}")
    else:
        print("\033[1;31m❌ Valor inválido.\033[0m")
        
    return saldo,valor,extrato

def vincular_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ").strip()

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\033[1;31m❌ Já existe usuário com esse CPF.\033[0m")
            return usuarios

    nome = input("Nome completo: ").strip()
    data_nasc = input("Data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Endereço (logradouro, número - bairro - cidade/sigla estado): ").strip()

    usuarios.append({"nome": nome, "cpf": cpf, "data_nasc": data_nasc, "endereco": endereco})
    print("\033[1;32m✅ Usuário cadastrado com sucesso!\033[0m")

    return usuarios

def cliente_banco(agencia,numero_conta,usuarios,contas):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break

    if usuario:
        contas.append({
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print(f"\033[1;32m✅ Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}\033[0m")
        numero_conta += 1
    else:
        print("\033[1;31m❌ Usuário não encontrado. Cadastre o usuário primeiro.\033[0m")

    return contas, numero_conta


def lista_contas(contas):
    if not contas:
        print("\033[1;31m❌ Nenhuma conta cadastrada.\033[0m")
        return

    for conta in contas:
        exibir_conta = f"""
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print(exibir_conta)

    return contas

def exibir_extrato(extrato):
    print("\n=== HISTÓRICO DO EXTRATO ===")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for mov in extrato:
            print(mov,end='')

#no loop que ira ativar as funções 
while True:
    opcao = (input("Digite para continuar:")).strip().upper()

    if opcao == "A":
        usuarios = vincular_usuario(usuarios)

    elif opcao == "C":
        contas, numero_conta = cliente_banco(AGENCIA, numero_conta, usuarios, contas)

    elif opcao == "S":
        valor = float(input("Digite o valor para o saque:\nR$"))
        saldo,valor,extrato,saque_realizado = sacar(saldo,valor,extrato,saque_realizado)
    
    elif opcao == "D":
        valor = float(input("Digite o valor para o depósito:\nR$"))
        saldo,valor,extrato = depositar(saldo,valor,extrato)
    
    elif opcao == "E":
        exibir_extrato(extrato)
    
    elif opcao == "L":
        lista_contas(contas)
    
    elif opcao == "Q":
        print("✅ Saindo do sistema...")
        break

    else:
        print("❌ Opção inválida, tente novamente.")