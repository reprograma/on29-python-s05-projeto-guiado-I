dataset = [
    {'ano': 2022, 'mes': '1', 'lucro': 21003, 'gastos': 18600},
    {'ano': 2022, 'mes': '2', 'lucro': 31717, 'gastos': 54851},
    {'ano': 2022, 'mes': '3', 'lucro': 12571, 'gastos': 44701},
    {'ano': 2022, 'mes': '4', 'lucro': 23775, 'gastos': 51092},
    {'ano': 2022, 'mes': '5', 'lucro': 13251, 'gastos': 15321},
    {'ano': 2022, 'mes': '6', 'lucro': 44903, 'gastos': 47597},
    {'ano': 2022, 'mes': '7', 'lucro': 15476, 'gastos': 54529},
    {'ano': 2022, 'mes': '8', 'lucro': 27346, 'gastos': 15365},
    {'ano': 2022, 'mes': '9', 'lucro': 21968, 'gastos': 22234},
    {'ano': 2022, 'mes': '10', 'lucro': 48833, 'gastos': 54157},
    {'ano': 2022, 'mes': '11', 'lucro': 23418, 'gastos': 22423},
    {'ano': 2022, 'mes': '12', 'lucro': 38790, 'gastos': 26672},
    {'ano': 2023, 'mes': '1', 'lucro': 48187, 'gastos': 11384},
    {'ano': 2023, 'mes': '2', 'lucro': 16137, 'gastos': 49848},
    {'ano': 2023, 'mes': '3', 'lucro': 35136, 'gastos': 58523},
    {'ano': 2023, 'mes': '4', 'lucro': 48703, 'gastos': 15792},
    {'ano': 2023, 'mes': '5', 'lucro': 28860, 'gastos': 33990},
    {'ano': 2023, 'mes': '6', 'lucro': 16293, 'gastos': 11151},
    {'ano': 2023, 'mes': '7', 'lucro': 10136, 'gastos': 23093},
    {'ano': 2023, 'mes': '8', 'lucro': 11298, 'gastos': 27107},
    {'ano': 2023, 'mes': '9', 'lucro': 32300, 'gastos': 26678},
    {'ano': 2023, 'mes': '10', 'lucro': 16655, 'gastos': 29369},
    {'ano': 2023, 'mes': '11', 'lucro': 43447, 'gastos': 44161},
    {'ano': 2023, 'mes': '12', 'lucro': 22841, 'gastos': 36748},
    {'ano': 2024, 'mes': '1', 'lucro': 41066, 'gastos': 34235},
    {'ano': 2024, 'mes': '2', 'lucro': 38245, 'gastos': 24730},
    {'ano': 2024, 'mes': '3', 'lucro': 41615, 'gastos': 10681},
    {'ano': 2024, 'mes': '4', 'lucro': 44559, 'gastos': 14573},
    {'ano': 2024, 'mes': '5', 'lucro': 18150, 'gastos': 7673},
    {'ano': 2024, 'mes': '6', 'lucro': 10824, 'gastos': 12598},
    {'ano': 2024, 'mes': '7', 'lucro': 11844, 'gastos': 58096},
    {'ano': 2024, 'mes': '8', 'lucro': 38085, 'gastos': 20842},
    {'ano': 2024, 'mes': '9', 'lucro': 35128, 'gastos': 21076},
    {'ano': 2024, 'mes': '10', 'lucro': 42366, 'gastos': 24859},
    {'ano': 2024, 'mes': '11', 'lucro': 19202, 'gastos': 41544},
    {'ano': 2024, 'mes': '12', 'lucro': 25698, 'gastos': 51182},
]

# 1. Criar o menu para que o Sr. Miyagi consiga interagir e indicar o mês em que ele quer saber o faturamento
# 2. Criar a função de calcular a receita do mês que o Sr. Miyagi escolheu
# 3. Criar uma função que permita ao Sr. Miyagi introduzir um novo registro
# 4. Analisar se existe melhorias que podem ser feitas pensando na felicidade do Sr. Miyagi

# Explicação do exercício:

# Na lojinha do Sr. Miyagi, ele armazena o faturamento e os custos mensais manualmente em uma planilha. 
# Porém, o Sr. Miyagi precisa saber se ele está realmente lucrando ou se seu negócio está indo mal.
# Para ajudar-lo, ele nos pediu para que a gente criasse um pequeno programa em python que fosse capaz de calcular a receita de acordo com um mês. 
# Vamos ajuda-lo?

# Digitar um mês e receber a receita desse mês.
# 1º: Inserir o mês que ele quer;
# 2º: Pegar no banco de dados o registro que a gente quer;
# 3º: Calcular a diferença entre  lucro e gasto pra dar a RECEITA;
# 4º: Mostrar o resultado para o resultado


def menu():   
    print("-----MENU LOJINHA-----")
    print("Adicionar novo registro - 1")
    print("Calcular faturamento - 2")

    opt = input("Digite a opção desejada: ")

    if opt =="1":
        adicionar_registro()
    elif opt == "2":
        mostrar_receita()

def adicionar_registro():
    ano = int(input("Digite o ano correspondente: "))
    mes = input("Digite o mês correspondente: ")
    lucro = int(input("Digite o lucro neste mês: "))
    gastos = int(input("Digite os gastos neste mês: "))

    novo_registro = {
    "ano": ano,
    "mes": mes,
    "lucro": lucro,
    "gastos": gastos
}
    dataset.append(novo_registro)

    print(dataset)


def mostrar_receita():
    mes = input("Digite o mês que gostaria de saber a receita: ")
    valor_total = 0
    receita_maior = 0
    ano = 0
    
    for el in dataset:
        mes_el = el.get("mes")
        if mes_el == mes:
            receita = el.get("lucro") - el.get("gastos")
            valor_total += receita # valor_total = valor_total + receita
            if receita > receita_maior:
                receita_maior = receita
                ano = el.get("ano")

    print(f"A soma das suas receitas é de {valor_total}")
    print(f"{ano} foi o ano mais lucrativo da Lojinha do Sr Myiagi, para o mês {mes}.")

         

    # print("Opção escolhida: mostrar_receita")
menu()


# el = linha
# get = pega o elemento daquela linha

