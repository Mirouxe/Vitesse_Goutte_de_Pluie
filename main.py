import numpy as np
import matplotlib.pyplot as plt

# ==== CONSTANTES ====
pair = 1.292    # Densité de l'air (kg/m³)
peau = 1e3      # Densité de l'eau (kg/m³)
Ro = 1e-3       # Rayon de la goutte de pluie (m)
pee = np.pi     # Constante Pi
g = 9.81        # Gravité (m/s²)
Cx = 0.445      # Coefficient de traînée
muair = 1.81e-5 # viscosite dynamique de l'air (Pa/s)

vo = 0.1      # Vitesse initiale (m/s)
time = 20     # Durée (s)
dt = 1        # Intervalle de temps (s)

t = np.arange(0, time + dt, dt)  # Temps 

# ==== CALCUL DES VITESSES ====

def calc_v1(t):
    """Hypothèse 1 : Sans frottement"""
    return (1 - pair / peau) * g * t + vo

def calc_v2(t):
    """Hypothèse 2 : Loi de traînée linéaire"""
    alpha = 6*pee*Ro*muair
    a2 = 3 / 4 * alpha / (peau * pee * Ro**3)
    return vo * np.exp(-a2 * t) + g / a2 * (1 - pair / peau) * (1 - np.exp(-a2 * t))

def calc_v3(t):
    G = g * (1-pair/peau)
    a3 = 3 / (8 * Ro) * Cx * (pair / peau)
    ra3 = np.sqrt(a3)
    rG = np.sqrt(G)
    return np.sqrt(G / a3) * np.tanh(ra3 * t + 1 / 2 * np.log((rG + ra3 * vo) / (rG - ra3 * vo)))

def calc_v3b(t):
    """Hypothèse 3b : Loi de traînée quadratique sans Archimède"""
    a3b = 3 / (8 * Ro) * Cx * (pair / peau)
    ra3b = np.sqrt(a3b)
    rg = np.sqrt(g)
    return np.sqrt(g / a3b) * np.tanh(ra3b * t + 1 / 2 * np.log((rg + ra3b * vo) / (rg - ra3b * vo)))

# ==== GRAPHIQUE ====

def plot_velocity(t, v1, v2, v3, v3b):
    """Fonction pour afficher les vitesses en fonction du temps"""
    plt.figure(figsize=(12, 8))
    plt.plot(t, v1, label='Hypothèse 1 (Sans frottement)', color='blue', marker='o', linestyle='-', linewidth=1.5, markersize=6)
    plt.plot(t, v2, label='Hypothèse 2 (Loi de traînée linéaire)', color='red', marker='s', linestyle='--', linewidth=1.5, markersize=6)
    plt.plot(t, v3, label='Hypothèse 3 (Loi de traînée quadratique)', color='green', marker='^', linestyle='-.', linewidth=1.5, markersize=6)
    plt.plot(t, v3b, label='Hypothèse 3b (Loi de traînée quadratique sans Archimède)', color='purple', marker='D', linestyle=':', linewidth=1.5, markersize=6)

    plt.title('Évolution de la vitesse v en fonction du temps t', fontsize=16, fontweight='bold')
    plt.xlabel('Temps (s)', fontsize=14)
    plt.ylabel('Vitesse v(t) (m/s)', fontsize=14)

    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.axhline(0, color='black', linewidth=0.75, ls='--')
    plt.axvline(0, color='black', linewidth=0.75, ls='--')

    plt.xlim(0, max(t))
    plt.ylim(min(min(v1), min(v2), min(v3), min(v3b)) - 1, max(max(v1), max(v2), max(v3), max(v3b)) + 1)

    plt.legend(fontsize=12, loc='best', title='Hypothèses', title_fontsize='13')
    plt.show()

# ==== CALCUL ET AFFICHAGE ====

v1 = calc_v1(t)
v2 = calc_v2(t)
v3 = calc_v3(t)
v3b = calc_v3b(t)

plot_velocity(t, v1, v2, v3, v3b)
