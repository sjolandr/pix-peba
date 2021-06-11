from xmlrpc.server import SimpleXMLRPCServer

print("Esperando requisições...")
server = SimpleXMLRPCServer(("localhost", 9000))
item = None
conta = None
id = None

# [id, Nome, Banco, Número da Conta Bancária, Número da Agência, Número do Cartão de Crédito, PIN, Valor da Conta, message de aviso]
clientes = [[1, "João", "Santander", 1245, 210, 12345, 111, 750],
            [2, "Maria", "Nubank", 1241, 130, 54321, 222, 750],
            [3, "José", "Itau", 123, 123, 123, 123, 0]]

def message(banco, conta, agencia, pin):

    for item in clientes:
        if item[2] == banco and item[3] == conta and item[4] == agencia and item[6] == pin:
            return "Bem-vindo!"


def balance(op):

        if op == 3:
            for info in clientes:
                saldo = "\nSaldo: " +str (info[7]) + "\n"
            return saldo   
        else:
            print("Ops! Falha no sistema. Tente novamente mais tarde.\n")

def check(banco, conta, agencia, pin):
    global id

    for item in clientes:
        if item[2] == banco and item[3] == conta and item[4] == agencia and item[6] == pin:
            print("Conta reconhecida.")
            id = item[0]
            return 1    
    return 0
            
def transaction(op, banco, conta, agencia, valor):

    global id
    if op == 1 or op == 2:

        for item in clientes:

            if banco == item[2] and conta == item[3] and agencia == item[4]:

                if valor < 0:
                    if item[7] < abs(valor):
                        return "\nSaldo insuficiente."
                else:
                    item[7] += valor
                    return "\nTransação efetuada com sucesso."      
    
        if op == 1:

            for item in clientes:
                if item[2] == banco and item[3] == conta and item[4] == agencia:
                    item[7] -= valor

        if op == 2:

            for item in clientes:
                if item[2] == banco and item[3] == conta and item[4] == agencia:
                    item[7] += valor
        

server.register_function(check)
server.register_function(message)
server.register_function(balance)
server.register_function(transaction)
server.serve_forever()