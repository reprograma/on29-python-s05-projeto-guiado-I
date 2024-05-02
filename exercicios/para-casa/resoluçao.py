#Use o dataset dataset_casa que se encontra no material adicional no classroom e cole para o seu arquivo python - assim como fizemos em aula, se lembra?

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

#Uma opção de saída

#Crie um menu que onde seja possível fazer as seguintes opções:
def menu():
    while True:  
        print(" - - - - - MENU LOJINHA - - - - - ")
        print("1. Novo registro")
        print("2. Calcular receita por ano")
        print("3. Calcular receita geral")
        print("0. Sair do menu")

        opt = input("Escolha a opção desejada: ")
        print("A opção escolhida foi ", opt)

        if opt == "1":
            adicionar_registro()
        elif opt == "2":
            calcular_receita()
        elif opt == "3":
            calcular_receita_geral()
        elif opt == "0":
            print("Encerramos o programa! Volte sempre.")
        else: ##Adicione uma condição para caso o usuário não digite uma opção válida no menu.
            print("Você não selecionou nenhuma opção válida.")
        break

def adicionar_registro(): #Adicionar um novo registro , contendo todos os dados necessários, seguindo o modelo dos registros do dataset
    ano_receita = int(input("Digite o ano que deseja verificar: "))
    mes_receita = input("Digite o mês que deseja verificar: ")
    faturamento = int(input("Adicione o lucro do mês correspondente: "))
    despesas = int(input("Digite as despesas do mês correspondente: "))

    novo_registro = { #adicionar dicionario
    "ano_receita": ano_receita,
    "mes_receita": mes_receita,
    "faturamento": faturamento,
    "despesas": despesas 
    }
            
    print(f"O novo registro é {novo_registro}")
                
            #adicionando o novo registro na memória da lista.
    dataset.append(novo_registro)
    print(dataset)

def calcular_receita(): #calcular receita geral do ano do usuário e também exibir qual mês teve maior lucro e qual teve maior gasto
    ano = int(input("Digite o ano que deseja calcular a receita: "))
    valor_total = 0
    maior_lucro = 0
    maior_despesas = 0
    mes_lucro = 0
    mes_gasto = 0

    #criar mais duas variaveis: dizer qual foi o mes, duas variaveis, uma pra dizer qual foi a mes que teve maior lucro e a que teve maior gasto

    for item in dataset: #convertendo o input pro elemento que o usuário quer verificar
        
        if ano == item.get("ano_receita"):
            receita = item.get("faturamento") - item.get("despesas")
            valor_total += receita #nos registros encontrados, calcular diferença entre lucro e gasto no ano > exibir resultado OK

            if maior_lucro < receita: #exibir qual foi o mês que teve mais lucro e o que teve mais despesa
                maior_lucro = receita # encontrando o maior lucro
                mes_lucro = item.get("mes_receita") # convertendo o valor do maior lucro pra encontrar o mês em que ele foi encontrado.

            if maior_despesas > receita:
                maior_despesas = receita
                mes_gasto = item.get("mes_receita")
            
    print(f"A diferença entre o lucro e o gasto do {ano} é de {valor_total}")
    print(f"No ano de {ano} o mês de maior lucro foi {mes_lucro} e o mês de maior despesa foi {mes_gasto}")

def calcular_receita_geral(): #Mostrar qual ano teve a melhor receita e qual teve a pior

    ano_maior_lucro = 0
    ano_menor_lucro = 0
    receita_maior = 0
    ano_menor_lucro = 0
    ano_melhor_lucro = 0
    
    for item in dataset:

         if item.get("ano_receita"):
            lucro_liquido = item.get("faturamento") - item.get("despesas")
            receita_maior += lucro_liquido

            if lucro_liquido > ano_maior_lucro: 
                ano_maior_lucro  = lucro_liquido
                ano_melhor_lucro = item.get("ano_receita") 

            if lucro_liquido < ano_menor_lucro:
                ano_menor_lucro = lucro_liquido
                ano_pior_lucro = item.get("ano_receita")        

    print(f"O {ano_melhor_lucro} foi o ano de maior lucro até a presente data. E o ano {ano_pior_lucro} foi o de maior despesa.")

menu()
