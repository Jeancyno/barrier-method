# Explication de la méthode des barrières logarithmiques

## 1. Introduction

La méthode des barrières logarithmiques est une technique d’optimisation permettant de résoudre des problèmes avec contraintes en les transformant en problèmes sans contraintes.

Elle appartient à la famille des **méthodes des points intérieurs**.



## 2. Problème général

On considère le problème :

Minimiser :

f(x)

Sous contraintes :

gᵢ(x) > 0



## 3. Transformation par barrière

On transforme le problème en :

φ(x, μ) = f(x) - μ ∑ ln(gᵢ(x))

où :

* μ > 0 est le paramètre de barrière
* ln(gᵢ(x)) empêche de sortir du domaine faisable

 Si gᵢ(x) → 0 alors ln(gᵢ(x)) → -∞



## 4. Principe de la méthode

L’algorithme suit les étapes :

1. Choisir un point initial faisable
2. Fixer μ initial
3. Résoudre le problème avec Newton
4. Réduire μ
5. Répéter jusqu’à convergence



## 5. Méthode de Newton

À chaque itération, on résout :

H(x) Δx = -∇φ(x)

Puis :

x ← x + α Δx

où :

* H(x) : Hessienne
* ∇φ(x) : gradient
* α : pas (line search)



## 6. Rôle des composants du projet

###  Gradient

Calcule la dérivée de la fonction barrière :

∇φ(x) = ∇f(x) - μ ∑ (∇gᵢ(x) / gᵢ(x))



###  Hessienne

Calcule la dérivée seconde :

∇²φ(x) = ∇²f(x) + μ ∑ ( (∇gᵢ ∇gᵢᵀ)/gᵢ² - ∇²gᵢ/gᵢ )



###  Solveur linéaire

Résout :

H Δx = -∇φ

via la méthode de Gauss.



###  Line Search

Garantit que :

gᵢ(x + αΔx) > 0

 donc on reste dans le domaine faisable



###  Newton

Calcule la direction de descente et met à jour x.

---

###  Méthode des barrières

Réduit progressivement μ pour se rapprocher de la solution réelle.



## 7. Convergence

Lorsque μ → 0 :

φ(x, μ) → f(x)

 La solution converge vers celle du problème original.



## 8. Résultat obtenu

Le programme converge vers :

(x, y) → (0, 0)

Avec une erreur très faible (~10⁻⁵)

 Ce qui confirme la validité de l’implémentation.



## 9. Conclusion

Ce projet montre :

* une implémentation complète de la méthode des barrières
* une maîtrise des outils mathématiques (gradient, Hessienne)
* une résolution numérique sans bibliothèques externes

 L’algorithme converge correctement vers la solution optimale.


