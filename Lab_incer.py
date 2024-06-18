
# Energia cinética
def K(m, h):
    Kc = m*h*9.8*1000
    return Kc

# Incerteza da energia cinética
def uk(h, uh, m, um):
    u = 9.8*(((h*um)**2 + (m*uh)**2)**(1/2))*1000
    return u



# Massas das bolinhas de gudi e neodímio em Kg. Numerador em gramas é transformado para Kg dividindo por 1000
mg = 1/1000
mn = 1/1000


# Alturas de lançamento em m
Alturas = [0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.00, 1.28, 1.50]

Lista_kg = []
Lista_ukg = []

Lista_kn = []
Lista_ukn = []


# Incertezas de instrumentos
um = (0.1/(2*(3)**(1/2)))/1000

uhparalaxe = (0.5/(2*(6)**(1/2)))/100
uhzero = (0.1/(2*(6)**(1/2)))/100

uh = ((uhparalaxe)**2+(uhzero)**2)**(1/2)
print(f"\nIncertezas puras da massa em e altura respectivamentes:\t {um:.7f} Kg\t {uh:.4f} m")


# Cálculo da energia cinética da bolinha de gudi em 10^-3 J. Kg: Energia cinética gudi; ukgn: Incerteza de Kg
print("\n\nEnergia cinética de gudi em J")

for i in Alturas:
    kg = K(mg, i)
    ukg = uk(i, uh, mg, um)
    print(f"\n{i:.2f}\t{kg:.5f}\t+/- {ukg:.5f}")

    Lista_kg.append(kg)
    Lista_ukg.append(ukg)


# Cálculo da energia cinética da bolinha de neodímio em 10^-3 J. kn: Energia cinética neodímio; ukn: Incerteza de kn
print("\n\nEnergia cinética de neodímio em J")

for i in Alturas:
    kn = K(mn, i)
    ukn = uk(i, uh, mn, um)
    print(f"\n{i:.2f}\t{kn:.5f}\t+/- {ukn:.5f}")

    Lista_kn.append(kn)
    Lista_ukn.append(ukn)




