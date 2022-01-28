import subprocess
import sys


def finAvecErreur(numeroErreur, message=""):
    """
    Affiche un message d'erreur (en rouge) avec le nom du programme sur la sortie
    erreur et quitte avec un numero d'erreur

    :param numeroErreur: valeur de retour du programme
    :param message: message optionnel (défaut="") à afficher
    :return: pas de retour, appel à exit
    """

    print("\033[31m\n",
          sys.argv[0],
          "\n - Fin avec erreur :",
          message,
          "\033[0m",
          file=sys.stderr,
          sep='')
    errorReason(numeroErreur)
    print(message)
    sys.exit(numeroErreur)


def commandeShellOuFin(command, message=""):
    """
    Lance la commande passée en paramètre via subprocess.run en mode shell
      - affichage sur le flux en cours
      - levée d'une exception si retour en erreur puis appel de finAvecErreur avec le message et la valeur de retour de
        la commande

    :param command: commande shell à lancer
    :type command: str

    :param message: message complémentaire (en plus de l'erreur du run) à afficher en cas d'erreur
    :type message: str

    :return: none ou fin du programme si erreur dans le run
    :rtype: None
    """

    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        finAvecErreur(e.returncode, message + " - " + str(e))


def commandeShellOuFinAvecCaptureStdout(command, message=""):
    """
    Lance la commande passée en paramètre via subprocess.run en mode shell
      - le flux stdout est capturé (en mode texte)
      - levée d'une exception si retour en erreur puis appel de finAvecErreur avec le message et la valeur de retour de
        la commande

    :param command: commande shell à lancer
    :type command: str

    :param message: message complémentaire (en plus de l'erreur du run) à afficher en cas d'erreur
    :type message: str

    :return: sortie stdout ou fin du programme si erreur dans le run
    :rtype: str
    """

    try:
        result = subprocess.run(command,
                                check=True,
                                shell=True,
                                encoding="utf-8",
                                stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        finAvecErreur(e.returncode, message + " - " + str(e))

    return result.stdout


def errorReason(number):
    reason = "wget"
    if (reason=="wget"):
        if (number == 0):
            # Pourquoi le mettre? On ne sait jamais
            print(
                "Aucune erreur pour wget (i.e. retour 0) mais une erreur est levé de valeur 0"
            )
        elif (number == 1):
            print("Generic error code")
        elif (number == 2):
            print(
                "Parse error—for instance, when parsing command-line options, the \'.wgetrc\' or \'.netrc\'... "
            )
        elif (number == 3):
            print("File I/O error.")
        elif (number == 4):
            print("Network failure.")
        elif (number == 5):
            print("SSL verification failure.")
        elif (number == 6):
            print("Username/password authentication failure.")
        elif (number == 7):
            print("Protocol errors.")
        elif (number == 8):
            print("Server issued an error response.")