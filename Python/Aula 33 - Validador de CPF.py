CPF_semPontuacao = ''

CPF = '192.502.789-93'

            ## Conversão CPF
listainicio = CPF.split('.')         ### 092   502   789-85
listafim = listainicio[2].split('-') ### 789   85
listainicio.pop()                    ### 092   502
listaTotal = listainicio + listafim  ### 092 502 789 85

for i in listaTotal:
    CPF_semPontuacao += i   ### 09250278985


### Verificação do CPF

num_verificacoes = 0

while num_verificacoes < 2:

    soma = 0

    for pos_lista_cpf, multiplicacao_do_cpf in enumerate(range(len(CPF_semPontuacao) + num_verificacoes, 2, -1)):
        multiplicacao_do_cpf-=1

        res = int(CPF_semPontuacao[pos_lista_cpf]) * multiplicacao_do_cpf
        soma += res

    formula = 11 - (soma % 11)

    if formula > 9:
        formula = 0

    CPF_temp = CPF.split('-')
    if int(CPF_temp[1][num_verificacoes]) == formula:
        num_verificacoes += 1
    else:
        print(f'O CPF: {CPF} é invalido')
        break

    if num_verificacoes == 2:
        print(f'O CPF: {CPF} é valido')