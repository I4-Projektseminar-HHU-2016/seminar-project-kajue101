import csv

#Funktionen

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
#Listen für die benötigten Spalten
total_user_installs_2015 = []
laenderabkuerzungen_2015 = []

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
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		country_installs_complete_2015.append(row)
		
with open ('Google Play 2015/com-ichi2-anki-country-ratings.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		country_ratings_2015.append(row)
		
with open ('Google Play 2015/com-ichi2-anki-device-crashes.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		device_crashes_2015.append(row)
		
with open ('Google Play 2015/com-ichi2-anki-language-installs.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		language_installs_2015.append(row)
		
#Einlesen der CSV-Dateien im Ordner Google Play 2016

with open ('Google Play 2016/installs_com.ichi2.anki_201603_country.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		country_installs_2016.append(row)
		
#with open ('Google Play 2016/installs_com.ichi2.anki_201603_overview.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		overview_2016.append(row)

#Voranstehende, bedeutungslose Listenelemente löschen
del country_installs_2015 [0:5]

#Listen mit einzelnen Spalten befüllen
for eintrag in country_installs_2015:
	total_user_installs_2015.append(eintrag[7])
	laenderabkuerzungen_2015.append(eintrag[1])
	
print (total_user_installs_2015)
		

#Berechnungen

#Diagrammeg