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
        print("********** FINANCEIRO LOJA **********")
        print("\nEscolha uma das opções do menu abaixo:")
        print("1 - Para novo registro")
        print("2 - Para calcular a receita de um determinado ano")
        print("3 - Para saber quais anos tiveram a maior e a menor receita")
        print("0 - Para sair do menu")

        opcao = input("Insira a opção desejada: ")

        if opcao == "1":
            novo_registro()
        elif opcao == "2":
            receita_anual()
        elif opcao == "3":
            ano_maior_menor_receita(dataset)
        elif opcao == "0":
            print("Fim da consulta.")
            break
        else:
            print("Insira uma opção válida.")
            continue
            

def novo_registro():
    ano = int(input("Insira o ano: "))
    mes = input("Insira o mês: ")
    faturamento = int(input("Insura o faturamento: "))
    despesas = int(input("Insira as depesas: "))

    novo_registro = {
        "ano_receita": ano,
        "mes_receita": mes,
        "faturamento": faturamento,
        "despesas": despesas
    }

    dataset.append(novo_registro)

def receita_anual():
    ano = int(input("Insira o ano que deseja saber a receita: "))
    receita_total_ano = 0
    receita_maior_mensal = 0
    mes_maior_receita = 0
    despesa_maior_mensal = 0
    mes_maior_despesa = 0
    
    
    for item in dataset:
        ano_item = item.get("ano_receita")
                
        if ano == ano_item:
           receita_mes = item.get("faturamento") - item.get("despesas")
           receita_total_ano += receita_mes
           
           if receita_mes > receita_maior_mensal:
               receita_maior_mensal = receita_mes
               mes_maior_receita = item.get("mes_receita")
               
           if item.get("despesas") > despesa_maior_mensal:
               despesa_maior_mensal = item.get("despesas")
               mes_maior_despesa = item.get("mes_receita")
                
   
    print(f"A receita total do ano de {ano} foi de {receita_total_ano}.")
    print(f"Neste ano o mês de maior receita foi o mês {mes_maior_receita}.")
    print(f"Neste ano o mês de maior despesa foi o mês {mes_maior_despesa}.")
    
                      
def calcular_receita_anual(dataset):
    receita_por_ano = {}
    
    for item in dataset:
        ano = item['ano_receita']
        receita = item['faturamento'] - item['despesas']
        if ano in receita_por_ano:
            receita_por_ano[ano] += receita
        else:
            receita_por_ano[ano] = receita
    
    return receita_por_ano

def ano_maior_menor_receita(dataset):
    receita_por_ano = calcular_receita_anual(dataset)
    ano_maior_receita = max(receita_por_ano, key=receita_por_ano.get)
    ano_menor_receita = min(receita_por_ano, key=receita_por_ano.get)
    
    print(f"{ano_maior_receita} foi o ano de maior receita.")
    print(f"{ano_menor_receita} foi o ano de menor receita.")

 
menu()

