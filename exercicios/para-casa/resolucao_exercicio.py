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
        print("-------- MENU --------")
        print("Digite 1 para adicionar um novo registro")
        print("Digite 2 para consultar a receita de certo ano")
        print("Digite 3 para consultar quais os anos com a pior e melhor receita")
        print("Digite 0 para sair")

        opcao = input("Insira a opção escolhida: ")

        if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "0":
            print("Opção inválida!")
            continue

        if opcao == "1":
            adicionar_registro()
        elif opcao == "2":
            consultar_receita()
        elif opcao == "3":
            melhor_pior_ano()
        elif opcao == "0":
            break


def adicionar_registro():
    ano = int(input("Insira o ano do registro: "))
    mes = input("Insira o mês do registro: ")
    lucro = int(input(f"Insira o faturamento do mês {mes} de {ano}: "))
    gasto = int(input(f"Insira as despesas do mês {mes} de {ano}: "))

    novo_registro = {
        "ano_receita": ano,
        "mes_receita": mes,
        "faturamento": lucro,
        "despesas": gasto
    }

    dataset.append(novo_registro)


def consultar_receita():
    ano = int(input("Insira o ano do qual deseja consultar a receita: "))
    receita_total = 0
    maior_lucro = 0
    maior_despesa = 0
    mes_lucrativo = ''
    mes_prejuizo = ''

    for registro in dataset:
        if ano == registro.get("ano_receita"):
            receita = registro.get("faturamento") - registro.get("despesas")
            receita_total += receita
        
            if registro.get("faturamento") >= maior_lucro:
                maior_lucro = registro.get("faturamento")
                mes_lucrativo = registro.get("mes_receita")
        
            if registro.get("despesas") >= maior_despesa:
                maior_despesa = registro.get("despesas")
                mes_prejuizo = registro.get("mes_receita") 
    
    print(f"A receita total em {ano} foi de R${receita_total:.2f}.")
    print(f"O mês mais lucrativo do ano de {ano} foi o mês {mes_lucrativo}, com um faturamento de {maior_lucro}")
    print(f"O mês com mais despesas do ano de {ano} foi o mês {mes_prejuizo}, com gastos equivalentes a {maior_despesa}")


def melhor_pior_ano():
    melhor_receita = 0
    pior_receita = 0
    anos_registrados = []
    melhor_ano = 0
    pior_ano = 0

    for registro in dataset:
        if registro.get("ano_receita") not in anos_registrados:
            anos_registrados.append(registro.get("ano_receita"))

    receitas = []

    for ano in anos_registrados:
        receita_anual = 0

        for registro in dataset:
            if registro.get("ano_receita") == ano:
                receita_anual += (registro.get("faturamento") - registro.get("despesas"))

        nova_receita = {
            "ano": ano,
            "receita" : receita_anual
        }

        receitas.append(nova_receita)

    for elemento in receitas:
        if elemento.get("receita") <= melhor_receita:
            pior_receita = elemento.get("receita")
            pior_ano = elemento.get("ano")
        elif elemento.get("receita") >= melhor_receita:
            melhor_receita = elemento.get("receita")
            melhor_ano = elemento.get("ano")
    
    print(f"O ano com a melhor receita foi {melhor_ano}, com uma receita final de R${melhor_receita:.2f}.")
    print(f"O ano com a pior receita foi {pior_ano}, com uma receita final de R${pior_receita:.2f}.")
        

menu()