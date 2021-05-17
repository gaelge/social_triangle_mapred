#!/usr/bin/env python3
# -*-coding:utf-8-*


import sys

""" Reducer: identifier et compter les triangles """


def main(file):
    # récupérer la sortie des mappers
    data = file.read().splitlines()

    current_key = None
    current_count = 0
    reals_triangles = []
    for key_value_line in data:
        new_key = key_value_line.strip().split('===>')[0].split(',')
        new_key = tuple(new_key)

        # si la clé actuel est identique à la précédente
        # alors on continue le décompte
        if new_key == current_key:
            current_count += 1
            # égal à trois signifie qu'on a un triangle
            if current_count == 3:
                reals_triangles.append(current_key)
                continue
        # sinon, on reprend le décompte sur la nouvelle clé
        else:
            current_key = new_key
            current_count = 1

    # sortie du résultat final
    print('Les triangles identifies sont:')
    for real_triangle in reals_triangles:
        print(real_triangle)
    print('Nombre de triangle: ', len(reals_triangles))


if __name__ == "__main__":
    main(sys.stdin)
