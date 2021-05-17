#!/usr/bin/env python3
# -*-coding:utf-8-*


import sys

""" Mapper: identifier et compter les triangles """


def main(file):
    # récupérer le contenu du fichier
    data = file.read().splitlines()

    # déterminer toutes les personnes qui interviennent dans le graphe
    persons = set()
    for line in data:
        relation = line.strip().split()
        for person in relation:
            persons.add(person)

    # déterminer tous les triangles possibles du graphe
    possibles_triangles = set()
    for first in persons:
        for second in persons:
            for third in persons:
                if first != second and second != third and first != third:
                    possibles_triangles.add(tuple(sorted((first, second, third))))

    # déterminer les relations existantes des triangles possibles
    keys_values = []
    for possible_triangle in possibles_triangles:
        for line in data:
            relation = line.strip().split()
            if relation[0] in possible_triangle and relation[1] in possible_triangle:
                keys_values.append([possible_triangle, tuple(relation)])

    # sortir sur la sortie standard
    for key_value in keys_values:
        print(key_value[0][0], ',', key_value[0][1], ',',  key_value[0][2], '===>', key_value[1][0], ',', key_value[1][1], sep='')


if __name__ == "__main__":
    main(sys.stdin)
