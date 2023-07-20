def monitorar_jantar():
    anoes = []
    quantidade_comida = []

    n = int(input())  # Quantidade de linhas de entrada

    for k in range(n):
        entrada = input().split(':')

        if entrada[0] == 'ENTROU':
            nome = entrada[1].strip()
            if nome in anoes:
                print('Anao ja estava em casa.')
            else:
                anoes.append(nome)
                comida = int(input())
                print(f'{nome} entrou e gostaria de {comida}g de comida.')
                quantidade_comida.append(comida)
        elif entrada[0] == 'SAIU':
            nome = entrada[1].strip()
            if nome not in anoes:
                print(f'{nome} nao estava na casa.')
            else:
                indexANAO = anoes.index(nome)
                anoes.remove(nome)
                del quantidade_comida[indexANAO]
                print(f'{nome} saiu de casa.')
    print()
    if len(anoes) == 7:
        print('teoria da branca de neve: porque so ter um se eu posso ter sete.')
    else:
        print(f'Estao na casa {len(anoes)} anoes:')
        for anao in anoes:
            print(anao)
        print(sum(quantidade_comida))


monitorar_jantar()
