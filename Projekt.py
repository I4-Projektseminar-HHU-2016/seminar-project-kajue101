import csv


#Funktionen

#Funktion zur Berechnung der Top20
def top20(liste1, liste2): #Liste1 und Liste2 werden eingelesen
	top20liste = []
	i = 0
	while i < 20:  #weil nur die ersten 20 betrachtet werden
		top20liste.append(max(liste1)) #die neue Liste bekommt den höchsten Wert von Liste 1 zugeordnet
		top20liste.append(liste2[liste1.index(max(liste1))]) #die neue Liste bekommt den Eintrag von Liste 2 zugeordnet, der den selben Index besitzt wie das Maximum von Liste 1
		liste1[liste1.index(max(liste1))] = 0 #der Maximalwert von Liste 1 wird auf 0 gesetzt, damit im nächsten Durchlauf der nächsthöchste Wert betrachtet werden kann
		i = i+1
	return top20liste

#Funktion zur Berechnung der Flop20
def flop20(liste1, liste2): #Liste1 und Liste2 werden eingelesen
	flop20liste = []
	i = 0
	while i < 20:  #weil nur die letzten 20 betrachtet werden
		flop20liste.append(min(liste1)) #die neue Liste bekommt den kleinsten Wert von Liste 1 zugeordnet
		flop20liste.append(liste2[liste1.index(min(liste1))]) #die neue Liste bekommt den Eintrag von Liste 2 zugeordnet, der den selben Index besitzt wie das Minimum von Liste 1
		liste1[liste1.index(min(liste1))] = 10000000 #der Maximalwert von Liste 1 wird auf 10000000 (beliebiger hoher Wert) gesetzt, damit im nächsten Durchlauf der nächstkleinste Wert betrachtet werden kann
		i = i+1
	return flop20liste
	
#Funktion zur Berechnung der Flop40
def flop40(liste1, liste2): #Liste1 und Liste2 werden eingelesen
	flop40liste = []
	i = 0
	while i < 40:  #weil nur die letzten 20 betrachtet werden
		flop40liste.append(min(liste1)) #die neue Liste bekommt den kleinsten Wert von Liste 1 zugeordnet
		flop40liste.append(liste2[liste1.index(min(liste1))]) #die neue Liste bekommt den Eintrag von Liste 2 zugeordnet, der den selben Index besitzt wie das Minimum von Liste 1
		liste1[liste1.index(min(liste1))] = 10000000 #der Maximalwert von Liste 1 wird auf 10000000 (beliebiger hoher Wert) gesetzt, damit im nächsten Durchlauf der nächstkleinste Wert betrachtet werden kann
		i = i+1
	return flop40liste
	
def aufsteigend(liste1, liste2): #Liste1 und Liste2 werden eingelesen
	aufsteigendeliste = []
	i = 0
	k = len(liste1)
	while i < k:  #weil nur die letzten 20 betrachtet werden
		aufsteigendeliste.append(min(liste1)) #die neue Liste bekommt den kleinsten Wert von Liste 1 zugeordnet
		aufsteigendeliste.append(liste2[liste1.index(min(liste1))]) #die neue Liste bekommt den Eintrag von Liste 2 zugeordnet, der den selben Index besitzt wie das Minimum von Liste 1
		del(liste2[liste1.index(min(liste1))])
		del(liste1[liste1.index(min(liste1))])
		i = i+1
	return aufsteigendeliste
	
def summe(liste):
	summe = 0
	for i in liste:
		summe += i
	return summe
	
def differenz_in_prozent(wert1,wert2):
	float(wert1)
	float(wert2)
	diff = wert1/wert2
	diff = diff*100
	return diff

def splitlist1(liste):
	newlist1=[]
	i = 0
	k = len(liste)
	while i < k:
		newlist1.append(liste[i])
		i+=2
	return newlist1
	
