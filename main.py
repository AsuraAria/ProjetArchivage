#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

# Import locaux
import archivage

# Modes de fonctionnement


def archivageMode(cible, destination, log):

    if ((cible is None) or (cible == 'arg_was_not_given')):
        print('Cible manquante')
    else:
        if ((destination is None) or (destination == 'arg_was_not_given')):
            print('Dossier de destination manquant')
        else:
            if log == 'arg_was_not_given':
                print(
                    'Option de logs spécifié mais chemin de destination manquant'
                )
            else:
                archivage.run(cible, destination, log)


def mode2():
    print('mode2')


def mode3():
    print('mode3')


# Gestion des options

parser = argparse.ArgumentParser(description='Travail d\'archivage.')

parser.add_argument('-m',
                    '--mode',
                    nargs='?',
                    const='arg_was_not_given',
                    help='le mode utilisé')
parser.add_argument('-l',
                    '--log',
                    nargs='?',
                    const='arg_was_not_given',
                    help='dossier de destination des logs, optionel')
parser.add_argument('-c',
                    '--cible',
                    nargs='?',
                    const='arg_was_not_given',
                    help='url ou chemin vers un fichier contenant les urls')
parser.add_argument('-d',
                    '--destination',
                    nargs='?',
                    const='arg_was_not_given',
                    help='chemin du dossier d\'extraction des cibles')

parser.add_argument('-a',
                    '--addarg',
                    nargs='+',
                    help='arguments supplémentaire pour le mode')

args = parser.parse_args()

# Run

if (args.mode == 'archivage'):
    archivageMode(args.cible, args.destination, args.log)
elif (args.mode == 'mode2'):
    # mode modification
    mode2()
elif (args.mode == 'mode3'):
    # mode paramètrage Apache
    mode3()
else:
    print('la spécificité de l\'argument -m n\'a pas été reconnu')