"""
Crie um programa que leia duas listas do teclado, correspondentes às notas de provas e de exercícios dos estudantes, normaliza cada nota dividindo-se a nota pelo máximo da lista correspondente e computa a média final de cada estudante, que é dada pela média geométrica entre a nota de prova e de exercícios.
"""
lista_provas = []
lista_exercicios = []
cont = 1
fim = True
opcao = 'n'
while fim:
    nprova = float(input(f'Digite a {cont}ª nota de prova do aluno: '.format(cont)))
    lista_provas.append(nprova)
    quant_notas = len(lista_provas)

    nexerc = float(input(f'Digite a {cont}ª nota de execício do aluno: '.format(cont)))
    lista_exercicios.append(nexerc)

    print('')
    print("Digite [s] para 'Sim' e [n] para 'Não'")
    opcao = input('Deseja informar outra nota?')

    if opcao == 'n' or opcao == 'N':
        fim = False

    soma_1 = 0.0
    for nprova in lista_provas:
        soma_1 += nprova
    
    soma_2 = 0.0
    for nexerc in lista_exercicios:
        soma_2 += nexerc

    soma_final = soma_1 + soma_2
    media_final = soma_final / (quant_notas * 2)

if media_final >= 7.0:
    print('-' * 40)
    print(f'Este aluno obteve {soma_1 :.1f} pontos nas provas\nE {soma_2 :.1f} pontos nos exercícios\nCom a média geral de {media_final :.2f} pontos - Portanto está APROVADO!'.format(soma_1, soma_2, media_final))
    print('')
elif media_final >= 5.0 and media_final < 7.0:
    print('-' * 40)
    print(f'Este aluno obteve {soma_1 :.1f} pontos nas provas\nE {soma_2 :.1f} pontos nos exercícios\nCom a média geral de {media_final :.2f} pontos - Portanto está em RECUPERAÇÃO!'.format(soma_1, soma_2, media_final))
    print('')
elif media_final < 5.0:
    print('-' * 40)
    print(f'Este aluno obteve {soma_1 :.1f} pontos nas provas\nE {soma_2 :.1f} pontos nos exercícios\nCom a média geral de {media_final :.2f} pontos - Portanto está REPROVADO!'.format(soma_1, soma_2, media_final))
    print('')