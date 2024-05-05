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
'''
1 - criar um menu onde será possível fazer as seguintes opções:
# criar uma função chamada menu que irá printar as seguintes opções 

a) adicionar um novo registro contendo todos os dados necessários, seguindo o modelo.
b) Calcular a receita do ano escolhido pelo USUÁRIO
      b2) Calcular também qual foi o mês que teve mais lucro e o que teve mais despesa.
c) Mostrar qual ano teve a melhor receita e qual teve a pior
d) Uma opção de saída

3 - Adicione uma condição para caso o usuário não digite uma opção válida no menu.

'''
#Criar menu
def menu():
    while True:
        print('\n--------- Financeiro Doce Sabor ---------\n')
        print('Opções disponíveis: ')
        print('1 - Adicionar um novo registro\n2 - Calcular a receita de um ano\n3 - Vericar qual ano teve melhor receita e pior despesa\n4 - Sair ')
        opcao = int(input('\nDigite o número correspondente à opção desejada: '))
        
        if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 :
            print('\nOpção inválida, digite uma opção VÁLIDA!\n')
            continue
        
        if opcao == 1:
            adicionar_registro()
        elif opcao == 2:
            receita_anual()
        elif opcao == 3:
            maior_receita()
        elif opcao == 4:
            break
        
            
def adicionar_registro():
    ano_receita = int(input('Digite o ano: '))
    mes_receita = input('Digite o mês: ')
    faturamento = int(input('Digite o faturamento: '))
    despesas = int(input('Digite as despesas: '))
    
    novo_registro = {
        
        "ano_receita": ano_receita,
        "mes_receita": mes_receita,
        "faturamento": faturamento,
        "despesas": despesas
    }
    
    dataset.append(novo_registro)
# calcular a receita do ano escolhido   
def receita_anual():
    ano_receita = int(input('Digite o ano que gostaria de saber a receita:  '))
    receita_total = 0
    maior_lucro = 0
    mes = 0
    maior_despesa = int(0)
    mes_despesa_maior = 0
    
    for item in dataset:
        ano_calculado = item.get("ano_receita") 
        if ano_calculado == ano_receita: 
            receita = item.get("faturamento") - item.get("despesas")
            receita_total += receita
            if receita > maior_lucro:
                maior_lucro = receita
                mes = item.get("mes_receita")
                
            if item.get("despesas") > maior_despesa:
                maior_despesa = item.get("despesas")
                mes_despesa_maior = item.get("mes_receita")
                       
    print(f'A soma das suas receitas no ano de {ano_receita} é R$ {receita_total}')
    print(f'No ano de {ano_receita} seu mês com maior lucro foi o mês {mes}')
    print(f'E o mês com maior despesa foi o mês {mes_despesa_maior}')
    
'''
Mostrar qual ano teve a melhor receita e qual teve a pior
1 - Encontrar o ano que teve a melhor receita 
    calcular a receita de cada ano existente dentro do dataset
    verificar qual ano possui a maior receita, depois a pior
'''
def maior_receita():
    maior_receita = 0
    pior_receita = 0
    
    for ano in dataset:
        receita = ano.get("faturamento") - ano.get("despesas")
        maior_receita += receita
        if receita > maior_receita:
            maior_receita = receita
            ano_melhor_receita = ano.get("ano_receita")
        if receita < maior_receita:
            pior_receita += receita
            ano_pior_receita = ano.get("ano_receita")
             
    print(f'O seu ano com maior receita foi {ano_melhor_receita}.')
    print(f'O seu ano com pior receita foi {ano_pior_receita}.')  
            
menu()
