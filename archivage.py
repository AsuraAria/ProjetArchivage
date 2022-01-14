from pathlib import Path
import subprocess
import datetime
import re
    
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
        -S : Less encoding issues

        -P : output directory        

        --trust-server-names : (Useless?)
        -N : (REMOVE as renaming prevent it) Turn on time-stamping. Prevent duplication of already downloaded files (if up-to-date)        
        -nH : (REMOVED) By default, wget put files in a directory named after the site's hostname. This will disabled creating of those hostname directories and put everything in the current directory.
        -K : (REMOVED) keep an original versions of files without the conversions made by wget

    - url : url target of wget
    - directoryPath : output directory
    '''

    fullCommand = "wget " + args + " " + url + " -P " + directoryPath
    print(fullCommand)
    subprocess.call(fullCommand, shell=True)

def run(cible, directoryPath, logOutputFolder):

    #Vérification de l'existance du dossier, sinion création
    Path(directoryPath).mkdir(parents=True, exist_ok=True)    

    args = ' -l 0 -S -r -p -k -E -S --restrict-file-names=unix -e robots=off'

    # if log asked
    if (logOutputFolder):

        #Vérification de l'existance du dossier, sinion création
        Path(logOutputFolder).mkdir(parents=True, exist_ok=True)            

        #nommage du log
        truetime = str(datetime.datetime.now())
        time = re.sub(r"\D", "_", truetime.split(".")[0])
        args = '-nv -o ' + logOutputFolder + "log" + time + ".txt" + args

    # test sur site personel
    if(cible == 'Test'):
        runWGET(args, "https://asuraaria.github.io/", directoryPath)

    # for single url    
    elif(cible.startswith("www") or cible.startswith("http")):
        runWGET(args, cible, directoryPath)

    # for url list
    else:
        runThroughURL(cible, directoryPath, logOutputFolder)

    print("wget réussi (probablement).\nVeuillez vérifier si les pages sont bien encodées.\nDans le cas contraire pensez à utiliser le script reencoding.py")    

def runThroughURL(cible, directoryPath, logOutputFolder):
   
    with open(cible) as fp:
        for line in fp:
            url = line.strip()
            #chech if url not starting by # nor empty
            if (not url.startswith('#') and url):
                run(url,directoryPath, logOutputFolder)