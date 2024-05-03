
import pandas as pd  
from tabulate import tabulate

dataset = [ 
    {'id': 1, 'ano_receita': 2022, 'mes_receita': '1', 'faturamento': 49179, 'despesas': 6295},
    {'id': 2, 'ano_receita': 2022, 'mes_receita': '2', 'faturamento': 12018, 'despesas': 43329},
    {'id': 3, 'ano_receita': 2022, 'mes_receita': '3', 'faturamento': 23524, 'despesas': 49376},
    {'id': 4, 'ano_receita': 2022, 'mes_receita': '4', 'faturamento': 29615, 'despesas': 16973},
    {'id': 5, 'ano_receita': 2022, 'mes_receita': '5', 'faturamento': 26527, 'despesas': 43742},
    {'id': 6, 'ano_receita': 2022, 'mes_receita': '6', 'faturamento': 48400, 'despesas': 11447},
    {'id': 7, 'ano_receita': 2022, 'mes_receita': '7', 'faturamento': 27219, 'despesas': 25593},
    {'id': 8, 'ano_receita': 2022, 'mes_receita': '8', 'faturamento': 46787, 'despesas': 19018},
    {'id': 9, 'ano_receita': 2022, 'mes_receita': '9', 'faturamento': 32306, 'despesas': 13522},
    {'id': 10, 'ano_receita': 2022, 'mes_receita': '10', 'faturamento': 27106, 'despesas': 15969},
    {'id': 11, 'ano_receita': 2022, 'mes_receita': '11', 'faturamento': 15255, 'despesas': 20105},
    {'id': 12, 'ano_receita': 2022, 'mes_receita': '12', 'faturamento': 23864, 'despesas': 32509},
    {'id': 13, 'ano_receita': 2023, 'mes_receita': '1', 'faturamento': 47240, 'despesas': 55776},
    {'id': 14, 'ano_receita': 2023, 'mes_receita': '2', 'faturamento': 42771, 'despesas': 36819},
    {'id': 15, 'ano_receita': 2023, 'mes_receita': '3', 'faturamento': 18008, 'despesas': 35853},
    {'id': 16, 'ano_receita': 2023, 'mes_receita': '4', 'faturamento': 21857, 'despesas': 6940},
    {'id': 17, 'ano_receita': 2023, 'mes_receita': '5', 'faturamento': 29735, 'despesas': 59626},
    {'id': 18, 'ano_receita': 2023, 'mes_receita': '6', 'faturamento': 33704, 'despesas': 30072},
    {'id': 19, 'ano_receita': 2023, 'mes_receita': '7', 'faturamento': 26515, 'despesas': 12129},
    {'id': 20, 'ano_receita': 2023, 'mes_receita': '8', 'faturamento': 18149, 'despesas': 21663},
    {'id': 21, 'ano_receita': 2023, 'mes_receita': '9', 'faturamento': 46176, 'despesas': 12564},
    {'id': 22, 'ano_receita': 2023, 'mes_receita': '10', 'faturamento': 24649, 'despesas': 58127},
    {'id': 23, 'ano_receita': 2023, 'mes_receita': '11', 'faturamento': 44484, 'despesas': 5304},
    {'id': 24, 'ano_receita': 2023, 'mes_receita': '12', 'faturamento': 30840, 'despesas': 5055},
    {'id': 25, 'ano_receita': 2024, 'mes_receita': '1', 'faturamento': 28726, 'despesas': 25133},
    {'id': 26, 'ano_receita': 2024, 'mes_receita': '2', 'faturamento': 34962, 'despesas': 26537},
    {'id': 27, 'ano_receita': 2024, 'mes_receita': '3', 'faturamento': 49424, 'despesas': 29649},
    {'id': 28, 'ano_receita': 2024, 'mes_receita': '4', 'faturamento': 42698, 'despesas': 54170},
    {'id': 29, 'ano_receita': 2024, 'mes_receita': '5', 'faturamento': 37237, 'despesas': 48453},
    {'id': 30, 'ano_receita': 2024, 'mes_receita': '6', 'faturamento': 30665, 'despesas': 8782},
    {'id': 31, 'ano_receita': 2024, 'mes_receita': '7', 'faturamento': 39597, 'despesas': 12261},
    {'id': 32, 'ano_receita': 2024, 'mes_receita': '8', 'faturamento': 49326, 'despesas': 18862},
    {'id': 33, 'ano_receita': 2024, 'mes_receita': '9', 'faturamento': 19043, 'despesas': 48517},
    {'id': 34, 'ano_receita': 2024, 'mes_receita': '10', 'faturamento': 24464, 'despesas': 24215},
    {'id': 35, 'ano_receita': 2024, 'mes_receita': '11', 'faturamento': 11635, 'despesas': 8190},
    {'id': 36, 'ano_receita': 2024, 'mes_receita': '12', 'faturamento': 39303, 'despesas': 14418}
]


