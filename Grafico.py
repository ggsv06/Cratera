from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from Lab_incer import *

config_plt = {
  "xtick.top": True,
  "ytick.right": True,
  "xtick.direction": "in",
  "ytick.direction": "in",
  "xtick.labelsize": 12,
  "ytick.labelsize": 12,
  "axes.titlesize": 12,
  "axes.labelsize": 12,
  "legend.fontsize": 12,
  "figure.subplot.wspace": 0.5,
  "figure.subplot.hspace": 0.5,
}
plt.style.use([config_plt])

# Identificar qual tipo de gráfico
while True:
  escolha = input('''
        \nQual tipo de gráfico deseja? Digite 
        [1] Gudi; D x E
        [2] Neodímio; D x E
        [3] Ambas bolinhas; D x E
        [4] Gudi; Log(D) x Log(E)
        [5] Neodímio; Log(D) x Log(E)
        [6] Ambas bolinhas; Log(D) x Log(E)
        [7] Sair
  ''')

  try:
    if escolha == str(1):
      Lx = Lista_kg
      Ly = Lista_Dgm
      Lux = Lista_ukg
      Luy = Lista_ucomdesvio_g

      unidade_x = "10^-3 J"
      unidade_y = "cm"
    
    elif escolha == str(2):
      Lx = Lista_kn
      Ly = Lista_Dnm
      Lux = Lista_ukn
      Luy = Lista_ucomdesvio_n
      
      unidade_x = "10^-3 J"
      unidade_y = "cm"

    elif escolha == str(3):
      Lx = Lista_kg + Lista_kn
      Ly = Lista_Dgm + Lista_Dnm
      Lux = Lista_ukg + Lista_ukn
      Luy = Lista_ucomdesvio_g + Lista_ucomdesvio_n

      unidade_x = "10^-3 J"
      unidade_y = "cm"

    elif escolha == str(4):
      Lx = Lista_Logkg
      Ly = Lista_LogDg
      Lux = Lista_uLogkg
      Luy =Lista_uLogDg

      unidade_x = "Log(10^-3 J)"
      unidade_y = "Log(cm)"

    elif escolha == str(5):
      Lx = Lista_Logkn
      Ly = Lista_LogDn
      Lux = Lista_uLogkn
      Luy =Lista_uLogDn
      
      unidade_x = "Log(10^-3 J)"
      unidade_y = "Log(cm)"

    elif escolha == str(6):
      Lx = Lista_Logkg + Lista_Logkn
      Ly = Lista_LogDg + Lista_LogDn
      Lux = Lista_uLogkg + Lista_uLogkn
      Luy =Lista_uLogDg + Lista_uLogDn
      
      unidade_x = "Log(10^-3 J)"
      unidade_y = "Log(cm)"

    elif escolha == str(7):
      break

    

  except KeyError:
    print("Erro. Digite um valor válido")
  except ValueError as e:
    print(e)
  except Exception as e:
    print(f"An unexpected error occurred: {e}")


  x = np.array(Lx)
  y = np.array(Ly)
  u_x = np.array(Lux)
  u_y = np.array(Luy)

  result = stats.linregress(x, y)

  # The number of digits printed might need to be ajusted.

  print(f'''"Linear regression:\n
  Slope: {result.slope:.2f}+-{result.stderr:.2f} \n
  Intercept: {result.intercept:.2f} +-{result.intercept_stderr:.2f}"
        ''')

  fig3, ax3 = plt.subplots(1, 1)
  ax3.errorbar(
    x,
    y,
    xerr=u_x,
    yerr=u_y,
    fmt="o",
    elinewidth=1,
    capsize=3,
    capthick=1,
    ms=3,
    c="b",
    ecolor="black",
  )
  if escolha == str(4) or escolha == str(5) or escolha == str(6):
    ax3.plot(x, x * result.slope + result.intercept)

  ax3.set_xlabel(f"Energia ({unidade_x})")
  ax3.set_ylabel(f"Diâmetro ({unidade_y})")
  plt.show()