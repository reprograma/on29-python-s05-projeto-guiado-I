dataset = [ {'ano_receita': 2022, 'mes_receita': '1', 'faturamento': 49179, 'despesas': 6295},
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
{'ano_receita': 2024, 'mes_receita': '12', 'faturamento': 39303, 'despesas': 14418}]



def novo_registro():
    ano = int(input("Digite o ano da receita: "))
    mes = int(input("Digite o mês da receita: "))
    faturamento = int(input("Digite o faturamento da receita: "))
    despesas = int(input("Digite as despesas da receita: "))
    
    dataset.append({
        "ano": ano, 
        "mes": mes, 
        "faturamento": faturamento, 
        "despesas": despesas 
        }) 
    
    print("Receita adicionada com sucesso!")

def calcular_receita():
    receita_total = 0
    receita_mensal_maior = 0
    receita_mensal_menor = 0

    ano_input = int(input("Digite o ano desejado para o cálculo da receita: "))
    
    for item in dataset:
        ano = item.get("ano_receita")
        receita = item.get("faturamento") - item.get("despesas")

        if ano_input == ano:
            receita_total += receita
       
        if receita > receita_mensal_maior:
            receita = receita_mensal_maior
            mes_receita_maior = item.get("mes_receita")
        
        if receita < receita_mensal_menor:
            receita = receita_mensal_menor
            mes_receita_menor = item.get("mes_receita")

    print("A receita total do ano", ano_input, "é de", receita_total)
    print("O mês", mes_receita_maior, "foi o mês com maior faturamento deste ano.")
    print("O mês", mes_receita_menor, "foi o mês com maior despesa deste ano.")

def ranking():
    ano_2022 = 2022
    ano_2023 = 2023
    ano_2024 = 2024
    receita_2022 = 0
    receita_2023 = 0
    receita_2024 = 0
    receita_anual_maior = 0
    receita_anual_menor = 0


    for item in dataset:
        ano = item.get("ano_receita")
        receita = item.get("faturamento") - item.get("despesas")
        
        if ano == ano_2022:
            receita_2022 += receita
        if ano == ano_2023:
            receita_2023 += receita
        if ano == ano_2024:
            receita_2024 += receita

    if receita_2022 > receita_2023 and receita_2022 > receita_2024:
        print("2022 foi o ano com maior receita.")
    elif receita_2023 > receita_2022 and receita_2023 > receita_2024:
        print("2023 foi o ano com maior receita.")
    else:
        print("2024 foi o ano com maior receita.")
        
    if receita_2022 < receita_2023 and receita_2022 < receita_2024:
        print("2022 foi o ano com menor receita.")
    elif receita_2023 < receita_2022 and receita_2023 < receita_2024:
        print("2023 foi o ano com menor receita.")
    else:
        print("2024 foi o ano com menor receita.")

    print("Receita de 2022:", receita_2022)
    print("Receita de 2023:", receita_2023)
    print("Receita de 2024:", receita_2024)
    
def menu():
        print("----- MENU -----")
        print("Adicionar novo registro - 1")
        print("Calcular receita - 2")
        print("Ver ranking de receitas - 3")
        print("Sair do programa - 0")
        selection = int(input("Digite a opção desejada: "))

        if selection == 1:
            novo_registro()
        elif selection == 2:
            calcular_receita()
        elif selection == 3:
            ranking()
        elif selection == 0:
            print("Programa finalizado.")
        else:
            selection = int(input("Opção inválida. Por favor, digite novamente:" ))


menu()

