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

# Massas das bolinhas de gudi e neodímio em Kg. Numerador em gramas é transformado para Kg dividindo por 1000
mg = 4.7/1000
mn = 16.3/1000


# Dados experimentais e tabelas bases. Obs: Diâmetros Dg, Dn estão em cm ; Alturas em m

Alturas = [0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.00, 1.28, 1.50]

Lista_Dg = [1.8, 1.9, 2.3, 2.9, 3.8, 4.2, 5.0, 5.0, 6.0]
Lista_Dn = [3.0, 3.6, 3.8, 4.3, 4.7, 6.0, 5.5, 6.0, 7.5]

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

ud = ((uparalaxe)**2+(udtolerancia)**2)**(1/2)
Lista_ud = len(Lista_Dg)*[ud]

print("\n################################################################################################################################")
print(f"\nIncertezas puras da massa em, altura e diâmetro da cratera são respectivamentes:\t {um*1000:.2f} g\t {uh*100:.1f} cm\t {ud*100:.1f} cm")




# Cálculo da energia cinética da bolinha de gudi em 10^-3 J. Kg: Energia cinética gudi; ukgn: Incerteza de Kg
print("\n\nEnergia cinética de gudi em J 10^-3")
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

# Cálculo de logaritmos dos diâmetros da bolinha de gudi

print(f"\nLogaritmos dos diâmetros (+/-{ud:.3f})bolinha de gudi")
print('\nDiâmetro(cm)\tLog\t\tIncerteza Log')

for i in Lista_Dg:
    
    logDg = np.log10(i)
    ulogDg = ulog(i, ud)
    print(f'{i:.1f}\t\t{logDg:.2f}\t\t+/- {ulogDg:.4f}')
    Lista_LogDg.append(logDg)
    Lista_uLogDg.append(ulogDg)


# Cálculo de logaritmos dos diâmetros da bolinha de neodímio

print(f"\nLogaritmos dos diâmetros (+/- {ud:.3f}) bolinha de neodímio")
print('\nDiâmetro(cm)\tLog\t\tIncerteza Log')

for i in Lista_Dn:

    logDn = np.log10(i)
    ulogDn = ulog(i, ud)
    print(f'{i:.1f}\t\t{logDn:.2f}\t\t+/- {ulogDn:.4f}')
    Lista_LogDn.append(logDn)
    Lista_uLogDn.append(ulogDn)


# Cálculo de logaritmos das energias da bolinha de gudi

print("\nLogaritmos das energias da bolinha de gudi")
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

