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


#[ ] Crie um menu que onde seja possível fazer as seguintes opções:
#[ ] Adicionar um novo registro , contendo todos os dados necessários, 
# <b>seguindo o modelo dos registros do dataset</b>
#[ ] Calcular a receita do ano escolhido pelo usuário
#[ ] Exibir também qual foi o mês que teve mais lucro e o que teve mais despesa
#[ ] Mostrar qual ano teve a melhor receita e qual teve a pior
#[ ] Uma opção de saída
#[ ] Adicione uma condição para caso o usuário não digite uma opção válida no menu.

def menu():
    while True:
        print("----- Meu programa -----")
        print("----- Adicionar Registro - 1")
        print("----- Calcular Receita do ano - 2")
        print("----- Exibir maior lucro e despesa mensal - 3")
        print("----- Exibor ano com a maior receita - 4")
        print("----- Sair do menu - 0")
        
        opt = input ("Escolha uma opção:  ")
      
       
        if opt == "1":
                adicionar_registro()
        elif opt == "2":
                calcular_receita()
        elif opt == "3":
               exibir_maior_lucro_e_despesas()
        elif opt == "4":
                exibir_ano_maior_receita()
        elif opt == "0":
                print("Sair do menu")
                break
        else:
            print("Opção invalida")
    print("Muito Obrigado, volte sempre")
       
def adicionar_registro():  
      print("opção 1 escolhida - Adicionar registro")
      ano_receita = int(input("Digite o ano do registro:  "))
      mes_receita = input("Digite o mes do registro:  ")
      faturamento = int(input ("Digite o valor dos lucros:  "))
      despesas = int(input("Digite o valor dos gastos:  "))
    
      novo_registro = {
         "ano" : ano_receita,
         "mês" : mes_receita,
         "faturamento" : faturamento,
         "gastos" : despesas,
     }
      dataset.append(novo_registro)
      print(novo_registro)
      
def calcular_receita():
    print("Opção 2 escolhida - Calcular receita do ano")
    
    valor_total = 0
    ano_receita =int(0) 
    receita_maior = 0 
     
    ano_receita =int(input("Digite o ano que deseja a receita:   ")) 
    for el in dataset:
         ano_receita_el = el.get("ano_receita")
         if ano_receita_el == ano_receita:
             receita = (el.get("faturamento") - el.get("despesas"))
             valor_total += receita
             if receita > receita_maior:
                 receita_maior = receita
                 ano_receita = el.get("ano_receita")
    print(f"A soma das suas receitas do {ano_receita} é : {valor_total}")
     
 
def exibir_maior_lucro_e_despesas():
    print("Opção 3 escolhida - Exibir maior lucro e despesa mensal ")
    
     
    maior_lucro = 0 
    mes_lucro = 0
    maior_gasto = 0
    mes_gasto = 0
    
    ano_receita =int(input("Digite o ano que deseja a receita:   ")) 
    for el in dataset:
         ano_receita_el = el.get("ano_receita")
         if ano_receita_el == ano_receita:
            receita = (el.get("faturamento") - el.get("despesas"))
            
            if maior_lucro < receita:
                maior_lucro = receita
                mes_lucro = el.get("mes_receita")

            if maior_gasto > receita:
                maior_gasto = receita
                mes_gasto = el.get("mes_receita")
    print(f"O mês que você teve mais lucro foi o mês : {mes_lucro}")
    print(f"O mês que você teve maior gasto foi o mês : {mes_gasto}")
    
def exibir_ano_maior_receita():
    
  print("Opção 4 escolhida -  Exibir ano com a maior receita")
  
  maior_receita_anual = 0
  ano_receita = 0
      
  for el in dataset:
      ano_receita_el = (el.get("faturamento") - el.get("despesas"))
      
      if ano_receita_el >= maior_receita_anual:
          ano_receita_el == maior_receita_anual
          ano_receita = el.get("ano_receita")

  print(f"o lucro foi {ano_receita_el} e o ano foi {ano_receita}")     

        
    
    
   
                   
menu()