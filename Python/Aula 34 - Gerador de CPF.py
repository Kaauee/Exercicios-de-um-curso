from random import randint

CPF = randint(10000000, 999999999)
CPF_semPontuacao = str(CPF)

### Criador de CPF

num_verificacoes = 0

while num_verificacoes < 2:

    soma = 0

    for pos_lista_cpf, multiplicacao_do_cpf in enumerate(range(len(CPF_semPontuacao) + 2, 2, -1)):
        multiplicacao_do_cpf-=1

        res = int(CPF_semPontuacao[pos_lista_cpf]) * multiplicacao_do_cpf
        soma += res

    formula = 11 - (soma % 11)

    if formula > 9:
        formula = 0
    CPF_semPontuacao = CPF_semPontuacao + str(formula)
    num_verificacoes += 1

pontuarCPF = ''

contagem = 0
for i in CPF_semPontuacao:
    pontuarCPF += i
    if contagem == 2 or contagem == 5:
        pontuarCPF += '.'

    if contagem == 8:
        pontuarCPF += '-'

    contagem += 1


print(f'O CPF: {pontuarCPF} foi gerado com sucesso!!!')
