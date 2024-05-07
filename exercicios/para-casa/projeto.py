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
    print("-----MENU LOJA-----")
    print("Adicionar novo registro - 1")
    print("Calcular receita do ano escolhido - 2")
    print("Calcular mês com melhor receita - 3")

    opt=input("Digite a opçao desejada:")
    if opt =="1":
        adicionar_registro()
    elif opt=="2":
        mostrar_receita() 
    elif opt == "3":
        calcular_mes_maior_menor_receita()
    else:
        print("Opção inválida. Por favor, digite uma opção válida.")

def adicionar_registro():
    ano = int(input("digite o ano:"))
    mes = input("digite o mês:")
    faturamento = int(input("digite o faturamento neste mês:"))
    despesas = int(input("digite os despesas desse mês:"))

    novo_registro = {
    "ano_receita": ano,
    "mes_receita": mes,
    "faturamento": faturamento,
    "despesas": despesas
    }

    dataset.append(novo_registro)
    print(dataset)

def mostrar_receita():
    ano = input("digite o ano que gostaria de saber a receita")
    valor_total = 0
    for el in dataset:
        ano_el = el.get("ano_receita")
        if ano_el == ano:
            receita = (el.get("faturamento") - el.get("despesas"))
            valor_total += receita
    print(valor_total)

def calcular_mes_maior_menor_receita():
    valor_maior_receita = 0
    valor_menor_receita = 0
    for el in dataset:
        receita = el.get("faturamento") - el.get("despesas")
        
        if receita > valor_maior_receita:
            valor_maior_receita = receita  # Atualizando a maior receita
            mes_maior = el.get("mes_receita")
            ano_maior = el.get("ano_receita")
        
        if receita < valor_menor_receita:
            valor_menor_receita = receita  # Atualizando a menor receita
            mes_menor = el.get("mes_receita")
            ano_menor = el.get("ano_receita")

    print(f"Maior receita: {valor_maior_receita} no mês {mes_maior} do ano {ano_maior}")
    print(f"Menor receita: {valor_menor_receita} no mês {mes_menor} do ano {ano_menor}")

    
menu()