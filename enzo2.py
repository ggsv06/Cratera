def prob21(x):
    dif = 21 - x
    if dif < 10:
        f = dif/13
    else:
        f = 1
    f_porcento = f*100
    return f_porcento

print('\nProbabilidade de receber uma boa carta no jogo 21\n')

while True:
    escolha = input('Digite seu score atual, ou digite \'sair\': ')
    if str(escolha) == 'sair' or str(escolha) == 'Sair':
        break
    i = int(escolha)
    probabilidade = prob21(i)
    print(f'\n{probabilidade:.0f}%')