#lojinha
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
def menu():
    print("----MENU LOJINHA----")
    print("adicionar novo registro - 1")
    print("calcular faturamento - 2")

    opt = input("Digite a opção desejada: ")

    if opt == "1":
        adicionar_registro()

    elif opt == "2":
        mostrar_receita()

'''
Digitar um mês e a receita desse mês
1 - captar o mês que ele quer]
2 - buscar no dataset o registro com o mês escolhido pelo usuario
3 - calcular a diferença entre o lucro e os gastos nos registros encontrados (receita)
4 - exibir resultado para usuário

------------

'''

def adicionar_registro():
    ano = int(input("digite o ano correspodente: "))
    mes = input("digite o mês correspodente: ")
    lucro = int(input("digite o lucro deste mês: "))
    gastos = int(input("digite os gastos corespodentes: "))

    novo_registro = {
        "ano": ano,
        "mes": mes,
        "lucro": lucro,
        "gastos": gastos
    }

    dataset.append(novo_registro)
    
    print(dataset)


def mostrar_receita():
    mes = input("digite o mês da receita correspodente : ")
    valor_total = 0
    maior_receita = 0
    ano = 0

    for el in dataset:
        mes_el = el.get("mes")
        if mes_el  == mes:
            receita = el.get("lucro") - el.get("gastos")
            valor_total += receita
            if receita > maior_receita:
                maior_receita = receita
                ano = el.get("ano")
    print(f"somatorio das receitas é:{valor_total}")
    print(f"o ano de {ano} foi o mais lucrativo e o valor da receita foi {maior_receita}")           
    
menu()
    