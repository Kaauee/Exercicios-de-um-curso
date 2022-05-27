# Criado um sistema de perguntas e respostas utilizando dicionario em python

def verificarPorcentagemAcertos(nota):
    porcent_acertos = nota / n_perguntas * 100
    print(f'Seu numero de acertos é {nota} de {n_perguntas}')
    print(f'Sua porcentagem de acertos é {porcent_acertos:.2f}%')


perguntas = {
    "Pergunta 1" : {
        "pergunta" : "Qual destes escritores não era do movimento literário chamado de Romantismo?: ",
        "resposta" : {
            "a": "José de Alencar",
            "b": "Castro Alves",
            "c": "Álvares de Azevedo",
            "d": "Oswald de Andrade",

        },
        "resposta_correta" : "d",

    },
    "Pergunta 2": {
        "pergunta": "Qual foi o primeiro longa-metragem brasileiro a concorrer ao Oscar?: ",
        "resposta": {
            "a": "Abril despedacado",
            "b": "O Quatrilho",
            "c": "O Pagador de Promessas",
            "d": "Orfeu Negro",
        },
        "resposta_correta": "c",

    },
    "Pergunta 3": {
        "pergunta": "Qual é o ramo da biologia que se dedica especificamente a estudar os fungos?: ",
        "resposta": {
            "a": "Fucologia",
            "b": "Micologia",
            "c": "Ficologia",
            "d": "Mucologia",
        },
        "resposta_correta": "b",

    },
    "Pergunta 4": {
        "pergunta": "Casu Marzu é um tipo italiano de: ",
        "resposta": {
            "a": "Queijo",
            "b": "Azeite",
            "c": "Fruta",
            "d": "Tuberculo",
        },
        "resposta_correta": "A",

    },

}
n_perguntas = len(perguntas)
n_resp_correta = 0

for perguntaNum,chave_2 in perguntas.items():
    print(f'{perguntaNum}: {chave_2["pergunta"]}')

    for pergunta,respostas in chave_2["resposta"].items():
        print(f'[{pergunta}] : {respostas}')

    resposta_usuario = input("Insira uma letra para responder: ")

    if resposta_usuario.lower() == chave_2["resposta_correta"]:
        n_resp_correta += 1

    print()

verificarPorcentagemAcertos(n_resp_correta)