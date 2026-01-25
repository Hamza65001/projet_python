import sys
print("Bienvenue ! ")

#Renseignement client
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))

#Sécurité pour l'âge
if age < 0 : 
    print("Entrez un âge valide. ")
    sys.exit()
elif age < 18 :
    print("Il faut être majeur pour bénéficier de ce service. ")
    sys.exit()

#Renseignement Financier
capital_depart = int(input("Entrez votre capital de départ : "))
versement_mensuelle = int(input("Entrez le montant que vous allez verser chaque mois : "))
interet = float(input("Entrez le taux d'intérêt auquel sera soumis votre placement : "))
nb_annee = int(input("Entrez le nombre d'années sur lesquelles vous souhaitez investir : "))

#Calcule
versement_annuel = versement_mensuelle * 12
rendement_final = capital_depart + versement_annuel * (1 + interet / 100)
for i in range(nb_annee) : 
    rendement_final = rendement_final + versement_annuel * (1 + interet / 100)
print(rendement_final + capital_depart)

#Fin du code
