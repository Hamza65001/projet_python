import sys
#Renseignement de l'utilisateur
print("Bienvenue ! ")
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))

#Sécurité de l'âge
if age < 0 : 
    print("Entrez un âge valide. ")
    sys.exit()
elif age < 18 :
    print("Il faut être majeur pour bénéficier de ce service. ")
    sys.exit()

#renseignement de l'épargne
epargne = int(input("Entrez le montant de votre épargne : "))

#Algorihtme
if age < 25 and epargne > 10000 : 
    print("Profil dynamique : Vous devriez investir en actions\crypto. ")
elif age > 50 : 
    print("Profil prudent : Vous devriez misez sur les obligations et l'immobilier. ")
else :
    print("Profil équilibré : Un mix ETF et épargne classique est recommander. ")
