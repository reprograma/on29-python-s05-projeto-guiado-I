dataset = [
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


for dados in dataset:
    if  dados.get("lucro") > 30000:
        if dados.get("gastos") < 20000:
           print(dados)
          
