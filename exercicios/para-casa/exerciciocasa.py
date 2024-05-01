from operator import itemgetter


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
        print("Bem-vindo à lojinha!Digite uma das opções a seguir:\n1- Adicionar um novo registro \n2- Calcular receita anual. \n3- Calcular a melhor e pior receita anual\n4- Sair do programa")
        opcao= input("Digite a opção desejada: ")
        if opcao == "1":
            adicionar_registro()
        elif opcao == "2":
            receita_ano()
        elif opcao == "3":
            ano_melhor_pior_receita()
        elif opcao == "4":
            print("encerrando programa....")
            break
        else:
            print("opçãp inválida!")
            
        print(f"Foi selecionado a opção {opcao}")

    
###Para adicionar um novo registro é necessário:
# 1- ano da receita; 2- mês da receita; 3- faturamento; 4- despesas; 6- lucro total
# 2- Calcular a receita do ano escolhido - lucro/receita= faturamento - despesas, após armazenar valor_total += receita
# e mostrar o mês que teve maior receita: fazer comparativo entre maiores e menores receitas obtidas
# 3- ano que teve maior lucro

def adicionar_registro():
    print("Vamos adicionar um novo registro à sua receita! É necessário os seguintes dados: ano, mês, faturamento e despesa. Vamos lá!")
    
#para receber os novos valores, como input é armazenado como string, fazemos a conversão automática para o tipo inteiro:
    ano= int(input("Digite o ano correspondente: "))
    mes= int(input("Digite o mês correspondente: "))
    faturamento= float(input("Digite o faturamento neste mês correspondente: "))
    despesas= float(input("Digite a despesa deste mês: "))

# adicionamos os novos valores ao dataset

    novo_registro= {
        "ano_receita": ano,
        "mes_receita": mes,
        "faturamento": faturamento,
        "despesas": despesas
    }
    dataset.append(novo_registro)
    print(f"Esse é a nova entrada no dataset: mês {mes} de {ano} com faturamento de R${faturamento} e despesa de R$ {despesas}")

def receita_ano():
    ano= int(input("Digite o ano que gostaria de obter a receita: "))
    lucroliq_total= int(0)
    lucro_liq_max= int(0)
#    mes_maior_lucro= 0
    maior_despesa= int(0)
    despesa_max= int(0)
    
    for el in dataset:        
        ano_el= el.get("ano_receita") # pega um dado especifico
        if ano_el == ano: # entra no ano especifico desde que escolhido pelo usuário
            lucroliq_mes= el.get("faturamento") - el.get("despesas")
            lucroliq_total += lucroliq_mes 
            
            if lucroliq_mes > lucro_liq_max:
                lucro_liq_max = lucroliq_mes
                mes_maior_lucro= el.get("mes_receita")
                
            if el.get("despesas") > despesa_max:
                despesa_max = el.get("despesas")
                maior_despesa = el.get("mes_receita")
                
    print(f"O lucro total para o ano {ano} é de: R${lucroliq_total}")
    print(f"O mês com maior lucro foi: {mes_maior_lucro} com lucro de R${lucro_liq_max}")
    print(f"O mês com maior despesa foi: {maior_despesa} com despesa de R${despesa_max}")
                
def ano_melhor_pior_receita(): # aqui minha intenção é calcular o lucro liquido de cada ano e fazer um comparativo
    lucroliq_total= {} # crio um dicionario vazio para chamar depois e armazenar os dados que serão calculados
    
    for el in dataset: #seguindo a mesma logica da prof
        ano= el.get("ano_receita")
        lucroliq_ano= el.get("despesas") - el.get("faturamento")
        lucroliq_total[ano] = lucroliq_ano # agora armazeno no dicionário
        
        # ordenar os anos com base nas chaves "ano"(índice 0) e "lucro"(índice 1) armazenadas no dicionario lucroliq_total
        anos_ordem_crescente = sorted(lucroliq_total.items(), key=itemgetter(1)) # ordenando com base no lucro (índice 1)
    print("Ano em ordem crescente de receita:")
        
    for ano, lucroliq_total in anos_ordem_crescente:
        print(f"Ano {ano}: R$ {lucroliq_total}")
        
    # Determinando o ano com a melhor e a pior receita
    melhor_ano = anos_ordem_crescente[-1][0]  # Pegando o último elemento da lista ordenada (melhor receita)
    pior_ano = anos_ordem_crescente[0][0]  # Pegando o primeiro elemento da lista ordenada (pior receita)
    melhor_lucro = anos_ordem_crescente[-1][1]  # Pegando o valor do último elemento da lista ordenada (melhor lucro)
    pior_lucro = anos_ordem_crescente[0][1]  # Pegando o valor do primeiro elemento da lista ordenada (pior lucro)
    
    print(f"\nO ano com a melhor receita foi: {melhor_ano} com um lucro total de: R${melhor_lucro}")
    print(f"O ano com a pior receita foi: {pior_ano} com um lucro total de: R${pior_lucro}")
        
menu()