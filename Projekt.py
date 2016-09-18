import csv

#Funktionen
def top20(liste1, liste2): #Liste1 und Liste2 werden eingelesen
	top20liste = []
	i = 0
	while i < 20:  #weil nur die ersten 20 betrachtet werden
		top20liste.append(max(liste1)) #die neue Liste bekommt den höchsten Wert von Liste 1 zugeordnet
		top20liste.append(liste2[liste1.index(max(liste1))]) #die neue Liste bekommt den Eintrag von Liste 2 zugeordnet, der den selben Index besitzt wie das Maximum von Liste 1
		liste1[liste1.index(max(liste1))] = 0 #der Maximalwert von Liste 1 wird auf 0 gesetzt, damit im nächsten Durchlauf der nächsthöchste Wert betrachtet werden kann
		i = i+1
	return top20liste
	
def flop20(liste1, liste2): #Liste1 und Liste2 werden eingelesen
	flop20liste = []
	i = 0
	while i < 20:  #weil nur die letzten 20 betrachtet werden
		flop20liste.append(min(liste1)) #die neue Liste bekommt den kleinsten Wert von Liste 1 zugeordnet
		flop20liste.append(liste2[liste1.index(min(liste1))]) #die neue Liste bekommt den Eintrag von Liste 2 zugeordnet, der den selben Index besitzt wie das Minimum von Liste 1
		liste1[liste1.index(min(liste1))] = 10000000 #der Maximalwert von Liste 1 wird auf 10000000 (beliebiger hoher Wert) gesetzt, damit im nächsten Durchlauf der nächstkleinste Wert betrachtet werden kann
		i = i+1
	return flop20liste

#Listen erstellen 
#Listen für die gesamte CSV-Datei
version_crashes_2015 = []
country_installs_2015 = []
country_installs_complete_2015 = []
country_ratings_2015 = []
device_crashes_2015 = []
language_installs_2015 = []
country_installs_2016 = []
overview_2016 = []
language_installs_2016 = []
#Listen für die benötigten Spalten
total_user_installs_2015 = []
total_user_installs_2015_top = []
total_user_installs_2015_top_2 = []
total_user_installs_2015_flop = []
total_user_installs_2015_flop_2 = []
laenderabkuerzungen_2015 = []
total_user_installs_2015_2 = []
total_user_installs_2016 = []
total_user_installs_2016_top = []
total_user_installs_2016_top_2 = []
total_user_installs_2016_flop = []
total_user_installs_2016_flop_2 = []
laenderabkuerzungen_2016 = []
total_user_installs_2016_2 = []
languages_2015 = []
total_user_installs_2015_languages = []
total_user_installs_2015_languages_top = []
total_user_installs_2015_languages_flop = []
total_user_installs_2015_languages_top_2 = []
total_user_installs_2015_languages_flop_2 = []
languages_2016 = []
total_user_installs_2016_languages = []
total_user_installs_2016_languages_top = []
total_user_installs_2016_languages_flop = []
total_user_installs_2016_languages_top_2 = []
total_user_installs_2016_languages_flop_2 = []






#Einlesen der CSV-Dateien im Ordner Google Play 2015
with open ('Google Play 2015/com-ichi2-anki-app-version-crashes.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		version_crashes_2015.append(row) #Speichern der einzelnen Reihen in einer Liste
		
with open ('Google Play 2015/com-ichi2-anki-country-installs.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		country_installs_2015.append(row)
		
with open ('Google Play 2015/com-ichi2-anki-country-installs-complete.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		country_installs_complete_2015.append(row)
		
with open ('Google Play 2015/com-ichi2-anki-country-ratings.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		country_ratings_2015.append(row)
		
with open ('Google Play 2015/com-ichi2-anki-device-crashes.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		device_crashes_2015.append(row)
		
with open ('Google Play 2015/com-ichi2-anki-language-installs.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		language_installs_2015.append(row)
		
#Einlesen der CSV-Dateien im Ordner Google Play 2016

with open ('Google Play 2016/installs_com.ichi2.anki_201603_country.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		country_installs_2016.append(row)
		
with open ('Google Play 2016/installs_com.ichi2.anki_201603_overview.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		overview_2016.append(row)
		
#with open ('Google Play 2016/installs_com.ichi2.anki_201603_language.csv', 'rU') as csv_input:
#	reader = csv.reader(csv_input, delimiter='	')
#	for row in reader:
#		language_installs_2016.append(row)

#Voranstehende, bedeutungslose Listenelemente löschen
del country_installs_2015[0:5]
del country_installs_2016[0] 
del language_installs_2015[0:5]
#del language_installs_2016[0]


#Listen mit einzelnen Spalten befüllen
for eintrag in country_installs_2015:
	total_user_installs_2015.append(eintrag[7])
	laenderabkuerzungen_2015.append(eintrag[1])
	total_user_installs_2015_top.append(eintrag[7])
	total_user_installs_2015_flop.append(eintrag[7])
	
for eintrag in country_installs_2016:
	total_user_installs_2016.append(eintrag[8])
	laenderabkuerzungen_2016.append(eintrag[2])
	total_user_installs_2016_top.append(eintrag[8])
	total_user_installs_2016_flop.append(eintrag[8])
	
for eintrag in language_installs_2015:
	languages_2015.append(eintrag[1])
	total_user_installs_2015_languages.append(eintrag[7])
	total_user_installs_2015_languages_top.append(eintrag[7])
	total_user_installs_2015_languages_flop.append(eintrag[7])
	
for eintrag in language_installs_2016:
	languages_2016.append(eintrag[2])
	total_user_installs_2016_languages.append(eintrag[8])
	total_user_installs_2016_languages_top.append(eintrag[8])
	total_user_installs_2016_languages_flop.append(eintrag[8])

	
#String in int umwandeln
for string in total_user_installs_2015:
	total_user_installs_2015_2.append(int(string))
	total_user_installs_2015_top_2.append(int(string))
	total_user_installs_2015_flop_2.append(int(string))
for string in total_user_installs_2016:
	total_user_installs_2016_2.append(int(string))
	total_user_installs_2016_top_2.append(int(string))
	total_user_installs_2016_flop_2.append(int(string))
	
for string in total_user_installs_2015_languages:
	total_user_installs_2015_languages_top_2.append(int(string))
	total_user_installs_2015_languages_flop_2.append(int(string))
for string in total_user_installs_2016_languages:
	total_user_installs_2016_languages_top_2.append(int(string))
	total_user_installs_2016_languages_flop_2.append(int(string))


#Berechnungen
	
top20installs_country_2015 = top20(total_user_installs_2015_top_2, laenderabkuerzungen_2015)
top20installs_country_2016 = top20(total_user_installs_2016_top_2, laenderabkuerzungen_2016)
flop20installs_country_2015 = flop20(total_user_installs_2015_flop_2, laenderabkuerzungen_2015)
flop20installs_country_2016 = flop20(total_user_installs_2016_flop_2, laenderabkuerzungen_2016)

top20installs_language_2015 = top20(total_user_installs_2015_languages_top_2, languages_2015)
flop20installs_language_2015 = flop20(total_user_installs_2015_languages_flop_2, languages_2015)
#top20installs_language_2016 = top20(total_user_installs_2016_languages_top_2, languages_2016)
#flop20installs_language_2016 = flop20(total_user_installs_2016_languages_flop_2, languages_2016)

print (total_user_installs_2015_languages_flop_2)
		

#Diagramme

#TODO: D3 Diagramm mit den Informationen aus country_installs_2015 und country_installs_2016