def splitlist2(liste):
	newlist2=[]
	i = 1
	k = len(liste)
	while i < k:
		newlist2.append(liste[i])
		i+=2
	return newlist2
	

	
	
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
country_installs_complete_2016 = []

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
crashes_2015 = []
crashes_2015_2 = []
crashes_2015_top = []
crashes_2015_flop = []
crashes_2015_top_2 = []
crashes_2015_flop_2 = []
devices = []
crashes_2015_version = []
crashes_2015_version_2 = []
version = []
version_2 = []
laenderabkuerzungen_2015_ratings = []
ratings_2015 = []
ratings_2015_2 = []
daily_installs_2015 = []
daily_installs_2015_2 = []
daily_installs_2016 = []
daily_installs_2016_2 = []
current_user_installs_2015 = []
current_user_installs_2015_2 = []
total_user_installs_2015_complete = []
total_user_installs_2015_complete_2 = []
current_user_installs_2016 = []
current_user_installs_2016_2 = []
total_user_installs_2016_complete = []
total_user_installs_2016_complete_2 = []
daily_installs_2015_complete = []
daily_installs_2015_complete_2 = []
daily_uninstalls_2015_complete = []
daily_uninstalls_2015_complete_2 = []
daily_installs_2016_complete = []
daily_installs_2016_complete_2 = []
daily_uninstalls_2016_complete = []
daily_uninstalls_2016_complete_2 = []


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
		country_ratings_2015.append(row) #Bewertungen sind kaputt
		
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
		
