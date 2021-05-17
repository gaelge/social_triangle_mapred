# Description
L'objectif est d'identifier et de dénombrer la présence de structures triangulaires dans un graphe de réseau social.

Pour ce faire, nous avons opter pour l'utilisation du modèle MapReduce, que nous utiliserons ensuite avec le framework Hadoop.

Le fichier cible respecte un format bien précis à savoir, celui d'avoir sur chaque ligne deux éléments séparés par un simple espace.

Les éléments en questions peuvent être des identifiants sous forme de chiffres, de lettres, de nombres ou de noms.

Assurez-vous juste que les identifiants ne contiennent pas d'espace.

# Running
## Tester le code sans hadoop
Ouvrez votre terminal et positionnes-vous dans le répertoire du projet.

Ensuite, exécutez les commandes suivantes:

$ chmod +x mapper.py

$ chmod +x reducer.py

$ cat test_file | ./mapper.py | sort -k1,1 | ./reducer.py
