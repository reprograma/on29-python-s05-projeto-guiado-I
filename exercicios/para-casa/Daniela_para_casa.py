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

# 1. Use o dataset <b>dataset_casa</b> que se encontra no material adicional no classroom ou [no arquivo da pasta material](../../material/dataset_casa.py) e cole para o seu arquivo python - <b>assim como fizemos em aula, se lembra?</b>
# 2. Crie um menu que onde seja possível fazer as seguintes opções:
#       - Adicionar um novo registro , contendo todos os dados necessários, <b>seguindo o modelo dos registros do dataset</b>
#       - Calcular a receita do ano escolhido pelo usuário
#          - Exibir também qual foi o mês que teve mais lucro e o que teve mais despesa
#       - Mostrar qual ano teve a melhor receita e qual teve a pior
#       - Uma opção de saída
# 3. Adicione uma condição para caso o usuário não digite uma opção válida no menu.

def menu():   
    print("-----MENU LOJA LOJA-----")
    print("Adicionar novo registro - 1")
    print("Calcular receita - 2")

    opt = input("Digite a opção desejada: ")

    if opt =="1":
        adicionar_registro()
    elif opt == "2":
        calcular_receita()

def adicionar_registro():
    ano_receita = int(input("Digite o ano correspondente: "))
    mes_receita = input("Digite o mês correspondente: ")
    faturamento = int(input("Digite o faturamento neste mês: "))
    despesas = int(input("Digite a despesa neste mês: "))

    novo_registro = {
    "ano": ano_receita,
    "mes": mes_receita,
    "faturamento": faturamento,
    "despesas": despesas
}
    dataset.append(novo_registro)

    print(dataset)


def calcular_receita():
    mes_receita = input("Digite o mês que gostaria de saber a receita: ")
    ano_receita = 0
    
    for el in dataset:
        mes_receita_el = el.get("mes")
        if mes_receita_el == mes_receita:
            receita = el.get("faturamento") - el.get("despesas")
            ano_receita = el.get("ano")

    print(f"A receita para o mês escolhido é de {receita}")
    print(f"{ano_receita} foi o ano mais lucrativo da Loja Loja, para o mês {mes_receita}.")

         