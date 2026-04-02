from .algorith_principal import solveur_universel_barriere
import matplotlib.pyplot as plt
import numpy as np


def tracer_resultats_robuste(historique_x, c, A, b):
    hx = np.array(historique_x)
    n_vars = hx.shape[1]
    
    # --- CAS 1 : DEUX VARIABLES (2D) ---
    if n_vars == 2:
        plt.figure(figsize=(10, 7))
        # Ajustement de la plage de visualisation pour bien voir l'origine et la zone
        x1_max = np.max(hx[:,0])*1.5 if len(hx) > 0 else np.max(b)*1.5
        x_vals = np.linspace(0, x1_max, 100)
        
        # --- NOUVEAU : CALCUL DE LA ZONE RÉALISABLE ---
        # Initialiser y_poly avec une valeur très haute (plafond)
        y_poly = np.ones_like(x_vals) * np.max(b) * 2 
        # Pour les hachures, on suppose souvent x1 >= 0 et x2 >= 0
        y_sol_non_neg = np.zeros_like(x_vals) 

        # On trace chaque contrainte dynamiquement : Ai1*x1 + Ai2*x2 <= bi
        # => x2 = (bi - Ai1*x1) / Ai2
        for i in range(len(b)):
            if A[i, 1] != 0: # Éviter division par zéro
                y_val = (b[i] - A[i, 0] * x_vals) / A[i, 1]
                plt.plot(x_vals, y_val, label=f"Contrainte {i+1}")
                
                # --- NOUVEAU : MISE À JOUR DU POLYTOP ---
                # Si A[i,1] > 0, la contrainte est x2 <= y_val, on prend le MIN
                if A[i, 1] > 0:
                    y_poly = np.minimum(y_poly, y_val)
                # Si A[i,1] < 0, la contrainte est x2 >= y_val, on prendrait le MAX (non géré ici pour simplifier)

        # --- NOUVEAU : HACHURAGE DE LA ZONE ---
        # On remplace les valeurs négatives par 0 pour respecter x2 >= 0
        y_render = np.maximum(y_poly, y_sol_non_neg)
        
        # fill_between remplit entre 0 (y_sol_non_neg) et le plafond calculé (y_render)
        plt.fill_between(x_vals, y_sol_non_neg, y_render, 
                         color='gray', alpha=0.3, hatch='//', label='Zone Réalisable')
        # ----------------------------------------------

        # Chemin de l'algorithme
        if len(hx) > 0:
            plt.plot(hx[:,0], hx[:,1], 'go-', markersize=4, label="Chemin Central", zorder=4)
            plt.scatter(hx[-1,0], hx[-1,1], color='gold', s=150, zorder=5, label="Optimum")
        
        plt.xlabel('x1'); plt.ylabel('x2')
        # Définir des limites raisonnables pour x2 aussi
        x2_max = np.max(hx[:,1])*1.5 if len(hx) > 0 else np.max(b)*1.5
        plt.ylim(0, x2_max)
        
        plt.title("Visualisation 2D du Chemin Central avec Zone Réalisable")
        plt.legend(); plt.grid(True); plt.show()

    # --- CAS 2 : TROIS VARIABLES (3D) ---
    elif n_vars == 3:
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Trajectoire dans l'espace
        ax.plot(hx[:,0], hx[:,1], hx[:,2], 'go-', label="Chemin Central")
        ax.scatter(hx[-1,0], hx[-1,1], hx[-1,2], color='gold', s=200)
        
        ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('x3')
        plt.title("Visualisation 3D de la trajectoire")
        plt.legend(); plt.show()

    # --- CAS 3 : PLUS DE 3 VARIABLES (CONVERGENCE) ---
    else:
        print(f"Visualisation : {n_vars} variables détectées. Affichage du graphe de convergence.")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
        # Évolution de la valeur de l'objectif
        valeurs_obj = [np.dot(c, x) for x in hx]
        ax1.plot(valeurs_obj, 'b-o')
        ax1.set_title("Évolution de la fonction objectif")
        ax1.set_xlabel("Itérations (mu)"); ax1.set_ylabel("f(x)")
        
        # Évolution des variables
        for i in range(n_vars):
            ax2.plot(hx[:, i], label=f"x{i+1}")
        ax2.set_title("Convergence des variables")
        ax2.set_xlabel("Itérations"); ax2.legend()
        
        plt.tight_layout(); plt.show()