with open ('Google Play 2016/installs_com.ichi2.anki_201603_language.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		language_installs_2016.append(row)
		
with open ('Google Play 2016/installs_com.ichi2.anki_201603_country_complete.csv', 'rU') as csv_input:
	reader = csv.reader(csv_input, delimiter=';')
	for row in reader:
		country_installs_complete_2016.append(row)

		
#Voranstehende, bedeutungslose Listenelemente löschen
del country_installs_2015[0:5]
del country_installs_2016[0] 
del language_installs_2015[0:5]
del language_installs_2016[0:3]
del device_crashes_2015[0:5]
del version_crashes_2015[0:5]
del version_crashes_2015[-1]
del country_ratings_2015[0:5]
del country_installs_complete_2015[0:6]
del country_installs_complete_2016[0:1]


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
	
for eintrag in device_crashes_2015:
	devices.append(eintrag[1])
	crashes_2015.append(eintrag[2])
	crashes_2015_top.append(eintrag[2])
	crashes_2015_flop.append(eintrag[2])
	
for eintrag in version_crashes_2015:
	version.append(eintrag[1])
	crashes_2015_version.append(eintrag[2])
	
for eintrag in country_ratings_2015:
	laenderabkuerzungen_2015_ratings.append(eintrag[1])
	ratings_2015.append(eintrag[3])
	
for eintrag in country_installs_complete_2015:
	daily_installs_2015.append(eintrag[8])
	current_user_installs_2015.append(eintrag[6])
	total_user_installs_2015_complete.append(eintrag[7])
	daily_installs_2015_complete.append(eintrag[8])
	daily_uninstalls_2015_complete.append(eintrag[9])
	
for eintrag in country_installs_complete_2016:
	daily_installs_2016.append(eintrag[9])
	current_user_installs_2016.append(eintrag[7])
	total_user_installs_2016_complete.append(eintrag[8])
	daily_installs_2016_complete.append(eintrag[9])
	daily_uninstalls_2016_complete.append(eintrag[10])

	
#String in Integer umwandeln
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
	
for string in crashes_2015:
	crashes_2015_2.append(int(string))
	crashes_2015_top_2.append(int(string))
	crashes_2015_flop_2.append(int(string))
	
for string in crashes_2015_version:
	crashes_2015_version_2.append(int(string))
	
for string in version:
	version_2.append(int(string))
	
for string in ratings_2015:
	ratings_2015_2.append(float(string))

for string in daily_installs_2015:
	daily_installs_2015_2.append(int(string))
	
for string in daily_installs_2016:
	daily_installs_2016_2.append(int(string))
	
for string in current_user_installs_2015:
	current_user_installs_2015_2.append(int(string))
	
for string in total_user_installs_2015_complete:
	total_user_installs_2015_complete_2.append(int(string))
	
for string in current_user_installs_2016:
	current_user_installs_2016_2.append(int(string))
	
for string in total_user_installs_2016_complete:
	total_user_installs_2016_complete_2.append(int(string))
	
for string in daily_installs_2015_complete:
	daily_installs_2015_complete_2.append(int(string))

for string in daily_uninstalls_2015_complete:
	daily_uninstalls_2015_complete_2.append(int(string))
	
for string in daily_installs_2016_complete:
	daily_installs_2016_complete_2.append(int(string))

for string in daily_uninstalls_2016_complete:
	daily_uninstalls_2016_complete_2.append(int(string))




#Berechnungen
	
top20installs_country_2015 = top20(total_user_installs_2015_top_2, laenderabkuerzungen_2015)
top20installs_country_2016 = top20(total_user_installs_2016_top_2, laenderabkuerzungen_2016)
flop20installs_country_2015 = flop20(total_user_installs_2015_flop_2, laenderabkuerzungen_2015)
flop20installs_country_2016 = flop20(total_user_installs_2016_flop_2, laenderabkuerzungen_2016)

top20installs_language_2015 = top20(total_user_installs_2015_languages_top_2, languages_2015)
flop40installs_language_2015 = flop40(total_user_installs_2015_languages_flop_2, languages_2015)
top20installs_language_2016 = top20(total_user_installs_2016_languages_top_2, languages_2016)
flop40installs_language_2016 = flop40(total_user_installs_2016_languages_flop_2, languages_2016)

top20crashes_2015 = top20(crashes_2015_top_2, devices)
flop40crashes_2015 = flop40(crashes_2015_flop_2, devices)

versionen_crashes_aufsteigend = aufsteigend(version_2, crashes_2015_version_2)

summe_installs_2015 = summe(daily_installs_2015_2)

summe_installs_2016 = summe(daily_installs_2016_2)

summe_crashes_2015 = summe(crashes_2015_2)

summe_current_user_installs_2015 = summe(current_user_installs_2015_2)
summe_total_user_installs_2015 = summe(total_user_installs_2015_complete_2)
behalten_quote_2015 = differenz_in_prozent(summe_current_user_installs_2015, summe_total_user_installs_2015)

summe_current_user_installs_2016 = summe(current_user_installs_2016_2)
summe_total_user_installs_2016 = summe(total_user_installs_2016_complete_2)
behalten_quote_2016 = differenz_in_prozent(summe_current_user_installs_2016, summe_total_user_installs_2016)

summe_current_user_installs_gesamt = summe_current_user_installs_2015+summe_current_user_installs_2016
summe_total_user_installs_gesamt = summe_total_user_installs_2015+summe_total_user_installs_2016
behalten_quote_gesamt = differenz_in_prozent(summe_current_user_installs_gesamt, summe_total_user_installs_gesamt)

deinstallationsquote_2015 = 100 - behalten_quote_2015
deinstallationsquote_2016 = 100 - behalten_quote_2016
deinstallationsquote_gesamt = 100 - behalten_quote_gesamt

summe_daily_installs_2015 = summe(daily_installs_2015_complete_2)
summe_daily_uninstalls_2015 = summe(daily_uninstalls_2015_complete_2)
summe_daily_installs_2016 = summe(daily_installs_2016_complete_2)
summe_daily_uninstalls_2016 = summe(daily_uninstalls_2016_complete_2)

differenz_installs_uninstalls_2015 = summe_daily_installs_2015 - summe_daily_uninstalls_2015
differenz_installs_uninstalls_2016 = summe_daily_installs_2016 - summe_daily_uninstalls_2016

version_list = splitlist1(versionen_crashes_aufsteigend)
crashes_list = splitlist2(versionen_crashes_aufsteigend)

crashes_list_2 = splitlist1(top20crashes_2015)
devices_list = splitlist2(top20crashes_2015)
crashes_list_flop = splitlist1(flop40crashes_2015)
devices_list_flop = splitlist2(flop40crashes_2015)	
language_list_1 = splitlist2(top20installs_language_2015)
installs_list_1 = splitlist1(top20installs_language_2015)
language_list_2 = splitlist2(top20installs_language_2016)
installs_list_2 = splitlist1(top20installs_language_2016)
language_list_3 = splitlist2(flop40installs_language_2015)
installs_list_3 = splitlist1(flop40installs_language_2015)
language_list_4 = splitlist2(flop40installs_language_2016)
installs_list_4 = splitlist1(flop40installs_language_2016)

laenderabkuerzungen_2015_klein = []
laenderabkuerzungen_2016_klein = []
laenderabkuerzungen_2015_ratings_klein = []

for eintrag in laenderabkuerzungen_2015:
	laenderabkuerzungen_2015_klein.append(eintrag.lower())
for eintrag in laenderabkuerzungen_2016:
	laenderabkuerzungen_2016_klein.append(eintrag.lower())
for eintrag in laenderabkuerzungen_2015_ratings:
	laenderabkuerzungen_2015_ratings_klein.append(eintrag.lower())


country_dictionary_2015 = dict(zip(laenderabkuerzungen_2015_klein, total_user_installs_2015_2))
country_dictionary_2016 = dict(zip(laenderabkuerzungen_2016_klein, total_user_installs_2016_2))
ratings_dictionary_2015 = dict(zip(laenderabkuerzungen_2015_ratings_klein, ratings_2015_2))
print (ratings_dictionary_2015)

#Diagramme

import pygal
from IPython.display import SVG
from pygal.style import NeonStyle
from pygal.style import LightenStyle
from pygal.style import Style

#Horizontales Histogramm mit Vergleich zwischen Installationszahlen 2015 und 2016
chart = pygal.HorizontalBar(style=NeonStyle,legend_box_size=20)
chart.title = 'Installationen 2015 und 2016'
chart.add('2015', summe_installs_2015, rounded_bars=5)
chart.add('2016', summe_installs_2016, rounded_bars=5)
chart.render_to_file('charts/installs_compared_2015_2016.svg')

#Kreisdiagramm mit Deinstallations- und "Behalten"-Quote von 2015
pie_chart = pygal.Pie(style=NeonStyle,legend_box_size=20)
pie_chart.title = 'Deinstallationsquote 2015'
pie_chart.add('Deinstalliert in %', round(deinstallationsquote_2015,1))
pie_chart.add('Behalten in %', round(behalten_quote_2015,1))
pie_chart.render_to_file('charts/uninstalls_2015.svg')

#Kreisdiagramm mit Deinstallations- und "Behalten"-Quote von 2016
pie_chart = pygal.Pie(style=NeonStyle,legend_box_size=20)
pie_chart.title = 'Deinstallationsquote 2016'
pie_chart.add('Deinstalliert in %', round(deinstallationsquote_2016,1))
pie_chart.add('Behalten in %', round(behalten_quote_2016,1))
pie_chart.render_to_file('charts/uninstalls_2016.svg')

#Kreisdiagramm mit Deinstallations- und "Behalten"-Quote von 2015 und 2016 zusammen
pie_chart = pygal.Pie(style=NeonStyle,legend_box_size=20)
pie_chart.title = 'Deinstallationsquote 2015 und 2016'
pie_chart.add('Deinstalliert in %', round(deinstallationsquote_gesamt,1))
pie_chart.add('Behalten in %', round(behalten_quote_gesamt,1))
pie_chart.render_to_file('charts/uninstalls_2015_2016.svg')

#Kreisdiagramm als Vergleich zwischen täglichen Installationen und Deinstallationen 2015
pie_chart = pygal.Pie(style=NeonStyle,legend_box_size=20)
pie_chart.title = 'Vergleich zwischen täglichen Installationen und Deinstallationen 2015'
pie_chart.add('Tägliche Installationen', summe_daily_installs_2015)
pie_chart.add('Tägliche Deinstallationen', summe_daily_uninstalls_2015)
pie_chart.render_to_file('charts/installs_uninstalls_daily_2015.svg')

#Kreisdiagramm als Vergleich zwischen täglichen Installationen und Deinstallationen 2016
pie_chart = pygal.Pie(style=NeonStyle,legend_box_size=20)
pie_chart.title = 'Vergleich zwischen täglichen Installationen und Deinstallationen 2016'
pie_chart.add('Tägliche Installationen', summe_daily_installs_2016)
pie_chart.add('Tägliche Deinstallationen', summe_daily_uninstalls_2016)
pie_chart.render_to_file('charts/installs_uninstalls_daily_2016.svg')

#Graph soll Zusammenhang zwischen App-Versionen und Abstürzen zeigen
line_chart = pygal.Line(fill=True,style=NeonStyle,legend_box_size=20)
line_chart.title = 'Tägliche Abstürze pro App-Version'
line_chart.x_labels = version_list
line_chart.add('Abstürze',crashes_list)
line_chart.render_to_file('charts/version_crashes.svg')

#Histogramm aus den 20 Geräten, die die meisten Abstürze verzeichnen
line_chart = pygal.Bar(style=NeonStyle,legend_box_size=20)
line_chart.title = '20 Geräte mit den meisten täglichen Abstürzen'
line_chart.x_labels = devices_list
line_chart.add('Abstürze', crashes_list_2, rounded_bars=5)
line_chart.render_to_file('charts/top20_device_crashes.svg')

#Histogramm aus den 40 Geräten, die die wenigsten Abstürze verzeichnen
line_chart = pygal.Bar(style=NeonStyle,legend_box_size=20)
line_chart.title = '40 Geräte mit den wenigsten täglichen Abstürzen'
line_chart.x_labels = devices_list_flop
line_chart.add('Abstürze', crashes_list_flop, rounded_bars=5)
line_chart.render_to_file('charts/flop40_device_crashes.svg')

#Histogramm mit den 20 Sprachen, in denen die App 2015 am häufigsten installiert wurde
line_chart = pygal.Bar(style=NeonStyle,legend_box_size=20)
line_chart.title = 'Die 20 am häufigsten installierten Sprachen 2015'
line_chart.x_labels = language_list_1
line_chart.add('Installationen', installs_list_1, rounded_bars=5)
line_chart.render_to_file('charts/top20_language_installs_2015.svg')

#Histogramm mit den 20 Sprachen, in denen die App 2016 am häufigsten installiert wurde
line_chart = pygal.Bar(style=NeonStyle,legend_box_size=20)
line_chart.title = 'Die 20 am häufigsten installierten Sprachen 2016'
line_chart.x_labels = language_list_2
line_chart.add('Installationen', installs_list_2, rounded_bars=5)
line_chart.render_to_file('charts/top20_language_installs_2016.svg')

#Histogramm mit den 40 Sprachen, in denen die App 2015 am seltensten installiert wurde
line_chart = pygal.Bar(style=NeonStyle,legend_box_size=20)
line_chart.title = 'Die 40 am seltensten installierten Sprachen 2015'
line_chart.x_labels = language_list_3
line_chart.add('Installationen', installs_list_3, rounded_bars=5)
line_chart.render_to_file('charts/flop40_language_installs_2015.svg')

#Histogramm mit den 40 Sprachen, in denen die App 2016 am seltensten installiert wurde
line_chart = pygal.Bar(style=NeonStyle,legend_box_size=20)
line_chart.title = 'Die 40 am seltensten installierten Sprachen 2016'
line_chart.x_labels = language_list_4
line_chart.add('Installationen', installs_list_4, rounded_bars=5)
line_chart.render_to_file('charts/flop40_language_installs_2016.svg')

#Style für die Weltkarten
from pygal.style import Style
world_style = Style(
  background='transparent',
  plot_background='#E0F2F7',
  foreground='black',
  foreground_strong='black',
  foreground_subtle='#0B6121',
  font_family='arial',
  opacity='.6',
  opacity_hover='.9',
  transition=None,
  colors=('#04B404', 'green', 'green', 'green'))

#Weltkarte der Installationen weltweit 2015
worldmap_chart = pygal.maps.world.World(style=world_style)
worldmap_chart.title = 'Weltweite Installationen 2015'
worldmap_chart.add('Installationen', country_dictionary_2015)
worldmap_chart.render_to_file('charts/world_map_installs_2015.svg')

#Weltkarte der Installationen weltweit 2016
worldmap_chart = pygal.maps.world.World(style=world_style)
worldmap_chart.title = 'Weltweite Installationen 2016'
worldmap_chart.add('Installationen', country_dictionary_2016)
worldmap_chart.render_to_file('charts/world_map_installs_2016.svg')

#Weltkarte der App_Bewertungen
worldmap_chart = pygal.maps.world.World(style=world_style)
worldmap_chart.title = 'Weltweite Bewertungen 2015'
worldmap_chart.add('Bewertungen', ratings_dictionary_2015)
worldmap_chart.render_to_file('charts/world_map_ratings_2015.svg')
