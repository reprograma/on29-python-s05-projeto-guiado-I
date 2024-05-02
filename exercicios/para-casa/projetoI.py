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
        print("---MENU LOJINHA---")
        print("\nAdicionar novo registro --> 1")
        print("\nCalcular faturamento --> 2")
        print("\nConsultar faturamento --> 3")
        print("\nSair --> 0")
        
        opcao = input("Digite a opção desejada:")
        lista = ["1", "2", "3", "0"]
        if opcao not in lista:
            print("OPÇÃO INVÁLIDA. Digite uma opção válida:")
            continue
            
        if opcao == "1":
            adicionar_registro()
        elif opcao == "2":
            mostrar_receita()
        elif opcao == "3":
            consultar_receita()
        elif opcao == "0":
            break
# adicionei mais uma opção para filtrar um mês e ano específico 
        
def adicionar_registro():
    ano = int(input("Digite o ANO correspondente: "))
    mes = input("Digite o MÊS correspondente: ")
    
    meses = range(1,13)
    strmeses = [str(i) for i in meses]
    if mes not in strmeses:
#Foi preciso transformar o range de 1-12 em string pois na lista de dicionários a chave "mes_receita" tem valor em formato string.
        print("MÊS INVÁLIDO. Digite um mês entre janeiro e dezembro, do 1 ao 12:")
        return adicionar_registro()
#aqui esse bloco if retorna pra função adicionar_registro() pq não consegui retornar pro input da variável "mes", nas vezes q tentei retornava pro menu inicial ou dava erro

    faturamento = int(input("Digite o lucro neste mês: "))
    despesas = int(input("Digite os gastos deste mês: "))
    # aqui são as variáveis que receberão valores, inputs do usuário
    novo_registro = {
        "ano_receita": ano,
        "mes_receita": mes,
        "faturamento": faturamento,
        "despesas": despesas}
    
    dataset.append(novo_registro)
# append() adciona um novo registro baseado no input do usuario 

def mostrar_receita():
    ano = int(input("Digite o ANO: "))
    mes = input("Digite o MÊS: ")
    valor_total = 0
    receita_maior = 0
    receita_menor = 0
    ano_menor_receita = 0

  
    
    for i in dataset:
        mes_i = i.get("mes_receita")   
            
        if mes_i == mes:
            receita = i.get("faturamento") - i.get("despesas")
            valor_total = valor_total + receita
            
            if receita < receita_maior:
                receita_menor = receita
                ano_menor_receita = i.get("ano_receita")
            
            if receita > receita_maior:
                receita_maior = receita
                ano = i.get("ano_receita")
        else:
            print("VALOR INVÁLIDO. Digite um MÊS válido")

    
    print(f"A soma das suas receitas é: {valor_total}")
    print(f"O ano {ano} foi o ano mais lucrativo nesse mês, e o valor foi {receita_maior}")
    print(f"O ano {ano_menor_receita} foi o ano menos lucrativo desse mês, e o valor foi {receita_menor}")


def consultar_receita():
    ano = int(input("Digite o ano da receita que você deseja consultar: "))
    mes = input("Digite o mês da receita que você deseja consultar (1 a 12): ")
    ano_mes = False
    for i in dataset:
        if i['ano_receita'] == ano and i['mes_receita'] == mes:
            print(f"No mês de {mes} do ano de {ano} o faturamento foi de R${i['faturamento']:.2f} e as despesas foram de R${i['despesas']:.2f}")
            ano_mes = True
            break
    if not ano_mes:
        print("Não foi encontrado nenhum registro para o ano e mês fornecidos.")




menu()
