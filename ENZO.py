import numpy as np
import matplotlib.pyplot as plt

def cel_sigma(m, x1):
    c = (m - x1)**2
    return c

def gaussiana(x, m, sigma):
    base = 1/((2*np.pi*(sigma**2))**(1/2))
    expoente = ((-1)*((x-m)**2))/(2*(sigma**2))
    f = base*np.exp(expoente)
    return f


Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Lista_sigma_numerador = []

media = sum(Lista)/len(Lista)

for i in Lista:
    soma = cel_sigma(media, i)
    Lista_sigma_numerador.append(soma)
sigma = (sum(Lista_sigma_numerador)**(1/2))/((len(Lista)-1)**(1/2))

x_sigma1 = media - sigma
x_sigma2 = media + sigma

x = np.linspace(0,11, 50)

plt.plot(x, gaussiana(x, media, sigma))
plt.show()

print('\n')
print(f'{x_sigma1:.0f}')
print(f'{x_sigma2:.0f}')
print(sigma)
print(media)