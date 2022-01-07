#pip install inquirer
import sys

#local import
import archivage
import reencoding

argvmode = sys.argv[1]
#Pour archivage:
    # python3 main.py -archivage -cible(s) -output -logOutput
#Pour rencodage:
    # python3 main.py -reencodage -cible

if(argvmode == 'archivage'):
    if(len(sys.argv)==5):
        archivage.run(sys.argv[2],sys.argv[3],sys.argv[4])
    if(len(sys.argv)==4):
        archivage.run(sys.argv[2],sys.argv[3], None)    

elif(argvmode == 'reencodage'):
    reencoding.recodefile(sys.argv[2])


#TODO
elif(argvmode == 'Config Apache'):
    import apache

import argparse

parser=argparse.ArgumentParser(
    description='''Ceci est l'aide pour l'achivage Wev :). ''',
    epilog="""WIP.""")
parser.add_argument('--archivage --cible(s) -output -logOutput')
parser.add_argument('--archivage --cible(s) -output')
#parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
args=parser.parse_args()    