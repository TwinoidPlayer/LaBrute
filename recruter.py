import requests, time
from bs4 import BeautifulSoup 

print(" === RECRUTER LABRUTE === ")

########################################################################
sid=""
nb_recrut=3
nom="test brute"
dernier=10
########################################################################

cookie = {"sid":sid}

for i in range(nb_recrut):
	url = "http://labrute.muxxu.com/recrut"
	rep_finale = requests.get(url, cookies=cookie)
	soup2 = BeautifulSoup(rep_finale.text, 'html.parser')
	nouvelle_recrue = str(soup2.find_all("a", {"class": "button2"})[0]['href'])
	url = "http://labrute.muxxu.com"+nouvelle_recrue
	nom_b = nom+" "+str(dernier+i+1)
	rep_finale = requests.post(url,data={'name':nom_b,'ok':'on'}, cookies=cookie) 
	print("ok "+str(i+1))
