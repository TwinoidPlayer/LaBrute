Tous les programmes : 

- Il faut obligatoirement le SID. J'explique comment le récupérer à la racine de ce github.

![sid Labrute](https://imgur.com/JLaeqtt)

########################################################################

jouer.py :

- Les tournois sont rejoints/quittés en début et en fin de programme.
- Si le tournois est gagné, la brute prendra le même arbre de compétences.
- Les lvl up se font automatiquement avec la compétence proposée à gauche.
- Toutes les brutes utiliseront l'hôpital.

########################################################################

recruter.py :

- "nb_recrut" doit être un entier (Plus vous aurez de brutes, plus le jouer.py prendra du temps à tourner) (A noter aussi que 2 brutes d'un même compte ne peuvent pas être dans le même tournoi)
- "nom" et "dernier" sont là pour nommer les brutes créées. Les brutes auront le nom dans "nom" + un espace + le chiffre dans dernier (qui augmentera à chaque brute générée)
- Si le nom de la brute que le programme essaye de créer existe déjà, il n'y aura pas d'erreur mais la brute ne sera pas créée.

(Exemple : si nb_recrut=3, nom="test brute" et dernier=10 le programme va créer "test brute 11", "test brute 12" et "test brute 13")


########################################################################

retraite.py :

- "nb_retraite" doit être un entier.
- Le programme retraitera le nombre de brute que vosu choisirez en partant de la FIN. (Je trouve ça plus logique)



Have fun sur LaBrute !
