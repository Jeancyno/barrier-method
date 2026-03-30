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

Pour éprouver la robustesse de l'algorithme, nous modélisons un problème de planification logistique d'urgence près de Goma où le vecteur $\mathbf{x} = \begin{pmatrix} x \\ y \end{pmatrix}$ représentera les ressources stratégiques à déployer.

#### Présentation du Problème : Opération Goma

Dans une zone instable, une unité de réaction rapide doit être déployée pour sécuriser un corridor humanitaire. L’heure n’est plus à la discrétion, mais à la puissance de projection. Le commandement doit acheminer par hélicoptère deux types de ressources stratégiques : des Escouades de Commandos et des Unités de Ravitaillement Médical.Le défi du Commandant est de trouver la combinaison exacte d'hommes et de vivres permettant de maximiser l'impact opérationnel au sol lors d'une seule rotation. Ce déploiement massif est toutefois freiné par des paramètres logistiques rigides :

-Capacité d'emport : L'hélicoptère est limité à 10 tonnes de charge utile. Une escouade pèse 2 tonnes et une unité de ravitaillement pèse 1 tonne.

-Rotation de vol : Pour garantir une évacuation rapide, le nombre total de modules (hommes ou caisses) ne peut excéder 8 unités en soute.

Une escouade apporte 3 points d'efficacité tandis qu'une unité de ravitaillement en apporte 2.

#### Modélisation Mathématique

Pour résoudre ce dilemme, nous traduisons ces paramètres en un programme linéaire. Soit le vecteur de décision $\mathbf{x} = \begin{pmatrix} x \\ y \end{pmatrix}$, où $x$ est le nombre d'escouades et $y$ le nombre d'unités de ravitaillement.

##### Fonction Objectif (Maximisation de l'impact)

Le commandement cherche à maximiser l'efficacité totale $V(x, y)$. L'algorithme de barrière logarithmique étant nativement un processus de minimisation, nous transformons le problème en minimisant l'opposé de la fonction de gain :$$\text{Maximiser } V(x, y) = 3x + 2y \iff \text{Minimiser } f(x, y) = -3x - 2y$$

##### Contraintes de Faisabilité

Le déploiement doit satisfaire les fonctions de contraintes :

$g_i(x, y) \le 0$

- Poids ($g_1$) :
  - $2x + y \le 10$ 
  - équivalent à $2x + y - 10 \le 0$
- Espace ($g_2$) :
  - $x + y \le 8$
  - équivalent à $x + y - 8 \le 0$
- Non-négativité ($g_3, g_4$) :
  - $x \ge 0$ (donc $-x \le 0$)
  - $y \ge 0$ (donc $-y \le 0$)

L'objectif de l'algorithme est de trouver le point $(x, y)$ qui descend le plus bas possible dans la "vallée" créée par $f(x, y)$, ce qui correspondra mécaniquement au sommet d'efficacité le plus élevé.

---


## Résolution par la Méthode de Barrière

Pour traiter ces contraintes, nous définissons la fonction de barrière $B(x, y, \mu)$. Cette fonction "pénalise" le rapprochement des limites de l'hélicoptère en ajoutant un potentiel logarithmique qui tend vers l'infini aux frontières du domaine admissible :

$$B(x, y, \mu) = f(x, y) - \mu \sum_{i=1}^{4} \ln(-g_i(x, y))$$

La fonction de barrière s'écrit :

$$B(x, y, \mu) = -3x - 2y - \mu \ln(10 - 2x - y) - \mu \ln(8 - x - y) - \mu \ln(x) - \mu \ln(y)$$

 
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


