import requests, time
from bs4 import BeautifulSoup 

print(" === COMBAT LABRUTE === ")

########################################################################
sid = "Ysmk42BYKCCUX0qzcwOKZaFsHf2EyCvG"
########################################################################

cookie = {"sid": sid}
url = "http://labrute.muxxu.com/team"
rep_finale = requests.get(url, cookies=cookie)
soup2 = BeautifulSoup(rep_finale.text, 'html.parser')
brutes = []
for a in soup2.find_all("a", {"class": "button2"}, href=True) :
	brutes.append(a['href'])

for brute in brutes :
	url_choix = "http://labrute.muxxu.com"+brute
	rep_choix = requests.get(url_choix, cookies=cookie)
	soup_choix = BeautifulSoup(rep_choix.text, 'html.parser')
	chk = str(soup_choix.find_all("script")).split("&amp;k=")[1][0:8]

	tournoi_fin = "http://labrute.muxxu.com/t/quit"
	rep_tournoi_fin = requests.get(tournoi_fin, cookies=cookie)
	
	tournoi_fin = "http://labrute.muxxu.com/t/1333588/quit?chk="+chk
	rep_tournoi_fin = requests.get(tournoi_fin, cookies=cookie)
	
	tournoi_new = "http://labrute.muxxu.com/t/join"
	rep_tournoi_new = requests.get(tournoi_new, cookies=cookie)
	
	HOPI = False
	while True :
		test_lvl_up = "http://labrute.muxxu.com"+brute
		rep_test_lvl_up = requests.get(test_lvl_up, cookies=cookie)
		soup_test_lvl_up = BeautifulSoup(rep_test_lvl_up.text, 'html.parser')		
		if str(soup_test_lvl_up.find_all('a',{"class": "button4"}, href=True)[0]['href'][-7:]) == "levelup":
			choix_lvl_up = "http://labrute.muxxu.com"+brute+"/levelup?c=0;chk="+chk
			rep_choix_lvl_up = requests.get(choix_lvl_up, cookies=cookie)
			
		try:
			url_choix = "http://labrute.muxxu.com"+brute+"/train"
			rep_choix = requests.get(url_choix, cookies=cookie)
			soup_choix = BeautifulSoup(rep_choix.text, 'html.parser')
			url_combat = "http://labrute.muxxu.com"+soup_choix.find_all("a", {"class": "button2"}, href=True)[0]['href']
			requests.get(url_combat, cookies=cookie)
						
		except IndexError:
			if not HOPI :
				HOPI = True
				url_mort = "http://labrute.muxxu.com"+brute
				rep_mort = requests.get(url_mort, cookies=cookie)
				soup_mort = BeautifulSoup(rep_mort.text, 'html.parser')
				url_potion = "http://labrute.muxxu.com"+soup_mort.find_all("a", {"class": "button4"}, href=True)[1]['href']
				requests.get(url_potion, cookies=cookie)
			else:
				print("ok "+brute[3:])
				break

	tournoi_new = "http://labrute.muxxu.com/t/join"
	rep_tournoi_new = requests.get(tournoi_new, cookies=cookie)
	
print("========= FIN =========")
