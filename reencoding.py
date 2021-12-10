import os
import codecs
#pip install inquirer
import inquirer

path = "/home/ubuntuvm/Desktop/ProjetArchivage/output"

def recodefile():

    questions = [
                inquirer.List(
                                'answer',
                                message="Quelle site sera la cible du réencodage?",
                                choices=[f.name for f in os.scandir(path) if f.is_dir()],
                            ),
                ]
    choice = inquirer.prompt(questions)["answer"]
    print(choice)
    reEncoding(path + "/" + choice)

def reEncoding(url):

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(url):
        for file in f:
            # for each html file
            if file.endswith('.html'):
                files.append(os.path.join(r, file))


    for f in files:
        print (f)

        with codecs.open(f, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace('charset=iso-8859-1', '')

        # Write the file out again
        with codecs.open(f, 'w') as file:
            file.write(filedata)