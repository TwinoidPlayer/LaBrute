import requests, time
from bs4 import BeautifulSoup 

print(" === RETRAITE LABRUTE === ")

########################################################################
sid = "Ysmk42BYKCCUX0qzcwOKZaFsHf2EyCvG"
nb_retraite=2
########################################################################

cookie = {"sid": sid}

url = "http://labrute.muxxu.com/team"
rep_finale = requests.get(url, cookies=cookie)
soup2 = BeautifulSoup(rep_finale.text, 'html.parser')
brutes = []
for a in soup2.find_all("a", {"class": "button2"}, href=True) :
	brutes.append(a['href'])

i = 1
while i <= nb_retraite :
	url1 = "http://labrute.muxxu.com"+brutes[-i]
	rep1 = requests.get(url1, cookies=cookie)
	soup1 = BeautifulSoup(rep1.text, 'html.parser')
	chk = str(soup1.find_all("script")).split("&amp;k=")[1][0:8]
	url2 = "http://labrute.muxxu.com/old?retreat="+brutes[-i][3:]+";chk="+chk
	requests.get(url2, cookies=cookie)
	print("ok "+str(i))
	i+=1	
