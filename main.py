import random

NB_MIN = 1
NB_MAX = 10
NB_QUESTIONS = 5

def poser_question1():
    a = random.randint(NB_MIN, NB_MAX)
    b = random.randint(NB_MIN, NB_MAX)
    reponse_int = 0
    while reponse_int == 0:
        reponse_str = input(f"Calculez {str(a)}  +  {str(b)} : ")
        try:
            reponse_int = int(reponse_str)
        except:
            print("ERREUR, vous devez entrer un nombre.")
            reponse_int = 0
    if reponse_int == a+b:
        print("Réponse correcte")
    else:
        print("Réponse incorrecte")


def poser_question():
    a = random.randint(NB_MIN, NB_MAX)
    b = random.randint(NB_MIN, NB_MAX)
    o = random.randint(0, 1)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    reponse_str = input(f"Calculez {str(a)} {operateur_str} {str(b)} : ")
    reponse_int = int(reponse_str)
    calcul = a+b
    if o == 1:
        calcul = a*b
    if reponse_int == calcul:
        return True
    return False

nb_points = 0
for i in range(0, NB_QUESTIONS):
    #print("Question n°" + str(i+1) + " sur " + str(NB_QUESTIONS))
    print(f"Question n°{i+1} sur {NB_QUESTIONS} : ")
    if poser_question():
        print("Bonne réponse !")
        nb_points += 1
    else:
        print("Mauvaise réponse !")
    print()

print(f"Votre score est de {nb_points}/{NB_QUESTIONS}")
moyenne = int(NB_QUESTIONS/2)
if nb_points == NB_QUESTIONS:
    print("Excellent !")
elif nb_points == 0:
    print("Révisez vos maths !")
elif nb_points == moyenne:
    print("Tout juste !")
elif nb_points > moyenne:
    print("Pas mal")
else:
    print("Peut mieux faire")