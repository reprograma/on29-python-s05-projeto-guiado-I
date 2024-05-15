dataset = [ 
    {'ano_receita': 2022, 'mes_receita': '1', 'faturamento': 49179, 'despesas': 6295},
    {'ano_receita': 2022, 'mes_receita': '2', 'faturamento': 12018, 'despesas': 43329},
    {'ano_receita': 2022, 'mes_receita': '3', 'faturamento': 23524, 'despesas': 49376},
    {'ano_receita': 2022, 'mes_receita': '4', 'faturamento': 29615, 'despesas': 16973},
    {'ano_receita': 2022, 'mes_receita': '5', 'faturamento': 26527, 'despesas': 43742},
    {'ano_receita': 2022, 'mes_receita': '6', 'faturamento': 48400, 'despesas': 11447},
    {'ano_receita': 2022, 'mes_receita': '7', 'faturamento': 27219, 'despesas': 25593},
    {'ano_receita': 2022, 'mes_receita': '8', 'faturamento': 46787, 'despesas': 19018},
    {'ano_receita': 2022, 'mes_receita': '9', 'faturamento': 32306, 'despesas': 13522},
    {'ano_receita': 2022, 'mes_receita': '10', 'faturamento': 27106, 'despesas': 15969},
    {'ano_receita': 2022, 'mes_receita': '11', 'faturamento': 15255, 'despesas': 20105},
    {'ano_receita': 2022, 'mes_receita': '12', 'faturamento': 23864, 'despesas': 32509},
    {'ano_receita': 2023, 'mes_receita': '1', 'faturamento': 47240, 'despesas': 55776},
    {'ano_receita': 2023, 'mes_receita': '2', 'faturamento': 42771, 'despesas': 36819},
    {'ano_receita': 2023, 'mes_receita': '3', 'faturamento': 18008, 'despesas': 35853},
    {'ano_receita': 2023, 'mes_receita': '4', 'faturamento': 21857, 'despesas': 6940},
    {'ano_receita': 2023, 'mes_receita': '5', 'faturamento': 29735, 'despesas': 59626},
    {'ano_receita': 2023, 'mes_receita': '6', 'faturamento': 33704, 'despesas': 30072},
    {'ano_receita': 2023, 'mes_receita': '7', 'faturamento': 26515, 'despesas': 12129},
    {'ano_receita': 2023, 'mes_receita': '8', 'faturamento': 18149, 'despesas': 21663},
    {'ano_receita': 2023, 'mes_receita': '9', 'faturamento': 46176, 'despesas': 12564},
    {'ano_receita': 2023, 'mes_receita': '10', 'faturamento': 24649, 'despesas': 58127},
    {'ano_receita': 2023, 'mes_receita': '11', 'faturamento': 44484, 'despesas': 5304},
    {'ano_receita': 2023, 'mes_receita': '12', 'faturamento': 30840, 'despesas': 5055},
    {'ano_receita': 2024, 'mes_receita': '1', 'faturamento': 28726, 'despesas': 25133},
    {'ano_receita': 2024, 'mes_receita': '2', 'faturamento': 34962, 'despesas': 26537},
    {'ano_receita': 2024, 'mes_receita': '3', 'faturamento': 49424, 'despesas': 29649},
    {'ano_receita': 2024, 'mes_receita': '4', 'faturamento': 42698, 'despesas': 54170},
    {'ano_receita': 2024, 'mes_receita': '5', 'faturamento': 37237, 'despesas': 48453},
    {'ano_receita': 2024, 'mes_receita': '6', 'faturamento': 30665, 'despesas': 8782},
    {'ano_receita': 2024, 'mes_receita': '7', 'faturamento': 39597, 'despesas': 12261},
    {'ano_receita': 2024, 'mes_receita': '8', 'faturamento': 49326, 'despesas': 18862},
    {'ano_receita': 2024, 'mes_receita': '9', 'faturamento': 19043, 'despesas': 48517},
    {'ano_receita': 2024, 'mes_receita': '10', 'faturamento': 24464, 'despesas': 24215},
    {'ano_receita': 2024, 'mes_receita': '11', 'faturamento': 11635, 'despesas': 8190},
    {'ano_receita': 2024, 'mes_receita': '12', 'faturamento': 39303, 'despesas': 14418}
]

#função que faz o menu
def menu():
    #laço infinito para sempre fazer essa repetição
    while True:
        #imprime o texto do menu
        print("----------------- LOJINHA ----------------")
        print("           Adicionar registro - 1")
        print("      Calcular Receita do Ano - 2")
        print("Mostrar melhor e pior receita - 3")
        print("                         Sair - 0")
        print("------------------------------------------")

        #pede o código a ser escolhido no menu
        opt = input("Digite a opção desejada: ")

        #compara o código escolhido no menu
        #Se 1 executa a adição do registro
        if opt == "1":
            adicionar_registro()
        #Se 2 executa o calculo da receita do ano
        elif opt == "2":
            calcular_receita_ano()
        #Se 3 executa o calculo da receita de todos os anos
        elif opt == "3":
            mostrar_pior_melhor_receita()
        #Se 0 executa a função break que encera o programa
        elif opt == "0":
            break
        #Caso não seja nenhuma dessas ele dá um erro informando que a opção não foi valida
        else:
            print("opção inválida! por favor escolha uma opção válida!")

