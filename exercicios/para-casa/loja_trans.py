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

def menu():
    while True:
        print("------------------- LOJINHA TRANS -------------------")
        print("                 Adicionar Registro - 1")
        print("           Calcular Receita por Ano - 2")
        print("            Mostrar Balanço por Ano - 3")
        print("             Calcular Lucro por Ano - 4")
        print("                               Sair - 0")
        print("-----------------------------------------------------")

        opt = input("Digite a opção desejada: ")


        if opt == "1":
            add_registro()
        elif opt == "2":
            calcular_receita_ano()
        elif opt == "3":
            mostrar_balanco_ano()
        elif opt == "4":
            calcular_lucro_ano()
        elif opt == "0":
            break 
        else:
            print("Opção inválida! Por favor, escolha uma opção válida!")


def add_registro():
    ano = int(input("Digite o ano que deseja adicionar: "))
    mes = input("Digite o mês que deseja adicionar: ")

    while int(mes) <= 0 or int(mes) > 12:
        print("Mẽs inválido, tente um valor entre 1 e 12: ")
        mes = input("Digite o mês atual: ")

    faturamento = int(input("Digite o faturamento referente: "))
    despesas = int(input("Digite a despesa referente: "))

    novo_registro = {
        "ano": ano,
        "mes": mes,
        "faturamento": faturamento,
        "despesas": despesas        
    }

    dataset.append(novo_registro)
    print("Registro adicionado com sucesso!")


def calcular_receita_ano():
    ano_escolhido = int(input("Digite o ano que gostaria de saber a receita: "))
    valor_receita_ano = 0
    mes_maior_receita = ""
    mes_maior_despesa = ""
    maior_despesa_mes = 0
    maior_receita_mes = 0

    for dados in dataset:
        if dados.get("ano_receita") == ano_escolhido:
            receita_registro = dados.get("faturamento") - dados.get("despesas")
            valor_receita_ano += receita_registro

            if receita_registro > maior_receita_mes:
                maior_receita_mes = receita_registro
                mes_maior_receita = dados.get("mes_receita")
            
            if dados.get("despesas") > maior_despesa_mes:
                maior_despesa_mes = dados.get("despesas")
                mes_maior_despesa = dados.get("mes_receita")

    print(f"A receita para o ano {ano_escolhido} foi {valor_receita_ano}")
    print(f"O mês de maior receita foi {mes_maior_receita} com {maior_receita_mes}")
    print(f"O mês de maior despesa foi {mes_maior_despesa} com {maior_despesa_mes}")


def mostrar_balanco_ano():
    dict_balanco_por_ano = {}
    ano_maior_receita = 0
    ano_menor_receita = 0

    for dados in dataset:
        receita_registro = dados.get("faturamento") - dados.get("despesas")
        ano = dados.get("ano_receita")

        if ano in dict_balanco_por_ano:
            dict_balanco_por_ano [ano] += receita_registro
        else:
            dict_balanco_por_ano [ano] = receita_registro
    
    ano_maior_receita = max(dict_balanco_por_ano, key=dict_balanco_por_ano.get)
    ano_menor_receita = min(dict_balanco_por_ano, key=dict_balanco_por_ano.get)

    print(f"O ano que teve maior receita foi {ano_maior_receita} com o valor de {dict_balanco_por_ano.get(ano_maior_receita)}")
    print(f"O ano que teve menor receita foi {ano_menor_receita} com o valor de {dict_balanco_por_ano.get(ano_menor_receita)}")


def calcular_lucro_ano():
    ano_escolhido = int(input("Digite o ano que gostaria de saber o lucro: "))
    valor_lucro_ano = 0
    mes_maior_lucro = ""
    mes_menor_lucro = ""
    menor_lucro_mes = 0
    maior_lucro_mes = 0

    for dados in dataset:
        if dados.get("ano_receita") == ano_escolhido:
            lucro_registro = dados.get("faturamento") - dados.get("despesas")
            valor_lucro_ano += lucro_registro

            if lucro_registro > maior_lucro_mes:
                maior_lucro_mes = lucro_registro
                mes_maior_lucro = dados.get("mes_receita")

            if lucro_registro < menor_lucro_mes:
                menor_lucro_mes = lucro_registro
                mes_menor_lucro = dados.get("mes_receita")
                
    print(f"O lucro para o ano {ano_escolhido} foi {valor_lucro_ano}")
    print(f"O mês de maior lucro foi {mes_maior_lucro} com {maior_lucro_mes}")
   

menu()
