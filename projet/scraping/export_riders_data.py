#!/bin/python3

import requests
import pandas as pd
import bs4
import time

# Renvoie le nombre de PCS en 2023 pour un coureur

def find_pcs_points(html):
	h3 = html.find_all("h3")	
	ranking = None

	for title in h3:
		if title.string=="PCS Ranking position per season":
			ranking = title.parent.find("table")       
			continue

	table = ranking.find("tbody")

	for row in table.find_all("tr"):
		if row.find("td").string=="2023":
			break

	return int(row.find("div", class_="vTitle").string)

# Renvoie un tableau qui correspond aux points PCS dans les
# differentes categories d'un coureur :
# Points sur les courses d'un jour
# Points sur les classements generaux
# Points sur les contre la montre
# Points sur les sprints
# Points en montagne

def find_speciality_points(html):
	h4 = html.find_all("h4")
	rankings = []

	for title in h4:
		if title.string=="Points per specialty":
			break

	for li in title.parent.find_all("li"):
		rankings.append(int(li.find("div", class_="pnt").string))

	return rankings

# Renvoie l'equipe 2023 d'un coureur

def find_2023_team(html):
	h3 = html.find_all("h3")
	team = ""

	for title in h3:
		if title.string=="Teams":
			teams = title.parent.parent.find_all("div")[1]
			break

	for li in teams.find_all("li"):
		season = li.find("div", class_="season")

		if season.string=="2023":
			team = season.next_sibling
			break

	res = team.find("a")

	if res!=-1:
		return res.string

	for i in teams.find_all("a"):
		if "team" in i.get("href"):
			return i.string

res =[""]
res[0] = ["Rank","Prev","Diff","Rider","Team","Points","Date_of_birth","Nationality","Weight","Height","PCS_points","One_dav_races","GC","Time_trial","Sprint","Cimber"]
liens_coureurs = []
n=0
a=1
maxi = 500

#recuperer listes des  500 premiers coureurs au classement PCS
while(n<maxi):
	url_api = "https://www.procyclingstats.com/rankings.php?nation=&age=&zage=&page=smallerorequal&team=&offset="+ str(n) +"&teamlevel=&filter=Filter"
	req = requests.get(url_api)
	# On utilise beautifulsoup pour formater le code source
	page = bs4.BeautifulSoup(req.text , "html.parser" )
	
	#On recupere le tableau
	tabs = page.find_all("table")

	for tab in tabs :
		for line in tab.find_all("tr") :
			elems = line.find_all("td")
			resline =[]
			i=0
			for elem in elems :
				resline = resline +[elem.text.strip()]
				for lien in elem.find_all("a"):
					a=a+1
					if(len(str(lien.get("href")))>1):
						if(str(lien.get("href"))[0]=="r" and str(lien.get("href"))[1]=="i" and str(lien.get("href"))[2]=="d" and str(lien.get("href"))[3]=="e" and str(lien.get("href"))[4]=="r" and str(lien.get("href"))[5]=="/"):	
							liens_coureurs=liens_coureurs+[str(lien.get("href"))]

			if(resline!=[]):
				res = res +[resline]
	n=n+100								

for i in range(0,len(liens_coureurs)):
		liens_coureurs[i]="https://procyclingstats.com/"+liens_coureurs[i]


nb=0
dob=[]
nat=[]
poids=[]
taille=[]
pcs=[]
sp=[]
a=0
team=[]
for url in liens_coureurs:
	a=a+1
	nb=nb+1
	if(nb==50):
		time.sleep(1)
		nb=0
	print(f"\r{str(a)} / {str(maxi)}", end="")
	n=n+1
	req = requests.get(url)
	page=bs4.BeautifulSoup(req.text , "html.parser" )
	div = page.find("div", {'class':"rdr-info-cont"})
	infos = div.get_text()
	
	#dob
	dob = dob + [infos[infos.find("birth: ")+len("birth: "):(infos.find("(")-infos.find("birth: ")+len("birth: "))]]
	
	#nationalite
	if(infos.find("kg")!=-1):
		nat= nat + [infos[infos.find("Nationality: ")+len("Nationality: "):(infos.find("kg")-11)]]
	elif(infos.find("mPlace")!=-1):
		nat= nat + [infos[infos.find("Nationality: ")+len("Nationality: "):(infos.find("mPlace")-len("Height: 1.73 "))]]
	else:
		nat=nat+[""]
		
	#poids
	if(infos.find("kg")!=-1):	
		poids = poids + [infos[infos.find("kg")-3:infos.find("kg")-1]]
	else:
		poids= poids +[""]
	#taille
	if(infos.find("Height: ")!=-1):
		if(infos.find("mPlace")!=-1):
			taille = taille + [infos[infos.find("Height: ")+len("Height: "):infos.find("mPlace")-1]]
		else:
			taille=taille+[""]
	else:
		taille=taille+[""]+ [infos[infos.find("Height: ")+len("Height: "):infos.find("mPoints")-1]]
	
	pcs=pcs+[find_pcs_points(page)]
	
	sp=sp+[find_speciality_points(page)]
	
	team=team+[find_2023_team(page)]
		
				
for i in range(1,len(dob)+1):
	res[i]=res[i]+[dob[i-1]]+[nat[i-1]]+[poids[i-1]]+[taille[i-1]]+[pcs[i-1]]
	for j in range(0,len(sp[i-1])):
		res[i]=res[i]+[sp[i-1][j]]
			


#nettoyage
for i in range (1,len(res)) :
	if(res[i][2]=="-"):
		res[i][2]=res[i][2][1:len(res[i][2])]
	elif(res[i][2][0]=="▼"):
		res[i][2]=res[i][2][1:len(res[i][2])]
		res[i][2]="-"+str(res[i][2])
	else:
		res[i][2]=res[i][2][1:len(res[i][2])]
		res[i][2]="+"+str(res[i][2])

index=[]
for i in range (0,len(res)):
	index.append(i)

df = pd.DataFrame(res,index=index)


for i in range(0,len(team)):
	df[4][i+1]=team[i]
	if(len(df[9][i])>6):
		df[9][i]=""

df=df.drop(310)
df.to_csv("out/coureurs2023.csv", header=False, index=False, sep=";", mode="w")
print()