def opcoes_sistema():
    while True:
        print("*****OPÇÕES DO SISTEMA*****")
        print("Opção 1: Adicionar um novo registro")
        print("Opção 2: Calcular a receita do ano escolhido")
        print("Opção 3: Exibir o mês com mais lucro e mais despesa")
        print("Opção 4: Mostrar o ano com melhor e pior receita")
        print("Opção 5: Excluir um registro do sistema")
        print("Opção 0: Sair do Sistema")
        
        option = input("Digite a opção desejada: ")
        
        if option != "0" and option != "1"  and option != "2" and option != "3" and option != "4" and option != "5":
            print("Por favor, digite uma das opções disponíveis.")
            continue
        
        if option == "1":
            AddData()
        elif option == "2":
            CalcBill()
        elif option == "3":
            HighProfitExpenseMonth()
        elif option == "4":
            BestWorstRevenueYear()
        elif option == "5":
            DropSyst()
        elif option == "0":
            print("Concluímos por aqui. Até a próxima.")
            break
        
def print_dataset():
    print("Dataset completo:")
    print(tabulate(dataset, headers="keys", tablefmt="grid"))
    

def AddData(): # Adicionando um novo registro
    novo_registro = {}
    novo_registro['id'] = len(dataset) + 1  
    novo_registro['ano_receita'] = int(input("Digite o ano correspondente: "))
    novo_registro['mes_receita'] = input("Digite o mês correspondente: ")
    novo_registro['faturamento'] = int(input("Digite o valor de faturamento: "))
    novo_registro['despesas'] = int(input("Digite o valor das despesas: "))

    dataset.append(novo_registro)
    print("Novo registro adicionado com sucesso.")
    print_dataset()


def CalcBill(): # Calculando a receita por ano 
    ano = int(input("Digite o ano que deseja calcular a receita: "))
    receita_ano = sum(item['faturamento'] - item['despesas'] for item in dataset if item['ano_receita'] == ano)
    print(f"A receita do ano {ano} é: {receita_ano}\n")


def HighProfitExpenseMonth(): # Mês com mais lucro e mais despesa
    lucro_maximo = 0
    mes_lucro_maximo = ''
    despesa_maxima = 0
    mes_despesa_maxima = ''

    for item in dataset:
        lucro = item['faturamento'] - item['despesas']
        
        if lucro > lucro_maximo:
            lucro_maximo = lucro
            mes_lucro_maximo = item['mes_receita']

        if item['despesas'] > despesa_maxima:
            despesa_maxima = item['despesas']
            mes_despesa_maxima = item['mes_receita']

    print(f"O mês com maior lucro foi: {mes_lucro_maximo}")
    print(f"O mês com maior despesa foi: {mes_despesa_maxima}")


def BestWorstRevenueYear(): # Ano com melhor e pior receita
    receita_por_ano = {}
    for item in dataset:
        ano = item['ano_receita']
        if ano in receita_por_ano:
            receita_por_ano[ano] += item['faturamento'] - item['despesas']
        else:
            receita_por_ano[ano] = item['faturamento'] - item['despesas']

    ano_melhor_receita = max(receita_por_ano, key=receita_por_ano.get)
    ano_pior_receita = min(receita_por_ano, key=receita_por_ano.get)

    print(f"O ano com melhor receita foi: {ano_melhor_receita}")
    print(f"O ano com pior receita foi: {ano_pior_receita}")


def DropSyst():  # Excluindo um registro por meio do ID
    id_registro = int(input("Digite o ID do registro que deseja excluir: "))
    for item in dataset:
        if item['id'] == id_registro:
            dataset.remove(item)
            print("Registro excluído com sucesso.")
            print_dataset()
            return
    print("Registro não encontrado.")

opcoes_sistema()