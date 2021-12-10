import subprocess
import os
#pip install inquirer
import inquirer
#dev utilities
import shutil

outputPath = "/home/ubuntuvm/Desktop/ProjetArchivage/output/log"
args = '-o ' + outputPath + ' -l 0 -S -r -p -k -E -nv --restrict-file-names=unix -e robots=off'
directoryPath = "/var/www/"


def setDirectoryPath():
    return input('Veuillez renseigner l\'adresse de destiation:\n')

def setURL():
    return input('Veuillez renseigner l\'adresse URL pour l\'extraction:\n')
    
def runWGET (args, url, directoryPath):

    '''
    runWGET (args, url, directoryPath)

    Takes three arguments :

    - args : wget args

        -r : recursive… of course we want to make a recursive copy
        -p, --page-requisites : download all necessary files for each page (css, js, images)
        -k, --convert-links : convert links to relative
        -E, --adjust-extension : rename html files to .html (if they don't already have an htm(l) extension)
        -o,--output-file=logfile : pathfile for output log
        -nv, --no-verbose, do not show progress bar
        -l 0 : the maximum level of recursion. WARNING 0 is no limit, might take a reeeaaaly long time.
        -restrict-file-names=OS : may be useful if you want to copy the files to a PC running with OS.        
        -e robots=off  : disable robot.txt restriction
        -F : When input is read from a file, force it to be treated as an HTML file.

        -P : output directory        

        --trust-server-names : (Useless?)
        -N : (REMOVE as renaming prevent it) Turn on time-stamping. Prevent duplication of already downloaded files (if up-to-date)        
        -nH : (REMOVED) By default, wget put files in a directory named after the site's hostname. This will disabled creating of those hostname directories and put everything in the current directory.
        -K : (REMOVED) keep an original versions of files without the conversions made by wget

    - url : url target of wget
    - directoryPath : output directory
    '''

    fullCommand = "wget " + args + " " + url + " -P " + directoryPath
    subprocess.call(fullCommand, shell=True)

def run():

    questions = [
                inquirer.List(
                                'answer',
                                message="Que sera la cible du wget?",
                                choices=['Test', 'Liste', 'Autre', "Quitter"],
                            ),
                ]
    choice = inquirer.prompt(questions)["answer"]
    print(choice)    

    if(choice == 'Test'):

        # test sur site personel

        url ="https://asuraaria.github.io/"
        runWGET(args, url, directoryPath)

    elif(choice == 'Liste'):

        runThroughURL()

    elif(choice == 'Autre'):

        url = setDirectoryPath()
        runWGET(args, url, directoryPath)

    elif(choice == 'Quitter'):
        return

    else:
        print('Erreur : le choix problématique est ' + choice)
        return "ERREUR"

    print("wget réussi (probablement).\nVeuillez vérifier si les pages sont bien encodées.\nDans le cas contraire pensez à utiliser le script reencoding.py")    

def prerun():

    try:
        shutil.rmtree(directoryPath)
    except OSError:
        print ("Suppresion of the directory %s failed" % directoryPath)
    else:
        print ("Successfully deleted the directory %s " % directoryPath)

    input("Press Enter to continue")    
        
    try:
        os.mkdir(directoryPath)
    except OSError:
        print ("Creation of the directory %s failed" % directoryPath)
    else:
        print ("Successfully created the directory %s " % directoryPath)

def runThroughURL():
   
    with open("urlList.txt") as fp:
        for line in fp:
            url = line.strip()
            #chech if url not starting by # nor empty
            if (not url.startswith('#') and url):
                runWGET(args, url, directoryPath)