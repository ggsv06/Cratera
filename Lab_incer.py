import numpy as np

# Energia cinética
def K(m, h):
    Kc = m*h*9.8*1000
    return Kc

# Incerteza da energia cinética
def uk(h, uh, m, um):
    u = 9.8*(((h*um)**2 + (m*uh)**2)**(1/2))*1000
    return u

# Incerteza do logaritmo
def ulog(x, ux):
    ufinal = ux/(x*np.log(10))
    return ufinal

# Massas das bolinhas de gude e neodímio em Kg. Numerador em gramas é transformado para Kg dividindo por 1000
mg = 4.7/1000
mn = 16.3/1000


# Dados experimentais e tabelas bases. Obs: Diâmetros Dg, Dn estão em cm ; Alturas em c

Alturas = [0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.00, 1.28, 1.50]

Lista_Dg1 = [2.0,2.0,2.0,3.0,4.0,4.0,5.0,5.0,6.0]
Lista_Dg2 = [1.5,1.7,2.5,2.7,3.6,4.3,5.0,5.0,6.0]
Lista_Dn1 = [3.0,3.5,3.9,4.0,4.5,6.0,5.0,6.0,8.0]
Lista_Dn2 = [3.0,3.7,3.6,4.5,5.0,6.0,6.0,6.0,7.0]

Lista_Dgm = [1.8, 1.9, 2.3, 2.9, 3.8, 4.2, 5.0, 5.0, 6.0]
Lista_Dnm = [3.0, 3.6, 3.8, 4.3, 4.7, 6.0, 5.5, 6.0, 7.5]

Lista_ucomdesvio_g = []
Lista_ucomdesvio_n = []

Lista_LogDg = []
Lista_uLogDg = []

Lista_LogDn = []
Lista_uLogDn = []


Lista_kg = []
Lista_ukg = []
Lista_Logkg = []
Lista_uLogkg = []

Lista_kn = []
Lista_ukn = []
Lista_Logkn = []
Lista_uLogkn = []


    


# Incertezas de instrumentos
um = (0.1/(2*(3)**(1/2)))/1000

uparalaxe = (0.5/(2*(6)**(1/2)))/100
uhzero = (0.1/(2*(6)**(1/2)))/100

uh = ((uparalaxe)**2+(uhzero)**2)**(1/2)

udtolerancia = (0.1/(2*(6)**(1/2)))/100

for x1 , x2 , xm in zip(Lista_Dg1 , Lista_Dg2 , Lista_Dgm):
    
    sigma = ((xm-x1)**2+(xm-x2)**2)**(1/2)
    ud_desvio_padrao = ((sigma)/(2)**(1/2))/100
    udsigcom = ((uparalaxe)**2+(ud_desvio_padrao)**2)**(1/2)
    Lista_ucomdesvio_g.append(udsigcom)

for x1 , x2 , xm in zip(Lista_Dn1 , Lista_Dn2 , Lista_Dnm):
    
    sigma = ((xm-x1)**2+(xm-x2)**2)**(1/2)
    ud_desvio_padrao = ((sigma)/(2)**(1/2))/100
    udsigcom = ((uparalaxe)**2+(ud_desvio_padrao)**2)**(1/2)
    Lista_ucomdesvio_n.append(udsigcom)





print("\n################################################################################################################################")
print(f"\nIncertezas puras da massa e altura da cratera são respectivamentes:\t {um*1000:.2f} g\t {uh*100:.1f} cm")

# Cálculo das incertezas dos diâmetros da bolinha de gude
print("\n\nCálculo das incertezas dos diâmetros da bolinha de gude por estatística")
print("\nh(cm)\tDiâmetros médios (cm)\tIncerteza (cm)\n")

for i, j, k in zip(Alturas, Lista_Dgm, Lista_ucomdesvio_g):
    print(f"{i*100}\t\t{j:.1f}\t\t+/- {k*100:.1f}")


