import numpy as np
from src.Module_Bibliotheques.Algorith_Principal import solveur_universel_barriere
from src.Module_Bibliotheques.Visualisation import tracer_resultats_robuste



def main():

    # EXEMPLE D'APPEL (Votre exercice)

    c = np.array([-3, -2]) # Min -3x -2y
    A = np.array([[2, 1], [1, 1]]) # 2x+y <= 10 et x+y <= 8
    b = np.array([10, 8])

    solution, history = solveur_universel_barriere(c, A, b)
    print(f"Solution optimale : {solution}")

    print("  ")

    print("######################      VISUALIZATION     ########################")


    # Appel pour une valeur de mu moyenne (pour bien voir la forme)
    tracer_resultats_robuste(historique_x=history, c=c, A=A, b=b)


if __name__ == "__main__":
    main()