#função para adicionar um registro
def adicionar_registro():
    #pede o ano que vai ser adicionado
    ano = int(input("Digite o ano atual: "))
    #pede o mês que vai ser adicionado
    mes = input("Digite o mês atual: ")

    #verifica se o mês é valido
    while int(mes) <= 0 or int(mes) > 12:
        #caso o mês não seja valido informa um erro e pede novamente um mês valido
        print("mês inválido , tente um valor entre 1 e 12:")
        mes = input("Digite o mês atual: ")

    #pede o faturamento que vai ser adicionado
    faturamento = int(input("Digite o faturamento referente: "))
    #pede a despesas que vão ser adicionadas
    despesas = int(input("Digite o despesas referente: "))

    #cria um novo registro
    novo_registro = {
        "ano_receita": ano,
        "mes_receita": mes,
        "faturamento": faturamento,
        "despesas": despesas
    }

    #adiciona esse registro na tabela
    dataset.append(novo_registro)
    #informa o sucesso da operação
    print("Registro adicionado com sucesso!")

#função para calcular a receita do ano
def calcular_receita_ano():
    #pede o ano que vai ser calculado
    ano_escolhido = int(input("Digite o ano que gostaria de saber a receita: "))
    #cria uma variavel que vai acumular a receita do ano
    valor_receita_ano = 0
    #cria uma variavel para o mês de maior receita e para a menor receita (despesa)
    mes_maior_receita = ""
    mes_maior_despesa = ""
    #cria uma variavel para a maior receita e para a maior despesa
    maior_despesa_mes = 0
    maior_receita_mes = 0

    #faz um laço para todos os itens do dataset
    for dados in dataset:
        #verifica se o ano do dataset é o ano informado
        if dados.get("ano_receita") == ano_escolhido:
            #calcula a receita do mês (faturamento - despesas)
            receita_registro = dados.get("faturamento") - dados.get("despesas")
            #incrementa o valor total da receita anual
            valor_receita_ano += receita_registro

            #verifica se a receita calculada é maior que a maior receita registrada
            if receita_registro > maior_receita_mes:
                #altera a maior receita registrada
                maior_receita_mes = receita_registro
                #altera o maior mês da receita
                mes_maior_receita = dados.get("mes_receita")

            #verifica se a despesas desse mês são maiores que a maior despesas salvas
            if dados.get("despesas") > maior_despesa_mes:
                #altera a maior receita registrada
                maior_despesa_mes = dados.get("despesas")
                #altera o maior mês de despesas
                mes_maior_despesa = dados.get("mes_receita")

    #imprime as informações calculadas acima
    print(f"A receita para o ano {ano_escolhido} foi {valor_receita_ano}")
    print(f"O mês de maior receita foi {mes_maior_receita} com {maior_receita_mes}")
    print(f"O mês de maior despesa foi {mes_maior_despesa} com {maior_despesa_mes}")

#função para calcular a melhor e pior receita
def mostrar_pior_melhor_receita():
    #cria um conjunto de dados para o balanço
    dict_balanco_por_ano = {}
    #cria uma variavel para a maior e para a menor receita
    ano_maior_receita = 0
    ano_menor_receita = 0

    #faz um laço para todos os itens do dataset
    for dados in dataset:
        #calcula a receita do mês
        receita_registro = dados.get("faturamento") - dados.get("despesas")
        #pega o ano daquela receita
        ano = dados.get("ano_receita")

        #verifica se existe o ano no conjunto de dados do balanço
        if ano in dict_balanco_por_ano:
            #se existir ele soma a receita do mês com a receita total
            dict_balanco_por_ano[ano] += receita_registro
        else:
            #se não existir ele informa a receita como primeira
            dict_balanco_por_ano[ano] = receita_registro

    #pega o maior valor do balanço e informa o ano
    ano_maior_receita = max(dict_balanco_por_ano, key=dict_balanco_por_ano.get)
    #pega o menor valor de balanço e informa o ano
    ano_menor_receita = min(dict_balanco_por_ano, key=dict_balanco_por_ano.get)

    #imprime as informações calculadas acima
    print(f"O ano que teve maior receita foi {ano_maior_receita} com valor de {dict_balanco_por_ano.get(ano_maior_receita)}")
    print(f"O ano que teve menor receita foi {ano_menor_receita} com valor de {dict_balanco_por_ano.get(ano_menor_receita)}")

#chama a função do menu para entrar na repetição
menu()