#  Méthode des barrières logarithmiques

##  Description

Ce projet implémente la **méthode des points intérieurs (barrière logarithmique)** pour résoudre un problème d’optimisation sous contraintes.

L’implémentation est réalisée **sans aucune bibliothèque externe (comme NumPy)** afin de garantir une compréhension complète des aspects mathématiques et numériques.

---

## Objectifs du projet

* Implémenter la méthode des barrières logarithmiques
* Utiliser la méthode de Newton pour l’optimisation
* Implémenter un solveur linéaire (méthode de Gauss)
* Assurer la faisabilité avec une recherche linéaire (line search)
* Comprendre les conditions d’optimalité (KKT)

---

## Exemple étudié

Minimiser :

f(x, y) = 3x + 2y

Sous contraintes :

* 2x + y ≤ 10
* x + y ≤ 8
* x ≥ 0
* y ≥ 0

---

##  Méthode utilisée

On transforme le problème en :

φ(x, μ) = f(x) - μ ∑ ln(gᵢ(x))

Puis on applique :

* Méthode de Newton
* Réduction progressive de μ
* Recherche linéaire pour garantir g(x) > 0

---

##  Structure du projet

```
barrier-method/
│
├── src/
│   ├── algorithm/        # Newton + méthode des barrières
│   ├── barrier/          # Gradient et Hessienne
│   ├── solver/           # Solveur Gauss + line search
│   ├── problem/          # Fonction objectif et contraintes
│   └── __init__.py
│
├── main.py               # Point d’entrée
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Installation

### 1. Cloner le projet

```bash
git clone https://github.com/Jeancyno/barrier-method.git
cd barrier-method
```

---

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

---

### 3. Activer l’environnement

#### Windows :

```bash
venv\Scripts\activate
```

#### Mac/Linux :

```bash
source venv/bin/activate
```

---

### 4. Installer les dépendances Facultatif

```bash
pip install -r requirements.txt
```

---

## ▶️ Exécution

```bash
python main.py
```

---

## Résultat

Le programme affiche les itérations de Newton et converge vers :

(x, y) → (0, 0)

Exemple :

```
Solution optimale : [4.06e-05, 6.10e-05]
```


# Méthode des barrières logarithmiques

## Description
Résolution des programmes linéaires par la méthode des barrières logarithmiques.
.

## Objectif
- Implémentation des conditions KKT
- Utilisation de la méthode de Newton
- Calcul manuel des matrices

## Exécution

```bash
python main.py
