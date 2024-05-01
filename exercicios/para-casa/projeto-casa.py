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
    print("---BEM VINDE AO MENU---")
    print("Para adicionar registro = 1")
    print("Para calcular receita do ano = 2")
    print("Para saber ano de maior receita e de menor receita = 3")
    print("Para sair = 4")

    opt = input("Digite sua opção: ")
    print(opt)
    if opt == "1":
        adicionar_registro()
    elif opt == "2":
        calcular_receita()
    
    if opt == "3":
        ano_maior_menor()
    elif opt == "4":
        print("Saída")
    else:
         print("NENHUMA DAS OPÇÕES SÃO VÁLIDAS")


def adicionar_registro():
    ano_receita = input("Digite o ano da receita correspondente: ")
    mes_receita = input("Digite o mês da receita correspondente: ")
    faturamento = input("Digite o faturamento correspondente: ")
    despesas = input("Digite a despesa correspondente: ")

    novo_registro = {
        "ano_receita": ano_receita,
        "mes_receita": mes_receita,
        "faturamento": faturamento,
        "despesas": despesas
    }

    dataset.append(novo_registro)

    print(dataset)

    print("OPÇÃO ESCOLHIDA: 1")



    
def calcular_receita():
    ano = int(input("Digite o ano correspondente: "))
    receita_anual = 0
    receita = 0
    mes_maior_lucro = 0
    mes_maior_despesa = 0
    
    for item in dataset:
        ano_item = item.get("ano_receita")

        if ano_item == ano:
            receita = item.get("faturamento") - item.get("despesas")
            receita_anual += receita
            if receita > int(mes_maior_lucro):
                mes_maior_lucro == receita
                mes_maior_lucro = item.get("mes_receita")
            despesa = item.get("despesas")
            if despesa > receita:
             mes_maior_despesa == despesa
             mes_maior_despesa = item.get("mes_receita")
        
    print(f"O cálculo da receita do ano {ano} é: {receita_anual}")
    print(f"O mês {mes_maior_lucro} foi o de maior lucro e o mês {mes_maior_despesa} foi o de maior despesa")
    print("OPCÃO SELECIONADA: 2")


def ano_maior_menor():
    ano_um = int(input("Digite o primeiro ano: "))
    ano_dois = int(input("Digite o segundo ano: "))
    ano_tres = int(input("Digite o terceiro ano: "))
    receita = 0
    receita_anual = 0
    maior_receita = 0
    menor_receita = 0
    for item in dataset:
            ano_item = item.get("ano_receita")

            if ano_item == ano_um:
                receita = item.get("faturamento") - item.get("despesas")
                receita_anual += receita
                ano_um = receita_anual
    
    
           
    
            for item in dataset:
                ano_item = item.get("ano receita")
        
            if ano_item == ano_dois:
                receita = item.get("faturamento") - item.get("despesas")
                receita_anual += receita
                ano_dois = receita_anual
        

            for item in dataset:
                    ano_item = item.get("ano receita")        
            if ano_item == ano_tres:
                    receita = item.get("faturamento") - item.get("despesas")
                    receita_anual += receita
                    ano_tres = receita_anual

            if receita_anual > int(maior_receita):
                        maior_receita == receita_anual
                        maior_receita = item.get("ano_receita")
            
            if receita_anual < menor_receita: 
                        menor_receita == receita_anual                   
                        menor_receita = item.get("ano_receita")
    
    
    
    print(f"O ano {maior_receita} é o ano de maior receita, enquanto o ano {menor_receita} é o ano de menor receita.")
    print("OPCÃO SELECIONADA: 3")





menu()
