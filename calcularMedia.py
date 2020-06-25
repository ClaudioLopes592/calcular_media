"""
Crie um programa que leia duas listas do teclado, correspondentes às notas de provas e de exercícios dos estudantes, normaliza cada nota dividindo-se a nota pelo máximo da lista correspondente e computa a média final de cada estudante, que é dada pela média geométrica entre a nota de prova e de exercícios.
"""
lista_provas = [] # Cria uma lista com as notas das provas
lista_exercicios = [] # Cria uma lista com as notas dos exercícios
cont = 1
fim = True
opcao = 'n'
while fim:
    # Solicita que seja informado as notas do aluno
    nprova = float(input(f'Digite a {cont}ª nota de prova do aluno: '.format(cont)))
    lista_provas.append(nprova)
    quant_notas = len(lista_provas)

    nexerc = float(input(f'Digite a {cont}ª nota de execício do aluno: '.format(cont)))
    lista_exercicios.append(nexerc)

    print('')
    # Pergunta se quer continuar a informar outras notas
    print("Digite [s] para 'Sim' e [n] para 'Não'")
    opcao = input('Deseja informar outra nota?')

    # Verifica se a opção foi para encerrar o programa
    if opcao == 'n' or opcao == 'N':
        fim = False

    # Soma as notas das provas
    soma_1 = 0.0
    for nprova in lista_provas:
        soma_1 += nprova
    
    # Soma as notas dos exercícios
    soma_2 = 0.0
    for nexerc in lista_exercicios:
        soma_2 += nexerc

    # Calcula a média geral
    soma_final = soma_1 + soma_2
    media_final = soma_final / (quant_notas * 2)

# Imprime na tela os pontos obtidos pelo aluno, sua média geral e o status obtido
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