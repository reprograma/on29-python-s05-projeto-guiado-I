dataset = [
    {'ano_receita': 2022, 'mes_receita': '1',
        'faturamento': 49179, 'despesas': 6295},
    {'ano_receita': 2022, 'mes_receita': '2',
        'faturamento': 12018, 'despesas': 43329},
    {'ano_receita': 2022, 'mes_receita': '3',
        'faturamento': 23524, 'despesas': 49376},
    {'ano_receita': 2022, 'mes_receita': '4',
        'faturamento': 29615, 'despesas': 16973},
    {'ano_receita': 2022, 'mes_receita': '5',
        'faturamento': 26527, 'despesas': 43742},
    {'ano_receita': 2022, 'mes_receita': '6',
        'faturamento': 48400, 'despesas': 11447},
    {'ano_receita': 2022, 'mes_receita': '7',
        'faturamento': 27219, 'despesas': 25593},
    {'ano_receita': 2022, 'mes_receita': '8',
        'faturamento': 46787, 'despesas': 19018},
    {'ano_receita': 2022, 'mes_receita': '9',
        'faturamento': 32306, 'despesas': 13522},
    {'ano_receita': 2022, 'mes_receita': '10',
        'faturamento': 27106, 'despesas': 15969},
    {'ano_receita': 2022, 'mes_receita': '11',
        'faturamento': 15255, 'despesas': 20105},
    {'ano_receita': 2022, 'mes_receita': '12',
        'faturamento': 23864, 'despesas': 32509},
    {'ano_receita': 2023, 'mes_receita': '1',
        'faturamento': 47240, 'despesas': 55776},
    {'ano_receita': 2023, 'mes_receita': '2',
        'faturamento': 42771, 'despesas': 36819},
    {'ano_receita': 2023, 'mes_receita': '3',
        'faturamento': 18008, 'despesas': 35853},
    {'ano_receita': 2023, 'mes_receita': '4',
        'faturamento': 21857, 'despesas': 6940},
    {'ano_receita': 2023, 'mes_receita': '5',
        'faturamento': 29735, 'despesas': 59626},
    {'ano_receita': 2023, 'mes_receita': '6',
        'faturamento': 33704, 'despesas': 30072},
    {'ano_receita': 2023, 'mes_receita': '7',
        'faturamento': 26515, 'despesas': 12129},
    {'ano_receita': 2023, 'mes_receita': '8',
        'faturamento': 18149, 'despesas': 21663},
    {'ano_receita': 2023, 'mes_receita': '9',
        'faturamento': 46176, 'despesas': 12564},
    {'ano_receita': 2023, 'mes_receita': '10',
        'faturamento': 24649, 'despesas': 58127},
    {'ano_receita': 2023, 'mes_receita': '11',
        'faturamento': 44484, 'despesas': 5304},
    {'ano_receita': 2023, 'mes_receita': '12',
        'faturamento': 30840, 'despesas': 5055},
    {'ano_receita': 2024, 'mes_receita': '1',
        'faturamento': 28726, 'despesas': 25133},
    {'ano_receita': 2024, 'mes_receita': '2',
        'faturamento': 34962, 'despesas': 26537},
    {'ano_receita': 2024, 'mes_receita': '3',
        'faturamento': 49424, 'despesas': 29649},
    {'ano_receita': 2024, 'mes_receita': '4',
        'faturamento': 42698, 'despesas': 54170},
    {'ano_receita': 2024, 'mes_receita': '5',
        'faturamento': 37237, 'despesas': 48453},
    {'ano_receita': 2024, 'mes_receita': '6',
        'faturamento': 30665, 'despesas': 8782},
    {'ano_receita': 2024, 'mes_receita': '7',
        'faturamento': 39597, 'despesas': 12261},
    {'ano_receita': 2024, 'mes_receita': '8',
        'faturamento': 49326, 'despesas': 18862},
    {'ano_receita': 2024, 'mes_receita': '9',
        'faturamento': 19043, 'despesas': 48517},
    {'ano_receita': 2024, 'mes_receita': '10',
        'faturamento': 24464, 'despesas': 24215},
    {'ano_receita': 2024, 'mes_receita': '11',
        'faturamento': 11635, 'despesas': 8190},
    {'ano_receita': 2024, 'mes_receita': '12',
        'faturamento': 39303, 'despesas': 14418}
]


def menu():
    while True:
        print("--------MENU--------")
        print("Adicionar novo registro - 1")
        print("Calcular a receita do ano - 2")
        print("Analise anual - 3")
        print("Sair - 0")
        opt = input("Escolha a opção desejada: ")

        if opt != "1" and opt != "2" and opt != "0" and opt != "3":
            print("Digite uma opção válida.")
            continue

        if opt == "1":
            adicionar_registro()
        elif opt == "2":
            receita_ano()
        elif opt == "3":
            analise_ano()
        elif opt == "0":
            break


def adicionar_registro():
    ano = int(input("Digite o ano correspondente: "))
    mes = input("Digite o mês correspondente: ")
    faturamento = float(input("Digite o luco do mês correspondente: "))
    despesas = float(input("Digite os gastos do mês correspondete: "))

    novo_registro = {
        "ano_receita": ano,
        "mes_receita": mes,
        "faturamento": faturamento,
        "despesas": despesas
    }
    dataset.append(novo_registro)
    print(dataset)


def receita_ano():
    ano = int(input("Digite o ano desejado: "))
    valor_total = 0
    maior_lucro = 0
    maior_despesa = 0
    mes_lucro = 0
    mes_despesa = 0

    for el in dataset:
        ano_el = el.get("ano_receita")
        if ano_el == ano:
            receita = el.get("faturamento") - el.get("despesas")
            valor_total += receita

            if receita > maior_lucro:
                maior_lucro = receita
                mes_lucro = el.get("mes_receita")

            if el.get("despesas") > maior_despesa:
                maior_despesa = el.get("despesas")
                mes_despesa = el.get("mes_receita")

    print(f"No ano escolhido, a soma das suas receitas é: {valor_total}")
    print(f"O mês {mes_lucro}, foi o que teve mais lucro no ano.")
    print(f"O mês {mes_despesa}, foi o qual se teve maior despesa no ano.")


def analise_ano():
    melhor_ano = 0
    pior_ano = 0
    melhor_receita = 0
    pior_receita = 0

    for el in dataset:
        ano = el.get("ano_receita")
        receita = el.get("faturamento") - el.get("despesas")

        if receita > melhor_receita:
            melhor_receita = receita
            melhor_ano = ano

        if receita < pior_receita:
            pior_receita = receita
            pior_ano = ano

    print(f"Sua melhor receita foi de {melhor_receita} no ano {melhor_ano}")
    print(f"Sua pior receita foi de {pior_receita}, no ano de {pior_ano}")


menu()
print("Fim do programa")
