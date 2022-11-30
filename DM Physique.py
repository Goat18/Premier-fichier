import numpy as np
import matplotlib.pyplot as plt


def Modele_1(E0, w, s_0, w0, H0):
  f = w/(2*np.pi)
  T_caract = 2*np.pi/w
  T_obs = 10*T_caract  
  # On a décidé de T_obs = 10*T_caract
  
  delta_T = 1/(2*f) * 1/100
  # On choisit de prendre delta_T = 1/200 * 1/(2*fmax) <=> f_echant = 200*f_max
  
  N = int(T_obs/delta_T)
  # Nombre de points d'echantionnage.
  
  E = [0]*(N+1)
  S = [0]*(N+1)
  Temps = []
  S[0] = s_0
  # Initialisation S[0] = s_0
  
  for i in range(N+1):
    Temps.append(i*delta_T)
    E[i] = E0*np.cos(w*delta_T*i)
    if(i >= 1):
      S[i] = (1-w0*delta_T)*S[i-1]+H0*(E[i]-E[i-1])
  # Calculer les Sn et les En numériquement par la méthode d'Euler
  
  tracer(E, S, Temps)
  # Tracer les 2 graphes, delta_T se transmet pour calculer le temps correspondant

  
def tracer(E, S, Temps):
  plt.figure(figsize=(8, 10), layout='constrained')
  plt.scatter(Temps, E, label='Entree', color='r')
  plt.scatter(Temps, S, label = "Sortie", color='g')
  plt.ylabel('Tension en V')
  plt.xlabel('Temps en s')
  plt.title('Modele_2')
  plt.legend()
  plt.show()

# Modele_1(1,1,0,5,1)

#==================================================================
#==================================================================

def Modele_2(E0, w, s_0, w0, H0):
  f = w/(2*np.pi)
  T_caract = 2*np.pi/w
  T_obs = 10*T_caract  
  # On a décidé de T_obs = 10*T_caract
  
  # On decide de mettre 200 signaux composants pour former le signal créneau
  # Donc f_max = (2*200+1)*f
  delta_T = 1/(2*f*(2*200+1)) * 1/20
  # On choisit de prendre delta_T = 1/20 * 1/(2*fmax) <=> f_echant = 20*f_max
  
  N = int(T_obs/delta_T)
  # Nombre de points d'echantionnage.
  
  E = [0]*(N+1)
  S = [0]*(N+1)
  Temps = []
  S[0] = s_0
  # Initialisation S[0] = s_0
  
  for i in range(N+1):
    Temps.append(i*delta_T)
    E[i] = creneau(delta_T*i, w, E0)
    if(i >= 1):
      S[i] = (1-w0*delta_T)*S[i-1]+H0*(E[i]-E[i-1])
  # Calculer les Sn et les En numériquement par la méthode d'Euler
  
  tracer(E, S, Temps)
  # Tracer les 2 graphes, le Temps se transmet pour utiliser comme l'abscisse

def creneau(temps, w, E0):
  val = 0
  # Signal creneau de 200 composants
  for i in range(200):
    val += 1/(2*i+1) * np.sin((2*i+1)*w*temps)
  return 4/(2*np.pi) * 2 * E0 * val

Modele_2(1,5,0,5,1)
