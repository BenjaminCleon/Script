import os

assert os.path.exists("domaines.txt"), "Le fichier address.txt n'existe pas"
file = open("domaines.txt", "r")
domaines = file.read().split("\n")

final_result = []
for domaine in domaines:

    resultats = os.popen("whois {}".format(domaine)).read().split("\n")
    to_treat = {}
    for resultat in resultats:
        if resultat.__contains__(":"):
            to_treat[resultat.lstrip(" ")[0:resultat.find(":")]] = resultat[resultat.find(":")+1:].lstrip(" ")

    if "anonymous" in to_treat.keys():
        final_result.append({"Domaine": domaine, "Anonyme": to_treat["anonymous"], "Hébergeur": to_treat["registrar"], "Expiration": to_treat["Expiry Date"][0:10], "Créer": to_treat["created"][0:10], "Dernière Mise à jour": to_treat["last-update"][0:10]})
    else:
        final_result.append({"Domaine": domaine, "Anonyme": "YES", "Hébergeur": to_treat["Registrar"], "Expiration": to_treat["Registrar Registration Expiration Date"][0:10], "Créer": to_treat["Creation Date"][0:10], "Dernière Mise à jour": to_treat["Updated Date"][0:10]})

print("{:<30} | {:<10} | {:<20} | {:<10} | {:<10}| {:<10}".format("Domaine", "Anonyme", "Hébergeur", "Expiration", "Créer", "Dernière Mise à jour"))
ch = ""
for i in range(0,(15+14+50+10+25+11)):
    ch = ch + "-"
print(ch)
for value in final_result:
    print("{:<30} | {:<10} | {:<20} | {:<10} | {:<10}| {:<10}".format(value["Domaine"], value["Anonyme"], value["Hébergeur"], value["Expiration"], value["Créer"], value["Dernière Mise à jour"]))
