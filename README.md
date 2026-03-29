#  Méthode des barrières logarithmiques

##  Description

Ce projet implémente un solveur d'optimisation non linéaire basé sur **la méthode des points intérieurs (Barrière Logarithmique)**. L'algorithme est conçu pour naviguer au sein d'un domaine de décision contraint afin d'identifier une solution optimale globale.

---

## Objectifs du projet

* Implémenter la méthode des barrières logarithmiques
* Utiliser la méthode de Newton pour l’optimisation
* Implémenter un solveur linéaire (méthode de Gauss)
* Assurer la faisabilité avec une recherche linéaire (line search)
* Comprendre les conditions d’optimalité (KKT)

---

## 🌍 Contexte Opérationnel (Cas d'étude)

Bien que cette approche s'applique à diverses formes mathématiques (Programmation Non Linéaire ,Programmation  Linéaire ,….etc), elle est ici illustrée (dans la description, l'implementation est général) par la Programmation Linéaire (PL), où les fonctions $f$ et $g_i$ sont des combinaisons linéaires des variables de décision.

Pour éprouver la robustesse de l'algorithme, nous modélisons un problème de planification logistique d'urgence près de Goma

<!-- #### Présentation du Problème : Opération Goma -->
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


