import argparse
import sys

# local import
import archivage
import reencoding

argvmode = sys.argv[1]
# Pour archivage:
# python3 main.py -archivage "url" -output "cheminverslelog"
# python3 main.py -archivage "cheminverslefichiertxt" -output "cheminverslelog"
# -output
# Pour rencodage:
# python3 main.py -reencodage -cible

if argvmode == "-archivage":
    if len(sys.argv) == 5:
        archivage.run(sys.argv[2], sys.argv[3], sys.argv[4])
    if len(sys.argv) == 4:
        archivage.run(sys.argv[2], sys.argv[3], None)

elif argvmode == "-reencodage":
    reencoding.recodefile(sys.argv[2])


elif argvmode == "-h" or argvmode == "-help":
    help =  """
usage: python3 main.py [mode] [option] 

[mode]:
-archivage: ce mode utilise wget pour télécharger un ou plusieurs sites
    usage: python3 main.py -archivage [cible(s)] [output] [option] 
    [cible(s)]:
        Test: utilise le site test suivant https://asuraaria.github.io/
        \"url\": applique l'archivage pour l'url donnée
        \"cheminversfichier\": permet de prendre en compte l'ensemble des lignes d'un ficher avec les règles suivantes:
            -une ligne commencent par un espace est ignorée
            -une ligne commencent par un # est ignorée
    [option]:
        -output "dossierDeDestination": wget devient non-verbeux dans la console et à la place sauvegarde les logs de progressions dans le dossier de destination
    ex :  python3 main.py -archivage Test ~/Desktop/ProjetArchivage/download/ ~/Desktop/ProjetArchivage/log/

-reencodage: ce mode permet de modifier de manière récursive des dossiers de sites locaux (WIP)
    usage: python3 main.py -reencodage [cible(s)]     
    [cible(s)]:
        \"cheminversdossier\": détermine le dossier à modifier
"""

    print(help)
