# Criação do dataset

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

# Criando a função menu

def menu():
    while True:
        print("+--------------------------------------------+")
        print("+                MENU LOJINHA                +")
        print("+--------------------------------------------+")
        print("+ 1 - Adicionar novo registro                +")
        print("+ 2 - Calcular faturamento                   +")
        print("+ 3 - Visualizar todos os registros          +")
        print("+ 4 - Mostrar anos com maior e menor receita +")
        print("+ 0 - Sair                                   +")
        print("+--------------------------------------------+")

        opt = input("+ Insira a opção desejada: ")

        if opt not in ["0", "1", "2", "3", "4"]:
            print("Opção inválida, digite uma opção válida.")
            continue
            
        if opt == "1":
            adicionar_registro()
        elif opt == "2":
            mostrar_receita()
        elif opt == "3":
            mostrar_registros()
        elif opt == "4":
            mostrar_anos_receita()
        elif opt == "0":
            break

# Criando a função para adicionar registro
def adicionar_registro():
    try:
        ano = int(input("+ Insira o ano correspondente: "))
        mes = input("+ Insira o mês correspondente: ")
        faturamento = int(input("+ Insira o faturamento correspondente a esse mês: "))
        despesas = int(input("+ Insira as despesas correspondentes a esse mês: "))

        novo_registro = {
            "ano_receita": ano,
            "mes_receita": mes,
            "faturamento": faturamento,
            "despesas": despesas
        }

        dataset.append(novo_registro)
        print("Registro adicionado com sucesso!")
    except ValueError:
        print("Erro: Certifique-se de inserir números inteiros para ano, faturamento e despesas.")

# Criando a função mostrar receita
def mostrar_receita():
    mes = input("+ Insira o mês que gostaria de saber a receita: ")
    valor_total = 0
    receita_maior = 0
    receita_menor = 0
    ano_maior_receita = 0
    ano_menor_receita = 0

    for el in dataset:
        if el["mes_receita"] == mes:
            receita = el["faturamento"] - el["despesas"]
            valor_total += receita
            
            if receita > receita_maior:
                receita_maior = receita
                ano_maior_receita = el["ano_receita"]
                
            if receita < receita_menor:
                receita_menor = receita
                ano_menor_receita = el["ano_receita"]

    if valor_total == 0:
        print("Nenhum registro encontrado para o mês especificado.")
    else:
        print(f"A soma das suas receitas é: {valor_total}.")
        print(f"O ano {ano_maior_receita} teve a maior receita para este mês, com um valor de {receita_maior}.")
        print(f"O ano {ano_menor_receita} teve a menor receita para este mês, com um valor de {receita_menor}.")

# Criando a função para visualizar todos os registros
def mostrar_registros():
    if not dataset:
        print("Não há registros disponíveis.")
    else:
        print("Registros:")
        for idx, reg in enumerate(dataset, start=1):
            print(f"Registro {idx}: {reg}")

# Função para mostrar os anos com maior e menor receita
def mostrar_anos_receita():
    anos = set([data['ano_receita'] for data in dataset])
    receitas_ano = {}
    for ano in anos:
        receitas_ano[ano] = sum(data['faturamento'] - data['despesas'] for data in dataset if data['ano_receita'] == ano)

    ano_maior_receita = max(receitas_ano, key=receitas_ano.get)
    ano_menor_receita = min(receitas_ano, key=receitas_ano.get)

    print(f"O ano com maior receita foi {ano_maior_receita} com um total de {receitas_ano[ano_maior_receita]}.")
    print(f"O ano com menor receita foi {ano_menor_receita} com um total de {receitas_ano[ano_menor_receita]}.")


# Chamando a função menu
menu()