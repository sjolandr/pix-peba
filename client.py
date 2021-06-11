import xmlrpc.client as xmlrpclib

client = xmlrpclib.ServerProxy("http://localhost:9000")

while True:

    print("\nBanco: ")
    banco = str(input())
    print("Conta: ")
    conta = int(input())
    print("Agência: ")
    agencia = int(input())
    print("PIN: ")
    pin = int(input())

    auth = (client.check(banco, conta, agencia, pin))

    if auth == 1:
        print("\nConta reconhecida. Acessando...\n")
        break

    else:
        print("\nConta inválida. Tente novamente")


while True:
    print(client.message(banco, conta, agencia, pin))
    print("1 Receber\n2 Transferir\n3 Saldo\n4 Sair\n")
    operation = int(input())


    if operation == 1:
        print("\nValor: ")
        valor = int(input())
        if valor < 0:
            print("\nValor inválido. Finalizando...")
            break
        print("Banco de origem: ")
        banco = str(input())
        print("Conta de origem: ")
        conta = int(input())
        print("Agência de origem: ")
        agencia = int(input())

        print(client.transaction(operation, banco, conta, agencia, valor))
        print(client.balance(3))

    elif operation == 2:
        print("\nValor: ")
        valor = int(input())
        if valor < 0:
            print("\nApenas valores positivos! Finalizando...\n")
            break
        valor *= -1
        print("Banco de destino: ")
        banco = str(input())
        print("Conta de destino: ")
        conta = int(input())
        print("Agência de destino: ")
        agencia = int(input())

        print(client.transaction(operation, banco, conta, agencia, valor))
        print(client.balance(3))

    elif operation == 3:
        print(client.balance(operation))

    elif operation == 4:
        break

    else:
        print("Opção inválida. Digite novamente.\n")
