'''
pega o ovo, quebra, coloca o conteúdo na tigela
colocar açucar e adicionar manteiga

'''

ingredientes = {

    "ovos": 3,
    "açucar": "2 xicaras",
    "manteiga": "1 xicara",
    "leite": "1 xicara",
    "farinha": "3 xicaras"

} 

def fazer_bolo(ingredientes):
    preparar_o_ovo(ingredientes["ovos"])
    print(f"adicione {ingredientes["açucar"]}")
    print(f"de açucar e {ingredientes["manteiga"]} de manteiga")


def preparar_o_ovo(quantidade):
    print(f"{quantidade} de ovos foram quebrados e colocados na tigela")
    