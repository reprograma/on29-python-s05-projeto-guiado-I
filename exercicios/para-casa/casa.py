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
        print("Escolha uma das opções a seguir: 1) adicionar novo registro; 2) Calcular a receita do ano escolhido; 3) Mostrar qual ano teve a melhor receita e qual teve a pior; 0) Encerrar programa!")
        escolha = int(input("Escolha a opção que deseja (aceita apenas valores numéricos!): "))
        if escolha == 1:
            novo_registro()
        elif escolha == 2:
            receita_ano()
        elif escolha == 3:
            melhor_receita_ano()
        elif escolha == 0:
            print("programa encerrado")
            break
        else:
            print("entrada invalida, tente novamente")
            continue

def novo_registro():
    ano_receita = int(input("Digite o ano da nova receita: "))
    mes_receita = input("Qual o mês da nova receita: ")
    faturamento = int(input("Qual o faturamento da nova receita: "))
    despesas = int(input("Qual a despesa da nova receita: "))
    
    novo_registro = {'ano_receita': ano_receita, 
                     'mes_receita': mes_receita, 
                     'faturamento': faturamento, 
                     'despesas': despesas}
    
    dataset.append(novo_registro)
    print(dataset)

def receita_ano():
    ano = int(input("Qual ano da receita? "))
    valor_total = 0
    lucro_maior = 0
    despesa_menor = float('inf')  0
    

    for elemento in dataset:
        if ano == elemento.get("ano_receita"):
            receita = elemento.get("faturamento") - elemento.get("despesas")
            valor_total += receita

            if elemento.get("faturamento") > lucro_maior:
                lucro_maior = elemento.get("faturamento")
                mes_maior_lucro = elemento.get("mes_receita")

            if elemento.get("despesas") < despesa_menor:
                despesa_menor = elemento.get("despesas")
                mes_menor_despesa = elemento.get("mes_receita") 

    print(f"O valor total do ano {ano} é de {valor_total}")
    print(f"O mês {mes_maior_lucro} foi o que teve mais lucro, no valor de {lucro_maior}")
    print(f"O mês {mes_menor_despesa} foi o que teve menor despesa, no valor de {despesa_menor}")



def melhor_receita_ano():
    maior_despesa = 0
    menor_despesa = 100000

    for ano in dataset:
        receita_ano = ano.get("faturamento") - ano.get("despesas")
        if receita_ano > maior_despesa:
            maior_despesa = receita_ano
            ano_maior_receita = ano.get('ano_receita')
    print(f"O ano de maior despesa foi {ano_maior_receita} com valor de {maior_despesa}")
    
    for ano in dataset:
        receita_ano = ano.get("faturamento") - ano.get("despesas")
        if receita_ano < menor_despesa:
            menor_despesa = receita_ano
            ano_menor_receita = ano.get('ano_receita')
    print(f"O ano de menor despesa foi {ano_menor_receita} com valor de {menor_despesa}")

menu()