# Cálculo das incertezas dos diâmetros da bolinha de neodímeo
print("\n\nCálculo das incertezas dos diâmetros da bolinha de neodímio por estatística")
print("\nh(cm)\tDiâmetros médios (cm)\tIncerteza (cm)\n")

for i, j, k in zip(Alturas, Lista_Dnm, Lista_ucomdesvio_n):
    print(f"{i*100}\t\t{j:.1f}\t\t+/- {k*100:.1f}")


# Cálculo da energia cinética da bolinha de gude em 10^-3 J. Kg: Energia cinética gude; ukgn: Incerteza de Kg
print("\nEnergia cinética de gude em J 10^-3")
print("\nh(cm)\tEnergia média (J 10^-3)\tIncerteza\n")

for i in Alturas:
    kg = K(mg, i)
    ukg = uk(i, uh, mg, um)
    print(f"{i*100}\t\t{kg:.1f}\t\t+/- {ukg:.2f}")

    Lista_kg.append(kg)
    Lista_ukg.append(ukg)


# Cálculo da energia cinética da bolinha de neodímio em 10^-3 J. kn: Energia cinética neodímio; ukn: Incerteza de kn
print("\n\nEnergia cinética de neodímio em J 10^-3")
print("\nh(cm)\tEnergia média (J 10^-3)\tIncerteza\n")

for i in Alturas:
    
    kn = K(mn, i)
    ukn = uk(i, uh, mn, um)
    print(f"{i*100}\t\t{kn:.1f}\t\t+/- {ukn:.2f}")

    Lista_kn.append(kn)
    Lista_ukn.append(ukn)

# Cálculo de logaritmos dos diâmetros da bolinha de gude

print(f"\nLogaritmos dos diâmetros bolinha de gude")
print('\nDiâmetro(cm)\tLog\t\tIncerteza Log')

for i, j in zip(Lista_Dgm, Lista_ucomdesvio_g):
    
    logDg = np.log10(i)
    ulogDg = ulog(i, j)
    print(f'{i:.1f}\t\t{logDg:.2f}\t\t+/- {ulogDg:.4f}')
    Lista_LogDg.append(logDg)
    Lista_uLogDg.append(ulogDg)


# Cálculo de logaritmos dos diâmetros da bolinha de neodímio

print(f"\nLogaritmos dos diâmetros bolinha de neodímio")
print('\nDiâmetro(cm)\tLog\t\tIncerteza Log')

for i, j in zip(Lista_Dnm, Lista_ucomdesvio_n):

    logDn = np.log10(i)
    ulogDn = ulog(i, j)
    print(f'{i:.1f}\t\t{logDn:.2f}\t\t+/- {ulogDn:.4f}')
    Lista_LogDn.append(logDn)
    Lista_uLogDn.append(ulogDn)


# Cálculo de logaritmos das energias da bolinha de gude

print("\nLogaritmos das energias da bolinha de gude")
print('\nEnergia(J 10^-3)\tLog\t\tIncerteza Log')

for i, u in zip(Lista_kg, Lista_ukg):

    logKg = np.log10(i)
    ulogKg = ulog(i, u)
    print(f'{i:.1f}\t\t\t{logKg:.2f}\t\t+/- {ulogKg:.3f}')
    Lista_Logkg.append(logKg)
    Lista_uLogkg.append(ulogKg)


# Cálculo de logaritmos das energias da bolinha de neodímio

print("\nLogaritmos das energias da bolinha de neodímio")
print('\nEnergia(J 10^-3)\tLog\t\tIncerteza Log')

for i, u in zip(Lista_kn, Lista_ukn):

    logKn = np.log10(i)
    ulogKn = ulog(i, u)
    print(f'{i:.1f}\t\t\t{logKn:.2f}\t\t+/- {ulogKn:.3f}')
    Lista_Logkn.append(logKn)
    Lista_uLogkn.append(ulogKn)

