import csv

#Funktionen

#Listen
country_installs = []
#Einlesen
with open ('com-ichi2-anki-country-installs.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=',')
	for row in reader:
		country_installs.append(row)
		
print (country_installs)

#Berechnungen

#Diagramme