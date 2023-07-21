def verificar_assento_passageiro(num_passageiros):
    for _ in range(num_passageiros):
        possui_rg = input()
        data_rg = input()
        possui_passagem = input()
        data_passagem = input()
        assento = input()

        if possui_rg == "Nao possui":
            print("a saida e nessa direção")
        elif possui_passagem == "Nao possui":
            print("a recepição e nessa direção")
        elif data_rg != data_passagem:
            print("190")
        else:
            print("o seu assento e", assento, "tenha um bom dia")


# Entrada do usuário
num_passageiros = int(input())

# Chamada da função para verificar cada passageiro
verificar_assento_passageiro(num_passageiros)
