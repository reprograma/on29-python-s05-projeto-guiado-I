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
        print(' ')
        print('---- LOJAS PONEIMANIA ----')
        print('Adicionar novo registro - 1')
        print('Calcular a receita de um determinado ano - 2')
        print('Verificar o ano com melhor e pior receita - 3')
        print('Sair - 0')

        opt_cliente = input('Digite a opção desejada: ')
        if opt_cliente == '1':
            adicionar_registro()
        elif opt_cliente == '2':
            calculo_receita()
        elif opt_cliente == '3':
            melhor_pior_receita()
        elif opt_cliente == '0':
            break
        else:
            print('Essa opção não é válida.')

def adicionar_registro():
    ano_receita = int(input('Digite o ano (exemplo: 2024): '))
    mes_receita = input('Digite o mês (exemplo: 2): ')
    faturamento = int(input('Digite o faturamento: R$'))
    despesas = int(input('Digite as despesas: R$'))

    novo_registro = {
        'ano_receita': ano_receita,
        'mes_receita':mes_receita,
        'faturamento': faturamento,
        'despesas': despesas
    }
    dataset.append(novo_registro)
    print(dataset)

def calculo_receita():
    ano_escolhido = int(input('Digite o ano que você deseja saber a receita: '))
    receita_anual = 0

    for el in dataset:
        ano_el = (el.get('ano_receita'))
        if ano_el == ano_escolhido:
            receita = el.get('faturamento') - el.get('despesas')
            receita_anual += receita

    print(f'No ano de {ano_escolhido}, a receita foi de R${receita_anual}.')

def melhor_pior_receita():
    ano_escolhido = int(input('Digite o ano que você deseja saber a receita: '))
    receita_maior = 0
    receita_menor = 0

    for el in dataset:
        ano_el = (el.get('ano_receita'))
        if ano_el == ano_escolhido:
            receita = el.get('faturamento') - el.get('despesas')
            if receita > receita_maior:
                receita_maior = receita
                mes_maior = el.get('mes_receita')
            if receita < receita_menor:
                receita_menor = receita
                mes_menor = el.get('mes_receita')
    print(f'A maior receita foi de R${receita_maior}, obtida no mês {mes_maior} do ano de {ano_escolhido}.')
    print(f'A menor receita foi de R${receita_menor}, obtida no mês {mes_menor}, do ano de {ano_escolhido}.')
                
menu()