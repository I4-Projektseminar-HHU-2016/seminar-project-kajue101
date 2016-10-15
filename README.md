# Evaluation of AnkiDroid's Google Play statistics

My project is concerned with the flashcard-learning-app "AnkiDroid", that is described in greater detail in my projects documentation. I found Google Play statistics of this app for the years 2015 and 2016. Among others they include information about installations per country, installations per language and daily crashes per device.
I loaded those csv-files into a python program, did some calculations and visualised the obtained data with the python-library pygal. In addition, as a further part of the project, I created a website, where the results and the documentation of the project are presented.

## Contents ##

- [x] csv-files of the Google Play statistics
- [x] Python-file "Projekt.py" with calculations 
- [x] different visualisations of the results in the folder "charts"
- [x] first project-plan "Projekt_KarolineJüttner.pdf"
- [x] documentation of the project "Dokumentation.pdf"
- [x] website "index.html" in the folder "HTML", with a project presentation and the documentation
- [x] css-file "style.css" to design the website

## Features

- [x] interactive charts (you can hover with the cursor over the charts for more information)
- [x] style examples for the different charts
- [x] different functions to get information out of the csv-files
- [x] website with the embedded charts, further explanations and the documentation
- [] D3 visualisation was also planned, but not realized

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisities

This project was created in Anaconda 4.2.0 and Python 3.5. To run the file "Projekt.py" you will need Python 3. If you did not install it yet, you can get it [here] (https://www.continuum.io/downloads).
To open the file you will need an editor like for example [notepad++] (https://notepad-plus-plus.org/download/v7.html) or [Geany] (https://www.geany.org/Download/Releases).

### Installing

There are only a few things, that could be necessary to make the program run on your computer.

- [] Pull the project or download it as a zip-folder
- [] Install Python 3 on your computer (like already mentioned)
- [] Enter the following commands into your command prompt:

```
pip install ipython
```
```
pip install pygal
```
```
pip install pygal_maps_world
```

- [] Run the file "Projekt.py" to create the charts (not necessary, because I already uploaded the charts, but you can do if you want to test the code - the old files in the folder "charts" will be replaced)


## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## Authors

* **Karoline Jüttner** - [kajue101](https://github.com/kajue101)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* One of the functions in the code was made in cooperation with Philipp Nowak
* The Google Play statistics of the app can be found [here] (https://datahub.io/organization/ankidroid).
* This project was inspired by a team project of last years "Projektseminar Informetie"



*template inspired by [https://gist.github.com/PurpleBooth/109311bb0361f32d87a2](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)*