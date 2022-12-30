import os
import requests

assert os.path.exists("address.txt"), "Le fichier address.txt n'existe pas"
file = open("address.txt", "r")
address = file.read().split("\n")
final_result = [] 
for addr in address:
    requete = requests.get("https://rdap.db.ripe.net/ip/{}".format(addr))
    dictionnary = requete.json()
    source = (dictionnary["notices"][1]["description"][1])
    name   = (dictionnary["name"])
    last_change = (dictionnary["events"][0]["eventDate"])[0:10]
    dns_tmp = os.popen("nslookup {}".format(addr)).read()
    dns = dns_tmp[dns_tmp.find('name = ')+7:dns_tmp.find("\n")]
    final_result.append({"IP/Masque": addr, "Source": source, "Name": name, "Last change": last_change, "dns": dns})

print("{:<15} | {:<14} | {:<50} | {:<10}| {:<25}".format("IP/Masque", "Source", "Name", "Last change", "dns"))
ch = ""
for i in range(0,(15+14+50+10+25+11)):
    ch = ch + "-"
print(ch)
for value in final_result:
    print("{:<15} | {:<14} | {:<50} | {:<10} | {:<25}".format(value["IP/Masque"], value["Source"], value["Name"], value["Last change"], value["dns"]))
