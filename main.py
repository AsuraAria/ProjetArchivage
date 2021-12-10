#pip install inquirer
import inquirer


#local import
import archivage
import reencoding

questions = [
            inquirer.List(
                        'answer',
                        message="Que voulez-vous faire?",
                        choices=["Archivage","Reencodage"],
                        ),
            ]
choice = inquirer.prompt(questions)["answer"]

print(choice)

if(choice == 'Archivage'):
    if (archivage.run()=="ERREUR"):
        print("Une erreur est subvenue.")
elif(choice == 'Reencodage'):
    reencoding.recodefile()